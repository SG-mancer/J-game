
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
        xmaximum 350
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
    $ yenYen = 1000000 # cash remaining
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
    $ teikiken = False #A rail pass for getting to and from school
    $ homeStn = 1 # Home station (0 = Shiomi, 1 = Hamacho, 2 = Chofu, 3 = Takadanobaba)
    $ stnTcst = [310, 220, 250, 140] # cost of ticket
    $ teiTcst = [44260, 50440, 48550, 18980] # cost of 6 month teikiken
    $ daysClass = 5

    # Options for the weekly study planner
    $ studMeths = ['jog','nap'] #starting options for studying before/after class
    $ wkendMeths = ['shopping','computerGames'] #The options available to player at the weekend starting

    # Count how often each choice is made
    $ sMCounts = {'nap':0, 'clubbing':0, 'freeBoard':0, 'jog':0, 'library':0, 'gradedReader':0, 'computerGames':0, 'datingApp':0, 'shopping':0, 'SRS_convo':0, 'SRS_kanjiK':0, 'SRS_kanjiX':0, 'SRS_vocab':0, 'workbook':0, 'JLPT_drill':0, 'text-book':0, 'shadowing':0, 'langCircle':0, 'manga':0, 'bikeTouring':0, 'tutor':0, '0':0}
    # focus colour for each choice 0- none/black, 1- soci/blue, 2- phys/green, 3- ment/red, 4- soci+phys/cyan, 5- phys+ment/yellow, 6- soci+ment/magenta, 7- soci+phys+ment/white
    $ sMfocus = {'nap':0, 'clubbing':4, 'freeBoard':1, 'jog':2, 'library':6, 'gradedReader':3, 'computerGames':0, 'datingApp':1, 'shopping':4, 'SRS_convo':3, 'SRS_kanjiK':3, 'SRS_kanjiX':3, 'SRS_vocab':3, 'workbook':3, 'JLPT_drill':3, 'text-book':3, 'shadowing':6, 'langCircle':1, 'manga':3, 'bikeTouring':4, 'tutor':1, '0':0}
    # study method flavour text
    $ sMflav = {'nap':'Take a nap to recharge your batteries.', 
    'clubbing':'Head out to Roppongi.',
    'freeBoard':'Meet up with travellers couchsurf, and find cheap/free rooms and board around the world.',
    'library': 'Visit your local library, to sit and study or read books at your level.',
    'jog':'A 40min jog to lower your stress levels, and invigorate your to study harder.',
    'gradedReader':'Read a short story or article to improve your vocab and reading ability.', 
    'computerGames':'Stay at home, play some games and daydream.', 
    'datingApp':'Match a very popular dating app that lets you swipe to link with women, use it to practice conversation or try arrange a date.', 
    'shopping':'Walk around the shopping district, maybe practice Japanese with staff, or invest in a new hobby.', 
    'SRS_convo':'Spaced Repetiton System, conversation phrases and words to practice day to day conversations.', 
    'SRS_kanjiK':'Spaced Repetiton System, learn the school (Kyōiku) Kanji in the same order as Japanese children.',
    'SRS_kanjiX':'Spaced Repetiton System, Learn a keyword for every Kanji based on a list from a book called Never Forget Kanji by Sensei H.',
    'SRS_vocab':'Spaced Repetiton System, vocabularly builder focusing on topics like locations, body parts etc.', 
    'workbook':'Do more exercises from this extra workbook.', 
    'JLPT_drill':'Practice JLPT questions with a drill book.',
    'text-book':'Read the next chapter or two and do exercises from your textbook.',
    'shadowing':'Like Karaoke but for books. Read along with audio to improve your reading, listening and speaking skills.',
    'langCircle':'A weekend class arranged by the Language Teaching department of Waseda.',
    'manga':'Read manga to try improve your vocab and language skills.',
    'bikeTouring':'Ride around Tokyo and out of town to visit new places and meet people.',
    'tutor':'Private 1 on 1 japanese lessons - either online or at a cafe. Where you get to choose what to focus on.',
    '0':''}
    $ statOP = 1 # count of how many times a stat is greater than the maximum (i.e. already max Ment but nap)

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
        $ week_costs = renpy.random.choice([5000, 10000, 2000]) # random cost for sundries during the week
        $ sensenAbil = senshuAbil # week before lasts Ability modifier
        $ senshuAbil = konshuAbil # last weeks Ability modifier

        "[week_costs]"
        call costings

        if week_count == 1:
            jump beginning
        elif week_count == 25:
            "Half year ceremony"
            jump getTeikiken
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
            $ daysClass = 5
            if week_count in [17,29,32,42,46]:
                #flavour text for long weekened
                "Long weekend"
                $ daysClass = 4
            jump timetable #Then it jumps to studyCal before jumping back to looper here
    
    # If there has been 52 weeks already, the game ends with you stuck in Japan?

    return