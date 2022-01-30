
# Handle if the story has a scene here - called every week
label story:
    t "story goes here"
    return

# Oslo (o) and Jack (z)*the player chat about the plant shutting down...
# > select school,
label beginning:
    show text "The incidents descibed in this game never took place.\nSo many people travel to and study in Japan it is likely\nthat some will find their names in the following text.\n\nNo reference is intended to anyone living or dead." at truecenter
    with dissolve
    pause 10
    hide text
    with dissolve

    ## Your friend Andy has offered to drive you up to Sydney, rather than you catching the train.
    # "After winding up work, you had spent the past few days back at your parents relaxing.\n Your Highschool friend Andrew offered to drive you up to Sydney, so he could see you off, and save you the 8 hour train ride."

    nvl clear
    # Select the bonus item you take with you to Japan.
    menu:
        a "Is that everything? You're moving to Japan and all you have is that?"
        "1. Snowboard bag stuffed with gear. \n2. Duffle bag.":
            z "My snowboarding gear."
        "1. Lightweight hiking backpack.\n2. Duffle bag.":
            z "my Hiking gear"
        "1. Suit bag. \n2. Rugged roller luggage.":
            z "figured I'ld pack a suit and cold weather jacket and some clothes. Rather than hang onto a snowboard for nine months until the season starts again, or "


    a "How did you come to the decisions to enroll in a language school?"

    # Select the first two study methods - note first one is solid, and second one is dubious (cost more fatigue, motivation or confidence)
    z "It is hard to work in mining and studying at the same time. The swing made it difficult to sign up for classes, and I'm not the best at self studying from a textbook."
    z "I also figured, I don't want to get get buy and house and get a mortgage. I would prefer having experiences."

    nvl clear

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
