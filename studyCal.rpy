# ---------------
# Calculate and adjust status scores depending on the courses taken...    
label studyCal:
    python:
        # cyle through the study choices, adjusting the Statuses (soci, phys, ment) and adding to this weeks ability modifier (konshuAbil[])
        for x in study:
            
            if x == 0: #used for unavailable study periods, or periods player chose to not select anything
                break
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


    # Check Fatigue Stats are not above maximum
    if soci > max_stat:
        $ soci = max_stat
    if phys > max_stat:
        $ phys = max_stat
    if ment > max_stat:
        $ ment = max_stat
    
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