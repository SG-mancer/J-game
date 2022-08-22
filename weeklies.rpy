# ---------------
label monday:
    # sets the flags for the week. 
    $ week_count += 1
    $ classHW = False #set done homework to false 
    # check if bonus should be awarded
    if soci == phys == ment == max_stat:
        # give a stat bonus
        # $ stat_bonus += 1
        "bonus for max stats"

    # give an extra point in each stat (if not already max_stat)
    if soci < max_stat:
        $ soci += 1
    if phys < max_stat:
        $ phys += 1
    if ment < max_stat:
        $ ment += 1
    return

# ---------------
# Time Table (daily time table for the week of study/adventure)
label timetable:
    # Shows choices for activities for the weekdays.
    window hide
    scene bg planner
    show text "## Week [week_count] timetable ##" at top
    python:
        study = ['0','0','0','0','0'] # Zeros the choices, so they don't default to last weeks (what could get around O stat penalty)
        studyA = '0' #it was easier to just handle these strings for the options...
        studyB = '0'
        studyC = '0'
        studyD = '0'
        studyE = '0'
        colorz = "{color=#6699ff}█{/color}" #colour of the box before each option
        
        repeat = True
        if len(studMeths) > 10:
            if len(studMeths) > 15:
                Siz=12
            else:
                Siz = 15
        else: 
            Siz = 20
        while repeat:
            if earlyBird == True:
                ui.hbox(xalign=0.1, yalign=0.1)
                ui.text("Early Morning    ")
                for x in studMeths:
                    choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyE', x)
                ui.close()

            ui.hbox(xalign=0.1, yalign=0.2)
            ui.text("Morning          ")
            for x in studMeths:
                choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyD', x)
            ui.close()

            if timeMan == True:
                ui.hbox(xalign=0.1, yalign =0.3)
                ui.text("Forenoon        ")                
                for x in studMeths:
                    choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyA', x)
                ui.close()

            ui.hbox(xalign=0.1, yalign=0.4)
            ui.text("Afternoon Class")
            ui.close()

            ui.hbox(xalign=0.1, yalign=0.5)
            ui.text("Evening          ")
            for x in studMeths:
                choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyB', x)
            ui.close()
  
            if timeMan == True:
                ui.hbox(xalign=0.1, yalign=0.6)
                ui.text("Night            ")
                for x in studMeths:
                    choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyC', x)
                ui.close()

            if timeMan == True and earlyBird == False:  #Study E is for non-early bird players
                ui.hbox(xalign=0.1, yalign=0.7)
                ui.text("Late Night       ")
                for x in studMeths:
                    choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyE', x)
                ui.close()

            ui.textbutton('Done', clicked=ui.returns(False), xalign=0.5, yalign=0.8)
   
            repeat = ui.interact()
        study = [studyA, studyB, studyC, studyD, studyE]

    return
