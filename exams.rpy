# Test that the player has achieved the required skills to pass to next term (end of term Exams)
# It also generates a report for the player, so they know how their skills are going
label TermExam:
    $ grade = Txams[school][termNo]
    $ failCount = 0 # counts units failed - if fail 2 you do not go to next level
    $ Aca = ''
    $ Rea = ''
    $ Lis = ''
    $ Prn = ''
    $ Vcb = ''
    $ Gmr = ''
    $ Knj = ''
    
    # CHECK each of the Stats and assign S,A,B,C,D,E or F (and click up failCount)
    if Talen[0] > grade[0]:
        $ Aca = 'S'
    elif Talen[0] > grade[0]*0.9:
        $ Aca = 'A'
    elif Talen[0] > grade[0]*0.8:
        $ Aca = 'B'
    elif Talen[0] > grade[0]*0.7:
        $ Aca = 'C'
    elif Talen[0] > grade[0]*0.6:
        $ Aca = 'D'
    elif Talen[0] > grade[0]*0.5:
        $ Aca = 'E'
    else:
        $ Aca = 'F'
        $ failCount += 1
    
    if Skill[0] > grade[1]:
        $ Rea = 'S'
    elif Skill[0] > grade[1]*0.9:
        $ Rea = 'A'
    elif Skill[0] > grade[1]*0.8:
        $ Rea = 'B'
    elif Skill[0] > grade[1]*0.7:
        $ Rea = 'C'
    elif Skill[0] > grade[1]*0.6:
        $ Rea = 'D'
    elif Skill[0] > grade[1]*0.5:
        $ Rea = 'E'
    else:
        $ Rea = 'F'
        $ failCount += 1

    if Skill[1] > grade[2]:
        $ Lis = 'S'
    elif Skill[1] > grade[2]*0.9:
        $ Lis = 'A'
    elif Skill[1] > grade[2]*0.8:
        $ Lis = 'B'
    elif Skill[1] > grade[2]*0.7:
        $ Lis = 'C'
    elif Skill[1] > grade[2]*0.6:
        $ Lis = 'D'
    elif Skill[1] > grade[2]*0.5:
        $ Lis = 'E'
    else:
        $ Lis = 'F'
        $ failCount += 1

    if Skill[2] > grade[3]:
        $ Prn = 'S'
    elif Skill[2] > grade[3]*0.9:
        $ Prn = 'A'
    elif Skill[2] > grade[3]*0.8:
        $ Prn = '2'
    elif Skill[2] > grade[3]*0.7:
        $ Prn = 'C'
    elif Skill[2] > grade[3]*0.6:
        $ Prn = 'D'
    elif Skill[2] > grade[3]*0.5:
        $ Prn = 'E'
    else:
        $ Prn = 'F'
        $ failCount += 1

    if Knowl[0] > grade[4]:
        $ Vcb = 'S'
    elif Knowl[0] > grade[4]*0.9:
        $ Vcb = 'A'
    elif Knowl[0] > grade[4]*0.8:
        $ Vcb = '2'
    elif Knowl[0] > grade[4]*0.7:
        $ Vcb = 'C'
    elif Knowl[0] > grade[4]*0.6:
        $ Vcb = 'D'
    elif Knowl[0] > grade[4]*0.5:
        $ Vcb = 'E'
    else:
        $ Vcb = 'F'
        $ failCount += 1
    
    if Knowl[1] > grade[5]:
        $ Gmr = 'S'
    elif Knowl[1] > grade[5]*0.9:
        $ Gmr = 'A'
    elif Knowl[1] > grade[5]*0.8:
        $ Gmr = '2'
    elif Knowl[1] > grade[5]*0.7:
        $ Gmr = 'C'
    elif Knowl[1] > grade[5]*0.6:
        $ Gmr = 'D'
    elif Knowl[1] > grade[5]*0.5:
        $ Gmr = 'E'
    else:
        $ Gmr = 'F'
        $ failCount += 1
    
    if Knowl[2] > grade[6]:
        $ Knj = 'S'
    elif Knowl[2] > grade[6]*0.9:
        $ Knj = 'A'
    elif Knowl[2] > grade[6]*0.8:
        $ Knj = '2'
    elif Knowl[2] > grade[6]*0.7:
        $ Knj = 'C'
    elif Knowl[2] > grade[6]*0.6:
        $ Knj = 'D'
    elif Knowl[2] > grade[6]*0.5:
        $ Knj = 'E'
    else:
        $ Knj = 'F'
        $ failCount += 1

    call TermReport

    # CHECK IF PLAYER PASSED TERM (if they failed less than 2 stats they go ahead.)
    if failCount < 2:
        $ termNo += 1
        t "Omeditougozaimasu! Next term you will go up to class [termNo]!"
    else:
        if failCount > 4:
            t "Maybe you need to focus more."
            # Give an option to give up !
        else:
            t "Sumimasen... you did not pass. Next term you will do class [termNo] again."

    return

