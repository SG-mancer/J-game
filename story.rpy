
# Handle if the story has a scene here - called every week
label story:
    t "story goes here"
    return

# Oslo (o) and Jack (z)*the player chat about the plant shutting down...
# > select school,
label beginning:
    show text "The incidents described in this game never took place.\nSo many people travel to and study in Japan it is likely\nthat some will find their names in the following text.\n\nNo reference is intended to anyone living or dead." at truecenter
    with dissolve
    pause 10
    hide text
    with dissolve

    scene bg japanflight
    pause 5
    "Sydney - 8:30am Saturday 28 March 2015"
    nvl clear
    # Select the player character
    menu:
        "Choose your character:"
        "1. Dylan Barry - 31 year old":
            # Born Showa 58
            $ z = barry
            nvl clear
            "Boarding the flight, you are a little unsure. This feeling is not as great as the relief you felt when you sold your car. (That felt like letting go of the last item anchoring you to Australia)"
            "You think about how all your belongings are on this plane. Overhead is a backpack, in the seat pocket and below you somewhere in the hold."
            "\nAt 31 years old, all through your twenties you never had enough money to do this."
            "You think about when you moved away to Uni with only a few hundred dollars, then dropped out because it became too difficult to cope. From that low, you were sucked into a dead end sales job."
            "The past ten or so years have been a blur of working suburbs and rural towns, walking house to house canvasing and selling, lonely or drunk weekends and no way out."
            #nvl clear
            "A little under 2 years ago you travelled to Japan for the first time. After a three day conference in Niigata, you spent a long weekend exploring Tokyo enjoying roof top beer gardens, convenience stores, skytree and just wandering the suburbs in awe."
            "It made you curious, and on the flight back you were already planning a next trip. You took a ten week evening class."
            "Then booked a few weeks in the snow at Niseko, then Nagano before racing around the islands with a 3 week JR Pass."
            "It was probably the traveling, in the warmth of a \"wan-man densha\" seeing the beautiful winter mountain and seaside views that made you fall in love with Japan."
            "You wished you could had stayed longer, and explored more, experience Sakura and Momiji... But being over 30 you couldn't get a working holiday visa, and not having a degree meant you couldn't join an English teaching program."
            "\nThen, a few months later - browsing the internet on a rainy weekend, you found a blog where a polyglot who explained how they learnt Japanese in 6 months and passed the JLPT N2."
            "It made you determined to go to do something similar." 
            "\nThe school and visa application wasn't too difficult. Just a few emailed forms, and two visits to drop off your passport and collect your visa."
            "You were similarly surprised the fees were only about 300,000yen a semester (approx $3500 AUD - getting 80-90yen for $1 AUD). For the past 6 months, you saved every spare cent you could, and sold your belongings to fund this trip."
        "2. {b}Bradly Ryan{/b} - 22 year old":
            # Born Heisei 4
            $ z = ryan
            nvl clear
            "You had hoped to get a window seat, but at checkin you were upgraded to premium economy in the middle seat."
            "It is exciting a nerv racking to be going to Japan. Other than in anime, your first glipse of Japan was in 2011 when you watching intently the news coverage of the 11 March Tsunami and Fukushima incident."
            "One thing had lead to another, and just after the end of your first semester of university you were entrawled in a conspiratorial political group."
            "It has only been five or six months since you left. But each day you are glad you are no longer slaving away, and poising your mind with lies."
            "Your plan is to focus on learning Japanese, and making friends."
        #"3. AABDL NRRYY" # A third character ???

    nvl clear
    scene bg flightmap
    with dissolve

    show fltcon at left

    "8:40am - After watching the safety demonstration, the Boeing 777 heads to the runway for immediate departure."
    "8:55am - The seatbelt sign turns off, and you open your bag and pull out your new organiser."

    # TUTORIAL HERE

    if z == ryan:
        "hi Ryan [z]"
    elif z == barry:
        "hi barry"
    else:
        "[z] what is up. [pc]"


    scene planner
    pause 5
    "You open up your new planner on the tray table. "
    call tutorial
    
    return






    a "Are you ready to start studying again?"
    menu:
        z "For past few months, I've been disciplined, each day spending an hour studying:"
        "Studying a textbook":
            $ studMeths.append('text-book')
            z "I've been practicing dialogues, trying to build a flash card deck of vocab and phrases from a textbook.\nIt is difficult, I'm almost finished the first book of 12 lessons."
        "Listening to classes on CDs":
            $ studMeths.append('cd')
            z "I've been following along with classes on CD.\n"
        "Reading blogs and listening to podcasts":
            $ studMeths.append('browse-web')
            ""

    nvl clear

    menu:
        z "I also recently read about a group of people doing crazy things to learn Japanese."
        "Studying Remember the Kanji to learn the 2,136 Kanji in a month (100 new Kanji a day).":
            $ studMeths.append('Rem_Kanji')
        "Using a spaced repition App on my phone, and drilling vocab.":
            $ studMeths.append('Flash_Vocab')
        "Studying a FAST course textbook, and drilling dialogues.":
            ""
    
    
    # The flight
    nvl clear

    scene bg japanflight
    "30 March 2015 - Sydney Airport "
    
    # one last check of your paperwork


    return

# Getting a mobile phone
label keitai:
    ""

    return

# Getting a bank account
label ginko:
    ""

    return

# Visiting City/Ward Office
label kyuyakusho:
    "Get address registered"
    "Get National Health Insurance"
    "Lodge taxes paperwork"
    "Try avoid the Pension stuff"

    return
