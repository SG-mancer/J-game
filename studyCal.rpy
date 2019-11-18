# this is called to initiate studMeth and sMcounts (only once at start of game) - it is here to modulise the game
label init_study:
    $ studMeths = ['jog','nap','rev_notes','rev_class','browse_web','flash_cards'] #The options available to player at start
    # List of study methods and count done, and the primary cost (ment(0), soci(1) or phys(2), none(3)) for the activity
    $ sMcounts = {'0':0, 'jog':0,'nap':0,'rev_notes':0,'rev_class':0,'browse_web':1,'flash_cards':0,'SRS':0}
    $ sMfocus = {'0':0, 'jog':2,'nap':3,'rev_notes':0,'rev_class':0,'browse_web':1,'flash_cards':0,'SRS':3}
    $ FlashCards = 0 #Flashcard set (for flash card study)
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
                    if sMcounts[x] > 10 and Talen[1] > 5:
                        phys -= 1
                        ment += 2
                        if (sMcounts[x] % 15) == 0: #every 15 jogs increases your athletics
                            Talen[1] += 1
                        # TODO: Add Tokyo Marathon (weekend 47 and 99) if Tale[1] > 20 ??
                    elif Talen[1] > 5:
                        phys -= 1
                        ment += 1
                    elif (sMcounts[x] % 5) == 0: #every 5 jogs increases your athletics
                        phys -= 2
                        ment += 1
                        Talen[1] += 1
                    else: #starting to jog costs 2 phys and gives 1 ment
                        phys -= 2
                        ment += 1
                    continue

                elif x == 'nap':
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

                elif x == 'rev_notes': #Improve Vocab. Grammar every 2nd, every 13th bonus 5 (Academics, Reading, Listening, Kanji, General) 
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

                elif x == 'rev_class':
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
                    soci -= 1
                    if ment > 1: #If you have 2 ment, you improve Listening & Vocab, Pronounciation 50% time, Reading & Kanji 14%
                        ment -= 1
                        Skill[1] += 1
                        Knowl[0] += 1
                        if sMcounts[x]%2 == 0:
                            Skill[2] += 1
                        if sMcounts[x]%7 == 0:
                            Skill[0] += 1
                            Knowl[2] += 1
                    else:
                        Skill[3] += 1 #Otherwise you just find general info, no Japanese...
                    if sMcounts[x]%3 == 0:
                        #TODO 33% chance of finding new web resources for studying online...
                        if 'SRS' in studMeths:
                            pass
                        else:
                            studMeths.append('SRS')
                    continue
                
                elif x == 'flash_cards':
                    ment -= 1
                    if FlashCards == 0: #if no flashcard set, improves Grammar and Vocab. and Kanji every 4th use.
                        Knowl[0] += 1
                        Knowl[1] += 1
                        if sMcounts[x]%4 == 0:
                            Knowl[2] += 1
                    elif FlashCards == 1: #with Flashcard set 1, improves
                        #TODO with flashcard set, you have more results
                        pass
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
            o "don't burn yourself out"
        if ment < 0:
            $ burnout = True
        #The pentalty for burning out soci or phys is no soci or phys choice the next week
        if soci < 0:
            $ soci = -1
        if phys < 0:
            $ phys = -1
return