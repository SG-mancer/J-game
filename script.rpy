
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
            text u"{color=#6699ff}Fatigue: [fatig]{/color}"
            bar value AnimatedValue(value=fatig, range=max_stat, delay=2.0)

            text u"{color=#33cc33}Motivation: [motiv]{/color}"
            bar value AnimatedValue(value=motiv, range=max_stat, delay=2.0)

            text u"{color=#ff3300}Confidence: [confi]{/color}"
            bar value AnimatedValue(value=confi, range=max_stat, delay=2.0)

            text "Knoweldge:"
            bar value AnimatedValue(value=(Ability[0]+Ability[1]), range=100, delay=2.0)
            text "Receptive Skills: [Ability[2]]"
            bar value AnimatedValue(value=(Ability[2]+Ability[3]), range=100, delay=2.0)
            text "Productive Skills:[Ability[4]]"
            bar value AnimatedValue(value=(Ability[4]+Ability[5]), range=100, delay=2.0)            
            text u"Cash:  \n¥[yenYen], $[aus]"
            

        
# ---------------
# the story starts here...
label start:
    # # # # # # # # # # #
    # set up variables
    # # # # # # # # # # #
    ## Ability = Vocab, Grammar (Knoweldge); Reading, Listing (receptive/consuming); Writing, Speaking (protive/producing)
    $ Ability = [0,0,0,0,0,0]
    ## STATS = Fatigue, Motivation and Confidence
    $ fatig = 2
    $ motiv = 2
    $ confi = 2
    $ max_stat = 5
    ## Starting money (approx 20% deposit for a house $87,000AUD * 70yen/$ approx 6,000,000yen)
    $ aus = 87000
    $ yenYen = 0 # cash remaining
    $ spentY = 0 # cash spent
    $ week_count = 0

    ## Tuition cost is 700,000yen
    ## living cost 200,000yen = 2,400,000 yen for year
    ## On application form need to say your goal ...


    $ study = ['0','0','0','0','0'] #choice of what to study for the week
    $ studyA = '0' #it was easier to just handle these strings for the time table options...
    $ studyB = '0'
    $ studyC = '0'
    $ studyD = '0'
    $ studyE = '0'

    $ studMeths = ['jog','nap'] #The options available to player at start

    $ termNo = 1 #term number (it increases by incriments each time you finish a term and pass test)
    # flags for extra study times (effects layout of Timetable in weeklies.rpy/timetable)
    $ timeMan = False #gets extra study sessions (but beware of burnout)
    $ earlyBird = True

    jump looper

    return 



    # # # # # # # # # # #
    # adventures in Japan
    # # # # # # # # # # #
label looper:
    ## The time table is hard coded
    ## If events happen in a week, the week ends by jumping to looper

    while week_count < 52:
        
        call monday #handles flags, counts for week

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
            call timetable
            call studyCal
    
    # If there has been 52 weeks already, the game ends with you stuck in Japan?

    return