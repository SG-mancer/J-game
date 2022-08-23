
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
                    if sMfocus[x] == 0:
                        colorz = "{color=#000000}█{/color}"
                    elif sMfocus[x] == 1:
                        colorz = "{color=#0000ff}█{/color}"
                    elif sMfocus[x] == 2:
                        colorz = "{color=#00ff00}█{/color}"
                    elif sMfocus[x] == 3:
                        colorz = "{color=#ff0000}█{/color}"
                    elif sMfocus[x] == 4:
                        colorz = "{color=#00ffff}█{/color}"
                    elif sMfocus[x] == 5:
                        colorz = "{color=#ffff00}█{/color}"
                    elif sMfocus[x] == 6:
                        colorz = "{color=#ff00ff}█{/color}"
                    else:
                        colorz = "{color=#ffffff}█{/color}"
                    choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyA', x)
                ui.close()

            ui.hbox(xalign=0.1, yalign=0.2)
            ui.text("Morning          ")
            for x in studMeths:
                if sMfocus[x] == 0:
                    colorz = "{color=#000000}█{/color}"
                elif sMfocus[x] == 1:
                    colorz = "{color=#0000ff}█{/color}"
                elif sMfocus[x] == 2:
                    colorz = "{color=#00ff00}█{/color}"
                elif sMfocus[x] == 3:
                    colorz = "{color=#ff0000}█{/color}"
                elif sMfocus[x] == 4:
                    colorz = "{color=#00ffff}█{/color}"
                elif sMfocus[x] == 5:
                    colorz = "{color=#ffff00}█{/color}"
                elif sMfocus[x] == 6:                        
                    colorz = "{color=#ff00ff}█{/color}"
                else:
                    colorz = "{color=#ffffff}█{/color}"
                choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyB', x)
            ui.close()

            ui.hbox(xalign=0.1, yalign=0.3)
            ui.text("{b}{color=#ffa500}Afternoon Class{/color}{/b}")
            ui.close()

            ui.hbox(xalign=0.1, yalign=0.4)
            ui.text("Evening          ")
            for x in studMeths:
                if sMfocus[x] == 0:
                    colorz = "{color=#000000}█{/color}"
                elif sMfocus[x] == 1:
                    colorz = "{color=#0000ff}█{/color}"
                elif sMfocus[x] == 2:
                    colorz = "{color=#00ff00}█{/color}"
                elif sMfocus[x] == 3:                        
                    colorz = "{color=#ff0000}█{/color}"
                elif sMfocus[x] == 4:
                    colorz = "{color=#00ffff}█{/color}"
                elif sMfocus[x] == 5:
                    colorz = "{color=#ffff00}█{/color}"
                elif sMfocus[x] == 6:
                    colorz = "{color=#ff00ff}█{/color}"
                else:
                    colorz = "{color=#ffffff}█{/color}"
                choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyC', x)
            ui.close()
  
            if timeMan == True:
                ui.hbox(xalign=0.1, yalign=0.5)
                ui.text("Night            ")
                for x in studMeths:
                    if sMfocus[x] == 0:
                        colorz = "{color=#000000}█{/color}"
                    elif sMfocus[x] == 1:
                        colorz = "{color=#0000ff}█{/color}"
                    elif sMfocus[x] == 2:
                        colorz = "{color=#00ff00}█{/color}"
                    elif sMfocus[x] == 3:
                        colorz = "{color=#ff0000}█{/color}"
                    elif sMfocus[x] == 4:
                        colorz = "{color=#00ffff}█{/color}"
                    elif sMfocus[x] == 5:
                        colorz = "{color=#ffff00}█{/color}"
                    elif sMfocus[x] == 6:
                        colorz = "{color=#ff00ff}█{/color}"
                    else:
                        colorz = "{color=#ffffff}█{/color}"
                    choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyD', x)
                ui.close()

            ui.hbox(xalign=0.1, yalign=0.7)
            ui.text("{b}{color=#ff3300}WEEKEND          {/color}{/b}")
            for x in wkendMeths:
                if sMfocus[x] == 0:
                    colorz = "{color=#000000}█{/color}"
                elif sMfocus[x] == 1:
                    colorz = "{color=#0000ff}█{/color}"
                elif sMfocus[x] == 2:
                    colorz = "{color=#00ff00}█{/color}"
                elif sMfocus[x] == 3:
                    colorz = "{color=#ff0000}█{/color}"
                elif sMfocus[x] == 4:
                    colorz = "{color=#00ffff}█{/color}"
                elif sMfocus[x] == 5:
                    colorz = "{color=#ffff00}█{/color}"
                elif sMfocus[x] == 6:
                    colorz = "{color=#ff00ff}█{/color}"
                else:
                    colorz = "{color=#ffffff}█{/color}"
                choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyE', x)
            ui.close()

            # ui.textbutton ("STATS") action ToggleScreen('healthscreen')
            ui.textbutton ("Review Study Methods", clicked=Jump('pickMethods'), xalign=0.5, yalign=0.85)

            ui.textbutton('Done', clicked=ui.returns(False), xalign=0.5, yalign=0.9)
   
            repeat = ui.interact()
        study = [studyA, studyB, studyC, studyD, studyE]

    jump studyCal
    
    return

label costings:
    # Cost of train to class - if no teikiken rail pass
    if teikiken == False:
        $ calcY = daysClass * 2 * stnTcst[homeStn]
        "[calcY] for trains"
        $ spentY += calcY
        $ yenYen -= calcY
    
    # Cost of rent
    $ spentY += 12500
    $ yenYen -= 12500

    # Deduct the other costs of the week
    "[week_costs] costs for the week"
    $ yenYen -= week_costs
    $ spentY += week_costs

    # Add income from part time job

    # Check if about to become poor
    if yenYen < ((52-week_count)*25000):
        $ calcY = yenYen / (52-week_count)
        "Warning you have [yenYen] remaining.\nIt usually costs 25000 a week for rent and food.\n\nYou have [calcY] a week remaining!"


    # Go to start of week
    jump looper
    return