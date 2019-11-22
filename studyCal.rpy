# this is called to initiate studMeth and sMcounts (only once at start of game) - it is here to modulise the game
label init_study:
    $ studMeths = ['jog','nap','rev_notes','browse_web'] #The options available to player at start
    #$ studMeths = ['jog','nap','rev_notes','rev_class','browse_web','flash_cards','homework','SRS','shadowing','eConvo','Dino.jp','Noteo','Manga_Study','PlanetJapan','CopyCat','J_quiz','group','eChat','WnoMori']  #full list
    # List of study methods and count done, and the primary cost (ment(0), soci(1) or phys(2), none(3)) for the activity
    $ sMcounts = {'0':0, 'jog':0,'nap':0,'rev_notes':0,'rev_class':0,'browse_web':0,'flash_cards':0,'homework':0,'SRS':0,'shadowing':0,'eConvo':0,'Dino.jp':0,'Noteo':0,'Manga_Study':0,'PlanetJapan':0,'CopyCat':0,'J_quiz':0,'group':0,'eChat':0,'WnoMori':0}
    $ sMfocus = {'0':0, 'jog':2,'nap':3,'rev_notes':0,'rev_class':0,'browse_web':1,'flash_cards':0,'homework':0,'SRS':0,'shadowing':0,'eConvo':1,'Dino.jp':0,'Noteo':0,'Manga_Study':0,'PlanetJapan':0,'CopyCat':0,'J_quiz':1,'group':1,'eChat':1,'WnoMori':3}
    $ FlashCards = 0 #Flashcard set (for flash card study)

    $ termNo = 1 #term number (it increases by incriments each time you finish a term and pass test)
    $ testWeeks = [12,25,37,49,62,75,89,100] # weeks TermExam will occur. week before holidays in Yr1, weekend before holidays in Yr2
    $ Txams = {1:[0,0,0,0,0,0,0],2:[0,0,0,0,0,0,0],3:[0,0,0,0,0,0,0],4:[0,0,0,0,0,0,0],5:[0,0,0,0,0,0,0],6:[0,0,0,0,0,0,0],7:[0,0,0,0,0,0,0],8:[0,0,0,0,0,0,0],9:[0,0,0,0,0,0,0]} #for TermExams [Acacemics, Reading, Listening, Pronou, Vocab, Gram, Kanji]
return

