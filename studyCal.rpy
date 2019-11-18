# this is called to initiate studMeth and sMcounts (only once at start of game) - it is here to modulise the game
label init_study:
    $ studMeths = ['jog','heisig','revise_notes'] #The options available to player at start
    # List of study methods and count done, and the primary cost (ment, soci or phys) for the activity
    $ sMcounts = {'0':0, 'jog':0,'heisig':0, 'revise_notes':0, 'podcast':0}
    $ sMfocus = {'0':0, 'jog':2,'heisig':0, 'revise_notes':0, 'podcast':0}
return

# ---------------
# Calculate and adjust status scores depending on the courses taken...    
label studyCal:
        python:
            for x in study:
                sMcounts[x] += 1 #add to the count for this study method
                if x == 0: #used for unavailable study periods
                    continue

                elif x == 'jog':
                    if sMcounts > 10 and Talen[1] > 5:
                        phys -= 1
                        ment += 2
                        if (sMcounts % 15) == 0: #every 15 jogs increases your athletics
                            Talen[1] += 1
                        # TODO: Add Tokyo Marathon (weekend 47 and 99) if Tale[1] > 20 ??
                        if ()
                    elif Talen[1] > 5:
                        phys -= 1
                        ment += 1
                    elif (sMcounts % 5) == 0: #every 5 jogs increases your athletics
                        phys -= 2
                        ment += 1
                        Talen[1] += 1
                    else: #starting to jog costs 2 phys and gives 1 ment
                        phys -= 2
                        ment += 1
                    continue

                elif x == 'heisig':
                    ment -= 1
                    continue

                elif x == 'revise_notes':
                    ment -= 1
                    continue
                
                elif x == 'podcast':
                    ment -= 1
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