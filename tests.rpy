# This file is for testing the game core loop
label test1:

    $ week_count = 0
    $ burnoutWarn = 0
    $ Talen[1] = 6
    $ school = 0

    while week_count < 100:
        
        $ study = ['homework', 'rev_class', 'eConvo', 'SRS', '0']
        
        call monday
      
        call studyCal
        call HomeWorkCheck
        call Learning
        
        if week_count in [11,21,31,41,51,61,71,81,91,101,102]:
            z "week [week_count].\n[Talen],[Skill],[Knowl]. \nBurnout:[burnCount]. Warning:[burnoutWarn]"
        
    
    z "week [week_count].\n[Talen],[Skill],[Knowl]. [burnCount]"
    return
