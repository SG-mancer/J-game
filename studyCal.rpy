# ---------------
# Calculate and adjust status scores depending on the courses taken...    
label studyCal:
    python:
        # # # # # # # #
        # cyle through the study choices, adjusting the Statuses (soci, phys, ment) and adding to this weeks ability modifier (konshuAbil[])
        for x in study:

            sMCounts[x] += 1 #counts how many times this choice has been made
            
            if x == 0: 
                # unselected / unavailable study periods - disregard the count
                sMCounts[x] -= 1 

            elif x == 'nap':
                # nap for bonus stats
                soci += 1
                phys += 1
                ment += 1

            elif x == 'jog':
                # jogging clears your head
                soci += 1
                ment += 1
                if 'jog' in senshuStudy and sMCounts[x] > 5:
                    # jogging doesn't cost phys if you have routine, and more than 5 jogs
                    ""
                else:
                    phys -= 1

            elif x == 'datingApp':
                # Matches - a dating app (Tinder parody). In Aus you barely matched, but in Japan you get a few matches and can chat will girls
                soci -= 1
                if sMCounts[x] > 2:
                    # If more than 2 times using app you can start dating
                    "hi"

            elif x == 'computerGames':
                # Playing computer games
                ""
            
            elif x == 'shopping':
                # Go shopping on the weekends
                phys -= 1
                soci -= 1
            
            elif x == 'clubbing':
                # Go clubbing on the weekends
                phys -= 1
                soci -= 1

            elif x == 'SRS_kanji':
                # Spaced Repetition Kanji - you have 2 methods, RTK, School Kanji List - it is dificult, improves Reading, (and Vocab or Grammar if 2 weeks in row)
                if listRTK:
                    # If you chose the RTK list this list costs extra mental fatigue
                    ment -= 1
            
                if 'SRS_kanji' in senshuStudy:
                    ment -= 1
                    if sMCounts % 3:
                        konshuAbil[0] += 1
                    else:
                        konshuAbil[1] += 1
                else:
                    ment -= 2
                konshuAbil[2] += 1

            elif x == 'SRS_vocab':
                # Spaced Repetition Vocabularly - needs to be used in conjuction with Vocab collectors
                if 'SRS_vocab' in senshuStudy:
                    ment -= 1
                else:
                    ment -= 2
                konshuAbil[0] += 1
                konshuAbil[2] += 1

            elif x == 'SRS_convo':
                # Spaced Repetition Conversation - improves Writing/Speaking, Vocab (and Grammar if done 2 weeks in a row)
                if 'SRS_convo' in senshuStudy:
                    ment -= 1
                    konshuAbil[1] += 1
                else:
                    ment -= 2
                konshuAbil[4] += 1
                konshuAbil[0] += 1

            elif x == 'workbook':
                # Do extra homework from a workbook - improves vocab, grammar?
                ment -= 1
                konshuAbil[0] += 1

            elif x == 'text-book':
                # Read forward in the textbook - improves grammar and reading
                ment -= 1
                konshuAbil[1] += 1
                konshuAbil[2] += 1

            elif x == 'JLPT_drill':
                # Do quiz/drills for JLPT - improves your reading/grammar
                ment -= 1
                konshuAbil[2] += 1
                konshuAbil[1] += 1
            
            
            # Each turn check Fatigue Stats are not above maximum
            if soci > max_stat:
                statOP += 1
                soci = max_stat
            if phys > max_stat:
                statOP += 1
                phys = max_stat
            if ment > max_stat:
                statOP += 1
                ment = max_stat
            # Note:: we wait until after calculating everything in the week to check if you have negative Stats
            # # # # # # # #
    
    # After the whole week bonus is calculated
    # If any Fatigue Stat is below Zero clear this weeks Ability modifier
    if soci < 0 or phys < 0 or ment < 0:
        $ konshuAbil = [0,0,0,0,0]

    # Loop throgh each Ability and add this weeks and any bonus modifiers
    $ x = 0
    while x < 5:

        $Ability[x] += konshuAbil[x]

        # Low Fatigue Bonus, if all Fatigue Stats are over half - get Ability bonus from 2 weeks ago
        if soci > 2 and phys > 2 and ment > 2:
            $ Ability[x] += sensenAbil[x]

        # Disciplin bonus
        if study == senshuStudy:
            # If 2 weeks in row identifical choices - get last week Ability bonus + 1 to each ability
            $ Ability[x] += (senshuAbil[x]+1)
        elif study[1] == senshuStudy[1] and study[2] == senshuStudy[2]:
            # If Morning and Evening 2 weeks in a row identical - get Ability bonus from last week
            $ Ability[x] += senshuAbil[x]

        $ x += 1
  
    # Warn if close to burn out - if you have depleted any fatigue stat to 0
    if soci == 0 or phys == 0 or ment == 0:
        "warning: You are about to burn out"
    
    # Handle Burn out/s
    if soci < 0:
        "Social Burn out"
        $ soci = 0
    if phys < 0:
        "Physical burn out"
        $ phys = 0
    if ment < 0:
        "Mental burn out"
        $ ment = 0

    # Go to next week
    jump looper

    return