# ---------------
# Calculate and adjust status scores depending on the courses taken...    
label studyCal:
        python:
            for x in study:
                sMcounts[x] += 1 #add to the count for this study method
                if x == 0: #used for unavailable study periods
                    sMcounts[x] = 0 #I do not let it count
                    continue

                elif x == 'jog':
                    # jogging clears your head and improves your athletics. Jog enough and maybe even get to enter races
                    if sMcounts[x] > 10 or Talen[1] > 5:
                        phys -= 1
                        ment += 2
                        if (sMcounts[x] % 15) == 0: #every 15 jogs increases your athletics
                            Talen[1] += 1
                        if week_count == 27 or week_count == 79:
                            Marathon = True
                            MarathonPrac = 0 #set practice to zero
                            # TODO: Add Tokyo Marathon (weekend 47 and 99) if Tale[1] > 20 ??
                        if Marathon == True:
                            #Marathon practice, costs extra phys and ment. But completing marathon will give bonus
                            MarathonPrac += 1
                            ment -= 1
                            phys -= 1
                    elif Talen[1] > 5:
                        phys -= 1
                        ment += 1
                        if (sMcounts[x] % 5) == 0: #every 5 jogs increases your athletics
                            Talen[1] += 1
                    else: #starting to jog costs 2 phys and gives 1 ment
                        phys -= 2
                        ment += 1
                        if (sMcounts[x] % 4) == 0: #every 4 jogs increases your athletics
                            Talen[1] += 1
                    continue

                elif x == 'nap':
                    # sleeping improves your stats (but if you nap too much it just clears your head)
                    if sMcounts[x] < week_count: #If you have napped less than week, you get better rest
                         ment += 1
                         phys += 1
                         soci += 1
                    elif sMcounts[x]%2 == 0: #otherwise napping just gives you ment 50% time 
                        ment += 1
                    else:
                        ment += 1
                        phys += 1
                     
                    continue

                elif x == 'rev_notes' or x== 'PlanetJapan':
                    #Improve Vocab. Grammar every 2nd, every 13th bonus 5 (Academics, Reading, Listening, Kanji, General)
                    # You keep notes or words etc. you find hard. Reviewing them improves your skills 
                    ment -= 1
                    Knowl[0] += 1
                    if sMcounts[x]%2 == 0:
                        Knowl[1] += 1
                    if sMcounts[x]%13 == 0:
                        Talen[0] += 1
                        Skill[0] += 1
                        Skill[1] += 1
                        Knowl[2] += 1
                        Knowl[3] += 1
                    continue

                elif x == 'rev_class' or x == 'Manga_Study':
                    # Reviewing your class notes/textbook will improve your skills
                    ment -= 1
                    if sMcounts[x] <= week_count: #Improve Reading, Kanji, Vocab/Grammar (which ever less)
                        Skill[0] += 1
                        Knowl[2] += 1
                        if Knowl[0] > Knowl[1]:
                            Knowl[1] += 1
                        else:
                            Knowl[0] += 1
                    else: #Improve academics, reading and Kanji/Grammar (which ever less)
                        Talen[0] += 1
                        Skill[0] += 1
                        if Knowl[2] > Knowl[1]:
                            Knowl[1] += 1
                        else:
                            Knowl[2] += 1
                    continue
                
                elif x == 'browse_web':
                    # browsing the web, if you are focused will improve your listening and vocab. If lucky you will find new resources!!
                    soci -= 1
                    Skill[3] += 1 #you find general info, no Japanese...
                    if sMcounts[x]%3 == 0:
                        #TODO 33% chance of finding new web resources for studying online...
                        if 'flash_cards' in studMeths:
                            if 'eConvo' in studMeths:
                                if 'SRS' in studMeths:
                                    if 'Dino.jp' in studMeths:
                                        if 'Noteo' in studMeths:
                                            if 'Manga_Study' in studMeths:
                                                if 'PlanetJapan' in studMeths:
                                                    if 'CopyCat' in studMeths:
                                                        if 'eChat' in studMeths:
                                                            # After 27 clicks the player gets Reading, Listening every 3 turns
                                                            Skill[0] += 1
                                                            Skill[1] += 1
                                                        else:
                                                            studMeths.append('eChat')
                                                    else:
                                                        studMeths.append('CopyCat')
                                                    pass
                                                else:
                                                    studMeths.append('PlanetJapan')
                                            else:
                                                studMeths.append('Manga_Study')
                                        else:
                                            studMeths.append('Noteo')
                                    else:
                                        studMeths.append('Dino.jp')
                                else:
                                    studMeths.append('SRS')
                            else:
                                studMeths.append('eConvo')
                        else:
                            studMeths.append('flash_cards')
                    continue
                
                elif x == 'flash_cards' or x == 'Noteo':
                    # reviewing your flash cards improves your memory and Knowledge. With a better card set you get more improvements!!!
                    ment -= 1
                    if FlashCards == 0: #if no flashcard set, improves Grammar and Vocab. and Kanji every 4th use.
                        Knowl[0] += 1
                        Knowl[1] += 1
                        if sMcounts[x]%4 == 0:
                            Knowl[2] += 1
                    elif FlashCards == 1: #with Flashcard set 1, improves
                        #
                        #TODO with flashcard set, you have more results
                        #
                        pass
                    continue
                
                elif x == 'homework':
                    # Do your homework, it gives classHW bonus. As you get better it also improves Knowl & Skill
                    ment -= 1
                    soci -= 1
                    if week_count in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] and classHW == False: #If week is a prime number you get bonus Knowledges (but only once that week)
                        Knowl[0] += 1
                        Knowl[1] += 1
                        Knowl[2] += 1
                        Knowl[3] += 1
                    classHW = True #set flag for class homework (on weekend if not burnout you get bonus)
                    if Talen[0] > 10: #if you are smart, you improve Vocab or Grammar
                        if Knowl[0] > Knowl[1]*2:
                            Knowl[1] += 1
                        else:
                            Knowl[0] += 1
                        if Talen[0] > 30: #if very smart, you also improve Kanji or Reading
                            if Knowl[2] > Skill[0]*2:
                                Skill[0] += 1
                            else:
                                Knowl[2] += 1
                    else:
                        if sMcounts[x]%3 == 0: #every 3 weeks improve Academics (becauase HW is hard at first)
                            Talen[0] += 1
                    continue

                elif x == 'SRS' or x == 'Dino.jp':
                    #Spaced repition system, improves skills already developed. To a limit
                    ment -= 1
                    if Knowl[2]/12 > 1 and sMcounts[x]%2 == 0: #Kanji
                        if Knowl[2]/214 < 0: #stops at 214
                            Knowl[2] += 1
                            if Knowl[2]/50 > 1: #after Kanji 50 improve faster
                                Knowl[2] += 1
                    if Knowl[0]/4 > 1 and sMcounts[x]%3 == 0: #Vocab
                        if Knowl[0]/70 < 1: #stops at Vocab 70
                            Knowl[0] += 1
                    if Knowl[1]/8 > 1 and sMcounts[x]%5 == 0: #Grammar
                        Knowl[1] += 1
                        if Knowl[1]/50 < 1: #stops at 50
                            Knowl[1] += 1
                    continue

                elif x == 'shadowing' or x== 'CopyCat':
                    #Shadowing, reading along to a text that has an audio file. Repeating it to perfection.
                    ment -= 1
                    if Knowl[0] < 20: #if vocab less than 20, get 1 vocab
                        Knowl[0] += 1

                    if Skill[1] < 10: #if listening less than 10, you get 1 listening and 0.5 pronounciation
                        Skill[1] += 1
                        if sMcounts[x]%2 == 0:
                            Skill[2] += 1
                    elif Skill[0] < 40: #if reading less than 40 (listening 10 or more), reading and pronounciation improve
                        Skill[0] += 1
                        Skill[2] += 1
                    else: #if Listening > 10 and Reading > 40 
                        Skill[0] += 1
                        Skill[1] += 1
                        Skill[2] += 1
                    continue
                
                elif x == 'eConvo' or x == 'eChat' or x == 'WnoMori':
                    #online classes. These raise your academics, pronounciation, grammar and vocab 
                    soci -= 1
                    if x == 'eConvo':
                        yenYen -= 5000 #also costs cash
                    elif x == 'eChat':
                        yenYen -= 3000
                    elif x == 'WnoMori':
                        soci += 1 #Waseda No Mori, is free and doesn't cost social. Also, raises reading every 3 visits
                        if (sMcounts[x] % 3) == 0:
                            Skill[0] += 1
                    else:
                        yenYen -= 10000 #Big cost, not sure how someone gets here yet.

                    if Talen[0] < 100:
                        Talen[0] += 1
                    if Skill[2] < 20:
                        Skill[2] += 1
                    if Knowl[1] < 25:
                        Knowl[1] += 1
                    if Knowl[0] < 100:
                        Knowl[0] += 1
                    continue
                
                elif x == 'J_quiz':
                    # A JLPT Quiz book. As a percentage of N2 requirements
                    soci -= 1
                    if sMcounts[x]%10 in [1,7]:
                        Skill[1] += 1 #0.2 Listening
                    if sMcounts[x]%10 in[3,6,9]:
                        Knowl[1] += 1 #0.3 Grammar
                    if sMcounts[x]%10 in[2,4,8]:
                        Knowl[0] += 1 #0.4 Vocab
                    if sMcounts[x]%10 in[2,3,4,7,9]:
                        Talen[0] += 1 #0.6 Academics
                    if sMcounts[x]%10 in[1,2,3,4,5,6,7,8,9]:
                        Skill[0] += 1 #0.9 Reading
                    Knowl[2] += 1 #1 Kanji
                    continue

                elif x == 'group':
                    # study in a group. Improves your lowest 4 skills out of pairs.
                    soci -= 1
                    if Knowl[0] > Skill[1]: #Vocab / Listening
                        Skill[1] += 1
                    else:
                        Knowl[0] += 1
                    if Knowl[1] > Talen[0]: #Grammar / Academics
                        Talen[0] += 1
                    else:
                        Knowl[1] += 1
                    if Knowl[2] > Skill[0]: #Kanji / Reading
                        Skill[0] += 1
                    else:
                        Knowl[2] += 1
                    if (Knowl[4]*5) > Skill[2]: # General x5 (becayse it is not wanted) / Pronounciation
                        Skill[2] += 1
                    else:
                        Knowl[4] += 1 
                    continue

                pass

        # Check for max stat, burnout and warn if it is close, and give the burnout flag if player burnt out, set negative stats to -1 so they clear on Monday (except Ment that clears on weekend)
        if ment > max_stat:
            $ ment = max_stat
        if soci > max_stat:
            $ soci = max_stat
        if phys > max_stat:
            $ phys = max_stat
        
        if ment < 1:
            # o "don't burn yourself out"
            $ burnoutWarn += 1
        if ment < 0:
            $ burnout = True
        #The pentalty for burning out soci or phys is no soci or phys choice the next week
        if soci < 0:
            $ soci = -1
        if phys < 0:
            $ phys = -1
        z "calculated"
        return