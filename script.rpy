
# declared characters:
define z = Character("Jack")
define o = Character("Oslo")
define t = Character("Sensei Teacher")
define x = Character("narrator")

#background images
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
            text u"{color=#6699ff}Mental: [ment]{/color}"
            bar value AnimatedValue(value=ment, range=max_stat, delay=2.0)

            text u"{color=#33cc33}Social: [soci]{/color}"
            bar value AnimatedValue(value=soci, range=max_stat, delay=2.0)

            text u"{color=#ff3300}Physical: [phys]{/color}"
            bar value AnimatedValue(value=phys, range=max_stat, delay=2.0)

            # Note: we only show totals for Talent, Skill and Knoweldge
            if ((Talen[0]+Talen[1]+Talen[2]+Talen[3])/100 < 1) and ((Skill[0]+Skill[1]+Skill[2]+Skill[3])/100 < 1) and ((Knowl[0]+Knowl[1]+Knowl[2]+Knowl[3])/100 < 1):
                text "Talent:"
                bar value AnimatedValue(value=(Talen[0]+Talen[1]+Talen[2]+Talen[3]), range=100, delay=2.0)
                text "Skill:"
                bar value AnimatedValue(value=(Skill[0]+Skill[1]+Skill[2]+Skill[3]), range=100, delay=2.0)
                text "Kowledge:"
                bar value AnimatedValue(value=(Knowl[0]+Knowl[1]+Knowl[2]+Knowl[3]), range=100, delay=2.0)
            else:
                text "Talent:"
                bar value AnimatedValue(value=(Talen[0]+Talen[1]+Talen[2]+Talen[3]), range=200, delay=2.0)
                text "Skill:"
                bar value AnimatedValue(value=(Skill[0]+Skill[1]+Skill[2]+Skill[3]), range=300, delay=2.0)
                text "Kowledge:"
                bar value AnimatedValue(value=(Knowl[0]+Knowl[1]+Knowl[2]+Knowl[3]), range=500, delay=2.0)                
            text u"Cash:  \n¥[yenYen]"
            

        
# ---------------
# the story starts here...
label start:
    # # # # # # # # # # #
    # set up variables
    # # # # # # # # # # #
    $ ment = 2 
    $ soci = 2
    $ phys = 2
    $ max_stat = 5
    $ Talen = [0,0,0,0] #Academics, Athletics, Art, Science
    $ Skill = [0,0,0,0] #Reading, Listening, Pronounciation, Sport
    $ Knowl = [0,0,0,0] #Vocab, Grammar, Kanji, General
    $ yenYen = 3375000 #this is before redundancy 6672330 after?
    
    $ stat_bonus = 0 #number of weeks you started with max_stats in ment, soci and phys... reward_???

    $ week_count = 0 #number of weeks played
    $ burnCount = 0 #number of burnouts
    $ burnoutWarn = 0 #number of burnout warnings
    $ school = 0 #the school selected

    call init_study #initialises many study variables
    
    # flags for extra study times
    $ timeMan = False #gets extra study sessions (but beware of burnout)
    $ earlyBird = True

    # flags for weekend events
    $ burnout = False #burnout happens when you go into negative for ment. (you can not study too hard)
    $ classHW = False #have you done homework this week
    $ Marathon = False #enter Tokyo Marrathon
    $ MarathonPrac = 0 #marathon practice
    

    # # # # # # # # # # #
    # adventures in Japan
    # # # # # # # # # # #

    call beginning #the story begins
    call tutorial #a tutorial for a new player

    while week_count < 101:
        
        call monday #handles flags, counts for week
        call ambient #background music for season
        call story #story events...

        if week_count in [5,13,14,20,26,27,38,39,50,51,52,57,64,65,71,77,78,89,90,102]:
            # holidays has no timetable, class
            call holidays
            call weekend
        else:
            # classes
            call timetable
            call studyCal
            call weekend

    return




            

