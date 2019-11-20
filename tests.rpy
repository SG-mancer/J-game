# This file is for testing the game core loop
label test1:

    $ week_count = 0
    $ choiceA = 0
    $ choiceB = 0
    $ choiceC = 0
    $ choiceD = 0
    $ burnoutWarn = 0
    $ Talen[1] = 6

    while week_count < 100:
        $ week_count += 1
        
        call monday

        #['jog','nap','rev_notes','rev_class','browse_web','flash_cards','homework']
        if ment > 0 and phys > 0:
            $ studyA = u'homework'
            if week_count% 2 == 0:
                $ studyB = u'rev_class'
                $ studyC = u'rev_notes'
            else:
                $ studyB = u'rev_notes'
                $ studyC = u'rev_class'
            $ studyC = u'jog'
            $ choiceA += 1
        elif ment > 0 and phys < 1:
            $ studyA = u'homework'
            if week_count% 2 == 0:
                $ studyB = u'rev_class'
                $ studyC = u'rev_notes'
            else:
                $ studyB = u'rev_notes'
                $ studyC = u'rev_class'
            if ment < 2:
                $ studyC = u'nap'
            $ choiceB += 1
        elif soci > 0: 
            $ studyA = u'browse_web'
            $ studyB = u'nap'
            $ studyC = u'nap'
            $ choiceC += 1
        else:
            $ studyA = u'nap'
            $ studyB = u'nap'
            $ studyC = u'nap' 
            $ choiceD += 1
        
        $ study = [studyA, studyB,u'0',u'0',studyC] #instead of timetable set our choices
        
        call studyCal
        
        if week_count in [13,35,65,87]:
            z "week [week_count].\n[Talen],[Skill],[Knowl]. \nBurnout:[burnCount]. Warning:[burnoutWarn]\n[choiceA]--[choiceB]--[choiceC]--[choiceD]"
        
        call weekend
    
    z "week [week_count].\n[Talen],[Skill],[Knowl]. [burnCount]\n[choiceA]--[choiceB]"
    return