# Report the results from Term to the player.
# Note: It can be called again until the TermExam is run again !
label TermReport:
    t "Your term exam results:\nReading:[Rea], Listening:[Lis], Pronounciation:[Prn],\nVocabulary:[Vcb], Grammar:[Gmr], Kanji:[Knj],\n and Academics:[Aca]"
    return

# ---------------
# JLPT Entry - select your JLPT level to conduct test at
label JLPTEntry:
    menu:
        "Which level of JLPT do you wish to attempt?"
        "JLPT 5":
            $Jlvl = 'JLPT 5'
        "JLPT 4":
            $Jlvl = 'JLPT 4'
        "JLPT 3":
            $Jlvl = 'JLPT 3'
        "JLPT 2":
            $Jlvl = 'JLPT 2'
        "JLPT 1":
            $Jlvl = 'JLPT 1'
        
    $ JResu = ['C','C','C','DNF'] #Vocab, Grammar, Reading - DNF is used, if you burnout and can not do the test!
    return

label JLPTResult:
    # Report the JLPT.
    t "Your JLPT Results are back:\n Vocab: [JRseu[0]], Grammar: [JRseu[1]], Reading: [JRseu[2]]. --[JRseu[3]]"

    if JResu[3] == 'Pass':
        #JLPT Pass reward
        $ JResu[3] == 'pass!' #so it will not trigger the reward if you check your results again...   
    return
    

# ---------------
# The JLPT. When you conduct it, you will get a result determined. But only vaguely know if you passed... (results in 4 weeks)
label JLPTExam:
    $ ExamReq = {'JLPT 5':[10,10,9,15,6,8],'JLPT 4':[15,40,9,20,9,25],'JLPT 3':[30,50,12,25,12,62],'JLPT 2':[60,90,21,40,27,100],'JLPT 1':[90,140,35,80,51]}
    $ Examinee = [Talen[0],Skill[0],Skill[1],Knowl[0],Knowl[1],Knowl[2]]
    $ JExam = ExamReq[Jlvl]
    

    if JExam[0] < Examinee[0] and JExam[5] < Examinee[5]: #Academics, Kanji
        # check Acadmeics and Kanji
        if (JExam[1]+JExam[2]) < (Examinee[1]+Examinee[2]):
            # check Reading/Listening
            if (JExam[3]+JExam[4]) < (Examinee[3]+Examinee[4]):
                # check Vocab/Grammar 
                $ JResu = ['A','A','A','Pass'] #Vocab, Grammar Reading all good
            elif JExam[4] < Examinee[4]: 
                $ JResu = ['C','A','A','Pass'] #Vocab Bad
            elif JExam[3] < Examinee[3]: 
                $ JResu = ['A','C','A','Pass'] #Grammar Bad
            else:
                $ JResu = ['C','C','A','Fail'] #Grammar & Vocab Bad 
        else:
            if JExam[1] < Examinee[1]: #is reading good?
                if (JExam[3]+JExam[4]) < (Examinee[3]+Examinee[4]):
                    $ JResu = ['B','A','B','Pass'] #Listening bad...
                else:
                    if JExam[4] < Examinee[4]: 
                        $ JResu = ['C','B','B','Pass'] #Vocab, Listening bad
                    elif JExam[3] < Examinee[3]:
                        $ JResu = ['B','C','B','Pass'] #Grammar, Listening bad
                    else:
                        $ JResu = ['C','C','C','Fail']
            elif JExam[2] < Examinee[2]: #reading bad
                if (JExam[3]+JExam[4]) < (Examinee[3]+Examinee[4]):
                    $ JResu = ['C','B','C','Fail']
                else:
                    $ JResu = ['C','C','C','Fail'] #reading bad, total of Vocab/Grammar bad
            else: #listening and reading bad
                $ JResu = ['C','C','C','Fail']
    elif JExam[0] < Examinee[0]: #if Academics good
        if (JExam[1]+JExam[2]) < (Examinee[1]+Examinee[2]):
            # check Reading/Listening
            if (JExam[3]+JExam[4]) < (Examinee[3]+Examinee[4]):
                # check Vocab/Grammar
                $ JResu = ['B','B','B','Pass']
            else:
                $ JResu = ['C','C','B','Fail']
        else:
            if (JExam[3]+JExam[4]) < (Examinee[3]+Examinee[4]):
                $ JResu = ['B','B','C','Fail']
            else:
                $ JResu = ['C','C','C','Fail']
    else:
        $ JResu = ['C','C','C','Fail']

    return