# ---------------
label monday:
    # sets the flags for the week. 
    $ week_count += 1
    $ classHW = False #set done homework to false 
    # check if bonus should be awarded
    if ment == soci == phys == max_stat:
        $ stat_bonus += 1
        $ y = 0
        while y < 4: #Give a bonus point in each language skill
            $ Skill[y] += 1
            $ Talen[y] += 1
            $ Knowl[y] += 1
            $ y += 1
    # give an extra point in each stat (if not already max_stat)
    if ment < max_stat:
        $ ment += 1
    if soci < max_stat:
        $ soci += 1
    if phys < max_stat:
        $ phys += 1
    return

# ---------------
# Time Table (daily time table for the week of study/adventure)
label timetable:
    # Shows choices for activities for the weekdays.
    window hide
    scene bg tokyonight
    show text "## Week [week_count] timetable ##" at top
    python:
        if ment < 1 or phys < 1 or soci < 1:
            study = ['0','0','0','0','0'] # Zeros the choices, so they don't default to last weeks (what could get around O stat penalty)
            studyA = '0' #it was easier to just handle these strings for the options...
            studyB = '0'
            studyC = '0'
            studyD = '0'
            studyE = '0'
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
                        colorz = "{color=#6699ff}█{/color}"
                    elif sMfocus[x] == 1:
                        colorz = "{color=#33cc33}█{/color}"
                    elif sMfocus[x] == 2:
                        colorz = "{color=#ff3300}█{/color}"
                    else:
                        colorz = "{color=#e6e6e6}█{/color}"
                    if sMfocus[x] == 0 and ment > 0 or sMfocus[x] == 1 and soci > 0 or sMfocus[x] == 2 and phys > 0 or sMfocus[x] == 3:
                        choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyE', x)
                ui.close()

            ui.hbox(xalign=0.1, yalign=0.2)
            ui.text("Morning          ")
            for x in studMeths:
                if sMfocus[x] == 0:
                    colorz = "{color=#6699ff}█{/color}"
                elif sMfocus[x] == 1:
                    colorz = "{color=#33cc33}█{/color}"
                elif sMfocus[x] == 2:
                    colorz = "{color=#ff3300}█{/color}"
                else:
                    colorz = "{color=#e6e6e6}█{/color}"
                if sMfocus[x] == 0 and ment > 0 or sMfocus[x] == 1 and soci > 0 or sMfocus[x] == 2 and phys > 0 or sMfocus[x] == 3:
                    choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyD', x)
            ui.close()

            if timeMan == True:
                ui.hbox(xalign=0.1, yalign =0.3)
                ui.text("Forenoon        ")                
                for x in studMeths:
                    if sMfocus[x] == 0:
                        colorz = "{color=#6699ff}█{/color}"
                    elif sMfocus[x] == 1:
                        colorz = "{color=#33cc33}█{/color}"
                    elif sMfocus[x] == 2:
                        colorz = "{color=#ff3300}█{/color}"
                    else:
                        colorz = "{color=#e6e6e6}█{/color}"
                    if sMfocus[x] == 0 and ment > 0 or sMfocus[x] == 1 and soci > 0 or sMfocus[x] == 2 and phys > 0 or sMfocus[x] == 3:
                        choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyA', x)
                ui.close()

            ui.hbox(xalign=0.1, yalign=0.4)
            ui.text("Afternoon Class")
            ui.close()

            ui.hbox(xalign=0.1, yalign=0.5)
            ui.text("Evening          ")
            for x in studMeths:
                if sMfocus[x] == 0:
                    colorz = "{color=#6699ff}█{/color}"
                elif sMfocus[x] == 1:
                    colorz = "{color=#33cc33}█{/color}"
                elif sMfocus[x] == 2:
                    colorz = "{color=#ff3300}█{/color}"
                else:
                    colorz = "{color=#e6e6e6}█{/color}"
                if sMfocus[x] == 0 and ment > 0 or sMfocus[x] == 1 and soci > 0 or sMfocus[x] == 2 and phys > 0 or sMfocus[x] == 3:
                    choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyB', x)
            ui.close()
  
            if timeMan == True:
                ui.hbox(xalign=0.1, yalign=0.6)
                ui.text("Night            ")
                for x in studMeths:
                    if sMfocus[x] == 0:
                        colorz = "{color=#6699ff}█{/color}"
                    elif sMfocus[x] == 1:
                        colorz = "{color=#33cc33}█{/color}"
                    elif sMfocus[x] == 2:
                        colorz = "{color=#ff3300}█{/color}"
                    else:
                        colorz = "{color=#e6e6e6}█{/color}"
                    if sMfocus[x] == 0 and ment > 0 or sMfocus[x] == 1 and soci > 0 or sMfocus[x] == 2 and phys > 0 or sMfocus[x] == 3:
                        choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyC', x)
                ui.close()

            if timeMan == True and earlyBird == False:  #Study E is for non-early bird players
                ui.hbox(xalign=0.1, yalign=0.7)
                ui.text("Late Night       ")
                for x in studMeths:
                    if sMfocus[x] == 0:
                        colorz = "{color=#6699ff}█{/color}"
                    elif sMfocus[x] == 1:
                        colorz = "{color=#33cc33}█{/color}"
                    elif sMfocus[x] == 2:
                        colorz = "{color=#ff3300}█{/color}"
                    else:
                        colorz = "{color=#e6e6e6}█{/color}"
                    if sMfocus[x] == 0 and ment > 0 or sMfocus[x] == 1 and soci > 0 or sMfocus[x] == 2 and phys > 0 or sMfocus[x] == 3:
                        choicebutton('{size=[Siz]}[colorz] '+x+'{/size} ', 'studyE', x)
                ui.close()

            ui.textbutton('Done', clicked=ui.returns(False), xalign=0.5, yalign=0.8)
   
            repeat = ui.interact()
        study = [studyA, studyB, studyC, studyD, studyE]

    return


