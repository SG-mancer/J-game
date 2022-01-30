
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

    # "You were becoming disheartened with work. The pay was good, but you always found the swing difficult to plan around. You were away pretty much three weeks every month, with a long holiday usually in February."

    
    # No one cares about what your paperwork is... or that you were FIFO for 4 or 5 years, working 9-on 5-off (work Monday, back home the following Wednesday, then off until Monday), or 12-on 9-off (leave Monday work until following Friday, then have a week off back to work on Monday), or 19 on and 9 off (arrive home on Friday back to work in 2 Sunday's time for 2 and a bit weeks)
    
    # the hardest thing about FIFO - was that you didn't feel part of the community. You were away often, and when you were home everyone else was working.
    # lonely you started learning French, travelled the France for a few weeks and didn't like it.
    # then somehow you started learning Hirigana and Katanaa, got a textbook and started learning to talk some Japanese each night after your 12 hour shift.
    # You also started snowboarding on your off week, and planned to visit Japan on your 4 weeks off in Feb/Mar

    # Dating websites? How they didn't work, or maybe you wasted money on them...

    # couch surfing?

    # Your twenties were hard working. You dropped out of Uni, and worked a dead end job for a few years before finding a FIFO job. Then whilst earning the big money, you traveled overseas on your off-swings. Visiting South East Asia, Europe and Pacific islands.
    # In 2012 at 29 you started snowboarding. Visiting Japan in 2013 for the powder. Then a second time in 2014 for a long rail holiday.

    menu:
        "How have you been studying Japanese?"
        "Studying a textbook":
            z "I've been practicing dialogues, trying to build a flash card deck of vocab and phrases from a textbook.\nIt is difficult, I'm almost finished the first book of 12 lessons."
        "Listening to classes on CDs":
            z "I've been following along with classes on CD.\n"
        "Reading blogs and listening to podcasts":
            ""
    
    z "Because I was working, I couldn't sit the JLPT last year."
    
        
    scene bg japanflight
    "30 March 2015 - Sydney Airport "
    


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
