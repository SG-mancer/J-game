# ---------------
# Calculate and adjust status scores depending on the courses taken...    
label studyCal:
    python:
        # sycle through our list
        for x in study:
              
            if x == 0: #used for unavailable study periods
                break
            elif fatig < 1 or motiv < 1 or confi < 1:
                "burn out"
                yenYen -= 10000
            elif x == 'jog':
                # jogging clears your head and improves your athletics. Jog enough and maybe even get to enter races
                fatig -= 1
                motiv += 1
                confi += 1
            elif x == 'Rem_Kanji':
                fatig -= 1
                confi -= 1
                if (week_count % 3):
                    Ability[2] -= 1
                else:
                    Ability[2] += 1
                if (week_count % 2) == 0:
                    Ability[4] += 1


    # Check Fatigue, Motivation or Confidence reserves are not above maximum
    if fatig > max_stat:
        $ fatig = max_stat
    if motiv > max_stat:
        $ motiv = max_stat
    if confi > max_stat:
        $ confi = max_stat
        
    # Check we haven't depleted (went to 0 or lower) Fatigue, Motivation or Confidence
    
        
    return