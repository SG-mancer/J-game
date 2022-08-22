
# ---------------
# Time Table (daily time table for the week of study/adventure)
label timetable:
    # Shows choices for activities for the weekdays.
    window hide
    scene bg planner
    show text "## Week [week_count] timetable ##" at top
    python:
        senshuStudy = study #copy what was studied last week (for checking a bonus)
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
                    choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyA', x)
                ui.close()

            ui.hbox(xalign=0.1, yalign=0.2)
            ui.text("Morning          ")
            for x in studMeths:
                choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyB', x)
            ui.close()

            ui.hbox(xalign=0.1, yalign=0.3)
            ui.text("Afternoon Class")
            ui.close()

            ui.hbox(xalign=0.1, yalign=0.4)
            ui.text("Evening          ")
            for x in studMeths:
                choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyC', x)
            ui.close()
  
            if timeMan == True:
                ui.hbox(xalign=0.1, yalign=0.5)
                ui.text("Night            ")
                for x in studMeths:
                    choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyD', x)
                ui.close()

            ui.hbox(xalign=0.1, yalign=0.7)
            ui.text("{b}{color=#ff3300}WEEKEND          {/b}{/color}")
            for x in wkendMeths:
                choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyE', x)
            ui.close()

            # ui.textbutton ("STATS") action ToggleScreen('healthscreen')
            ui.textbutton ("Review Study Methods", clicked=Jump('pickMethods'), xalign=0.5, yalign=0.85)

            ui.textbutton('Done', clicked=ui.returns(False), xalign=0.5, yalign=0.9)
   
            repeat = ui.interact()
        study = [studyA, studyB, studyC, studyD, studyE]

    jump studyCal
    
    return
