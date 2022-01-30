
# declared characters:
define z = Character("Dylan", color="#33ccff") ## The player character - Dylan A Thomas (DAT)

define t = Character("Sensei Teacher")

define a = Character("Andrew", color="#ffcc33") ## friend of the player


#background images
image bg japanflight = "ausflight.png"
image bg tokyonight = "ausflight.png"

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
            text "Receptive Skills:"
            bar value AnimatedValue(value=(Ability[2]+Ability[3]), range=100, delay=2.0)
            text "Productive Skills:"
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

    $ studMeths = ['jog','nap','rev_notes','browse_web','homework'] #The options available to player at start

    $ termNo = 1 #term number (it increases by incriments each time you finish a term and pass test)
    # flags for extra study times (effects layout of Timetable in weeklies.rpy/timetable)
    $ timeMan = False #gets extra study sessions (but beware of burnout)
    $ earlyBird = True


    # # # # # # # # # # #
    # adventures in Japan
    # # # # # # # # # # #

    ## need to use less call and more jump (if no need to loop back)

    call beginning #the story begins

    call tutorial #a tutorial for a new player

    while week_count < 101:
        
        call monday #handles flags, counts for week
        call timetable
        call studyCal
        
    return