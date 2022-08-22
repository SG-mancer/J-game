# ---------------
# Calculate and adjust status scores depending on the courses taken...    
label studyCal:
    python:
        # sycle through our list
        for x in study:
              
            if x == 0: #used for unavailable study periods
                break
            elif soci < 1 or phys < 1 or ment < 1:
                "burn out"
                yenYen -= 10000
            elif x == 'jog':
                # jogging clears your head and improves your athletics. Jog enough and maybe even get to enter races
                soci -= 1
                phys += 1
                ment += 1
            elif x == 'Rem_Kanji':
                soci -= 1
                ment -= 1
                if (week_count % 3):
                    Ability[2] -= 1
                else:
                    Ability[2] += 1
                if (week_count % 2) == 0:
                    Ability[4] += 1


    # Check Fatigue, Motivation or Confidence reserves are not above maximum
    if soci > max_stat:
        $ soci = max_stat
    if phys > max_stat:
        $ phys = max_stat
    if ment > max_stat:
        $ ment = max_stat
        
    # Check we haven't depleted (went to 0 or lower) Fatigue, Motivation or Confidence
    
        
    return