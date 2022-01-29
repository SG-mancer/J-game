# ---------------
# Calculate and adjust status scores depending on the courses taken...    
label studyCal:
    python:
        # sycle through our list
        for x in study:
                
            if x == 0: #used for unavailable study periods
                continue

            elif x == 'jog':
                # jogging clears your head and improves your athletics. Jog enough and maybe even get to enter races
 
                continue


    # Check Fatigue, Motivation or Confidence reserves are not above maximum
    if fatig > max_stat:
        $ fatig = max_stat
    if motiv > max_stat:
        $ motiv = max_stat
    if confi > max_stat:
        $ confi = max_stat
        
    # Check we haven't depleted (went to 0 or lower) Fatigue, Motivation or Confidence
    if fatig < 1 or motiv < 1 or confi < 1:
        "burn out"
        
    return