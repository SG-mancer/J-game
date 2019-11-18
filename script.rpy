
# declared characters:
define z = Character("Jack")
define o = Character("Oslo")

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

default ment = 2
default soci = 2
default phys = 2
default max_stat = 5
default stat_bonus = 0

# STATUS POPUP
screen healthscreen():
    frame:
        align (0.95, 0.05)
        xmaximum 250
        vbox:
            text "Week [week_count]"
            text "Mental: [ment]"
            bar value AnimatedValue(value=ment, range=max_stat, delay=2.0)

            text "Social: [soci]"
            bar value AnimatedValue(value=soci, range=max_stat, delay=2.0)

            text "Physical: [phys]"
            bar value AnimatedValue(value=phys, range=max_stat, delay=2.0)

            # Note: we only show totals for Talent, Skill and Knoweldge
            text "Talent:"
            bar value AnimatedValue(value=(Talen[0]+Talen[1]+Talen[2]+Talen[3]), range=100, delay=2.0)
            text "Skill:"
            bar value AnimatedValue(value=(Skill[0]+Skill[1]+Skill[2]+Skill[3]), range=100, delay=2.0)
            text "Kowledge:"
            bar value AnimatedValue(value=(Knowl[0]+Knowl[1]+Knowl[2]+Knowl[3]), range=100, delay=2.0)
            text u"Cash:  \n¥[yenYen]"
            

        
# ---------------
# the story starts here...
label start:
    # set up variables
    $ ment = 2 
    $ soci = 2
    $ phys = 2
    $ Talen = [0,0,0,0] #Academics, Athletics, Art, Science
    $ Skill = [0,0,0,0] #Reading, Listening, Pronounciation, Sport
    $ Knowl = [0,0,0,0] #Vocab, Grammar, Kanji, General
    $ stat_bonus = 0 #number of weeks you started with max_stats in ment, soci and phys
    $ week_count = 0 #number of weeks played
    $ burnCount = 0 #number of burnouts
    $ yenYen = 3375000 #this is before redundancy
    $ school = 0

    call init_study
    
    # studying
    $ study = [0,0,0,0,0] # This is populated for cycling through the study options
    $ studyA = '0' # These were just easier than study options above
    $ studyB = '0'
    $ studyC = '0'
    $ studyD = '0'
    $ studyE = '0'
    # flags for extra study times
    $ timeMan = False #gets extra study sessions (but beware of burnout)
    $ earlyBird = True
    $ burnout = False #burnout happens when you go into negative for ment. (you can not study too hard)
    

    call beginning

    # adventure in Japan 
    call timetable
    call studyCal
    call weekend

    $ week_count += 1
    call monday
    z "that is great"
    # adventure in Japan 
    call timetable
    call studyCal
    call weekend

    $ week_count += 1
    call monday
    z "week 2 over"

return



# ---------------
# Time Table (daily time table for the week of study/adventure)
label timetable:
    z "you are here in timetable ok"
    window hide
    python:
        study = [0,0,0,0,0] # Zeros the choices, so they don't default to last weeks (what could get around O stat penalty)
        repeat = True
        while repeat:
            if earlyBird == True:
                ui.hbox(xalign=0.1, yalign=0.1)
                ui.text("Early Morning    ")
                for x in studMeths:
                    if sMfocus[x] == 0 and ment > 0 or sMfocus[x] == 1 and soci > 0 or sMfocus[x] == 2 and phys > 0 or sMfocus[x] == 3:
                        choicebutton(x+'   ', 'studyE', x)
                ui.close()

            if timeMan == True:
                ui.hbox(xalign=0.1, yalign=0.2)
                ui.text("Morning         ")
                for x in studMeths:
                    if sMfocus[x] == 0 and ment > 0 or sMfocus[x] == 1 and soci > 0 or sMfocus[x] == 2 and phys > 0 or sMfocus[x] == 3:
                        choicebutton(x+'   ', 'studyD', x)
                ui.close()

            ui.hbox(xalign=0.1, yalign =0.3)
            ui.text("Morning          ")                
            for x in studMeths:
                if sMfocus[x] == 0 and ment > 0 or sMfocus[x] == 1 and soci > 0 or sMfocus[x] == 2 and phys > 0 or sMfocus[x] == 3:
                        choicebutton(x+'   ', 'studyA', x)
            ui.close()

            ui.hbox(xalign=0.1, yalign=0.4)
            ui.text("Afternoon Class")
            ui.close()

            ui.hbox(xalign=0.1, yalign=0.5)
            ui.text("Evening          ")
            for x in studMeths:
                if sMfocus[x] == 0 and ment > 0 or sMfocus[x] == 1 and soci > 0 or sMfocus[x] == 2 and phys > 0 or sMfocus[x] == 3:
                        choicebutton(x+'   ', 'studyB', x)
            ui.close()
  
            if timeMan == True:
                ui.hbox(xalign=0.1, yalign=0.6)
                ui.text("Night            ")
                for x in studMeths:
                    if sMfocus[x] == 0 and ment > 0 or sMfocus[x] == 1 and soci > 0 or sMfocus[x] == 2 and phys > 0 or sMfocus[x] == 3:
                        choicebutton(x+'   ', 'studyC', x)
                ui.close()

            if timeMan == True and earlyBird == False:  #Study E is for non-early bird players
                ui.hbox(xalign=0.1, yalign=0.7)
                ui.text("Late Night       ")
                for x in studMeths:
                    if sMfocus[x] == 0 and ment > 0 or sMfocus[x] == 1 and soci > 0 or sMfocus[x] == 2 and phys > 0 or sMfocus[x] == 3:
                        choicebutton(x+'   ', 'studyE', x)
                ui.close()

            ui.textbutton('Done', clicked=ui.returns(False), xalign=0.5, yalign=0.8)
   
            repeat = ui.interact()
        study = [studyA, studyB, studyC, studyD, studyE]

    return

# ---------------
label weekend:
    #check if burnout, if the player is burnt out. They miss the weekend, recover 2. If they are less than 0 still it will effect next week's choices
    if burnout == True:
        $ burnCount += 1
        $ ment += 2
        if ment < 0: #super burnout, get etra burnCount and penalty
            $ ment = -1 # this will increase to 0 on Monday, and effect their ment choices next week
        $ burnout = False
        #
        # TODO: flavour text for recovering from burnout over the weekend
        #
        return
    else: #handle the weekend BONUS event
        #
        # TODO: weekend events (JLPT will live here too)
        #
        return
return

# ---------------
label monday:
    # check if bonus should be awarded
    if ment == soci == phys == max_stat:
        $ stat_bonus += 1
    # give an extra point in each stat (if not already max_stat)
    if ment < max_stat:
        $ ment += 1
    if soci < max_stat:
        $ soci += 1
    if phys < max_stat:
        $ phys += 1
return
            

