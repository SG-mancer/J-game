
# declared characters:
define barry = Character("Barry", kind=nvl, color="#33ccff") ## The player character that will be default - Dylan Barry
define ryan = Character("Ryan", kind=nvl, color="#33ccff") ## Younger character Bradly Ryan
define z = barry ## The player character


define narrator = nvl_narrator


#background images
image bg japanflight = "ausflight.png"
image bg flightmap = "flightplan.png"
image fltcon = "flight_icon.png" 
image bg planner = "planner.png"
image nihoznmap = "nihonmap_empty.png"


# MULTIPLE CHOICE Form - From: https://lemmasoft.renai.us/forums/viewtopic.php?t=2899 
init python:
    def set_variable(name, value):
        setattr(store, name, value)
        return True

    setsvar = renpy.curry(set_variable)

    def choicebutton(label, var, value, **properties):
        if getattr(store, var) == value:
            role = "selected_"
        else:
            role = ""

        ui.textbutton(label, clicked=setsvar(var, value), role=role, **properties)


# STATUS POPUP
screen healthscreen():
    frame:
        align (0.95, 0.05)
        xmaximum 250
        vbox:
            text "Week [week_count]"
            text u""
            text u"fatigue levels:"
            text u"{color=#6699ff}Social: [soci]{/color}"
            bar value AnimatedValue(value=soci, range=max_stat, delay=2.0)

            text u"{color=#33cc33}Physical: [phys]{/color}"
            bar value AnimatedValue(value=phys, range=max_stat, delay=2.0)

            text u"{color=#ff3300}Mental: [ment]{/color}"
            bar value AnimatedValue(value=ment, range=max_stat, delay=2.0)

            text u""

            text "Knoweldge: [Ability[0]]"
            bar value AnimatedValue(value=(Ability[0]), range=100, delay=2.0)
            text "Receptive Skills: [Ability[3]]"
            bar value AnimatedValue(value=(Ability[3]), range=100, delay=2.0)
            text "Productive Skills:[Ability[4]]"
            bar value AnimatedValue(value=(Ability[4]), range=100, delay=2.0)
            text u""            
            text u"Cash:  \n¥[yenYen]"
            

        
# ---------------
# the story starts here...
label start:
    # # # # # # # # # # #
    # set up variables
    # # # # # # # # # # #

    ## Language Ability = 0_Vocab, 1_Grammar, 2_Reading, 3_Listing, 4_Writing/Speaking
    $ Ability = [0,0,0,0,0]

    ## Fatigue STATS - Social, Physical, Mental
    $ soci = 2
    $ phys = 2
    $ ment = 2
    $ max_stat = 5

    ## Starting money (approx 20% deposit for a house $87,000AUD * 70yen/$ approx 6,000,000yen)
    $ yenYen = 0 # cash remaining
    $ spentY = 0 # cash spent
    $ week_count = 0


    # variables for tracking choices made using weekly study planner
    $ study = ['0','0','0','0','0'] #choice of what to study for the week
    $ studyA = '0' #it was easier to just handle these strings for the time table options... Early morning
    $ studyB = '0' #Morning
    $ studyC = '0' #Evening
    $ studyD = '0' #Night
    $ studyE = '0' #is actually the weekend option

    $ timeMan = False #gets extra study session studyD
    $ earlyBird = True #allows studyA

    # Options for the weekly study planner
    $ studMeths = ['jog','nap'] #starting options for studying before/after class
    $ wkendMeths = ['shopping','museum','walking','computer games'] #The options available to player at the weekend starting

    # Tracking bonuses for the week (and past two weeks - for bonuses)
    $ konshuAbil = [1,2,3,4,5]
    $ senshuAbil = konshuAbil # last weeks Ability modifier
    $ sensenAbil = senshuAbil # week before lasts Ability modifier
    $ senshuStudy = study

    jump looper

    return 



    # # # # # # # # # # #
    # adventures in Japan
    # # # # # # # # # # #
label looper:
    ## The time table is hard coded
    ## If events happen in a week, the week ends by jumping to looper

    while week_count < 52:
        
        $ week_count += 1
        $ sensenAbil = senshuAbil # week before lasts Ability modifier
        $ senshuAbil = konshuAbil # last weeks Ability modifier

        "[Ability]"

        if week_count == 1:
            jump beginning
        elif week_count == 25:
            "Half year ceremony"
        elif week_count == 51:
            "School Graduation ceremony"
        elif week_count in [15,24,38,50]:
            "School exam"
        elif week_count in [5,6,13,26,27,39,40,52]:
            call holidays
        elif week_count in [14,36]:
            "JLPT"
        else:
            #studying week
            if week_count in [17,29,32,42,46]:
                #flavour text for long weekened
                "Long weekend"
            jump timetable #Then it jumps to studyCal before jumping back to looper here
    
    # If there has been 52 weeks already, the game ends with you stuck in Japan?

    return