# ---------------
label weekend:
    #check if burnout, if the player is burnt out. They miss the weekend, recover 2. If they are less than 0 still it will effect next week's choices

    # CHECK FOR BURNOUT and handle
    if week_count+5 in jlptWeeks: #enter JLPT 5 weeks before the exam
        call JLPTEntry
    if week_count-4 in jlptWeeks: #recieve JLPT Results 4 weeks after exam 
        call JLPTResult 

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
    else: #handle classHW bonus and termExams.
        call HomeWorkCheck
        call Learning
        
        if week_count in testWeeks:
            z "exam"
            call TermExam
        if week_count in jlptWeeks:
            call JLPTExam
        call WeekEndEvent
        return
return

# Get the class Homework bonus (it is dependent on Knowl increasing with terms ie. 2x Knowl (if termNo = 5), 1.25x Knowl (if termNo = 2)) 
label HomeWorkCheck:
    if classHW == True:
        if (Skill[0]+Skill[1]+Skill[2])*(((termNo-1)/4)+1) > (Knowl[0]+Knowl[1]+Knowl[2]):
            if Knowl[2] > (Knowl[0]+ Knowl[1]): 
                $ Knowl[0] += 1 #grammar and vocab
                $ Knowl[1] += 1
            else:
                $ Knowl[2] += 1 #kanji
        else: #Pronounciation + reading/listening
            $ Skill[2] += 1
            if Skill[1] > Skill[0]:
                $ Skill[0] += 1
            else:
                $ Skill[1] += 1
    return

# ---------------
# The information you learn by turning up to class
label Learning:
    if school == 0: #Shinjuku
        $ Skill[0] += 1
        $ Knowl[1] += 1
        $ Knowl[2] += 1 
        
    elif school == 1: #Takadanobaba
        $ Skill[0] += 1
        if Skill[2] < 100:
                $ Skill[2] += 1
        else:
            if week_count % 2 == 0:
                $ Talen[0] += 1
            else:
                $ Knowl[2] += 1
        if week_count % 2 == 0:
            $ Knowl[1] += 1
        else:
            $ Skill[1] += 1
    else: #Osaki
        if Skill[2] < 100:
            $ Skill[2] += 1
        else:
            if week_count% 2 == 0:
                $ Skill[0] += 1
            else:
                $ Talen[0] += 1
        if termNo < 3:
            $ Knowl[0] += 1
        else:
            $ Knowl[2] += 1
        if week_count% 3 == 0:
            $ Skill[0] += 1
        $ Knowl[1] += 1

    return

