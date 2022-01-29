
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

    scene bg tokyonight

    # No one cares about what your paperwork is... or that you were FIFO for 4 or 5 years, working 9-on 5-off (work Monday, back home the following Wednesday, then off until Monday), or 12-on 9-off (leave Monday work until following Friday, then have a week off back to work on Monday) 
    
    # the hardest thing about FIFO - was that you didn't feel part of the community. You were away often, and when you were home everyone else was working.
    # lonely you started learning French, travelled the France for a few weeks and didn't like it.
    # then somehow you started learning Hirigana and Katanaa, got a textbook and started learning to talk some Japanese each night after your 12 hour shift.
    # You also started snowboarding on your off week, and planned to visit Japan on your 4 weeks off in Feb/Mar

    # Dating websites? How they didn't work, or maybe you wasted money on them...

    # couch surfing? 

    "You check over your paperwork. * Passport with Student Visa, * Residency Card (Zairyū Card) application, * Part time work application, * language school enrolement letter, * passport photo, * bank card..."
    "and a * printed one way ticket to Tokyo (Narita)."
    "Three years working FIFO, two weeks on one week off has swelled your bank account."

    "Rather than buy a house, and"

    "== Jikoshoukai ==" ## Part 1 - self introduction
    "From the Airport Bar you watch as all your belongings in two bags are loaded into the cargo hold of the Boeing 787 Dreamliner."""


    menu:
        "Hajimemashite, Watashi wa _Dylan Thomas_ desu.\nHow do you do, My name is _Dylan Thomas_."
        "I like snowboarding.":
            ""
        "I like watching anime.":
            ""
        "I like travelling.":
            ""
    
    menu:
        "For the past few months I've been studying Japanese by:"
        "Reading a text book.":
            ""
        "Listening to podcasts.":
            ""
        "Reading blogs.":
            ""
        "Watching music videos online.":
            ""

    "8 and a half hour flight - Gold Coast to Tokyo (Narita)"

    # set your language learning style
    "Over the past few years, you have visited Japan 3 times."
    "On your first visit you visited Sapporo, a three days in Tokyo visiting Shinjuku, Akihabara and Takadanobaba. But you didn't know what Managa or Anime to buy."
    "On your second trip, you got a Japan Rail pass for 21 days. Visited Tokyo for a week, then couch surfed around Honshu. Spending a week in Hiroshima and Yamaguchi, then a week in Osaka, Kobe and Kyoto before a week in Nagano, Niigata and then racing up to Aomori."
    "Your third trip..."

    # addicted to Pachinko? Snowboarding? Hentai? Games?

    # understand how the player has learnt until now.
    "Since New Years, you have been spending three hours a day studying."
    menu:
        "Most of your study is"
        "Studying a phrase book":
            "intesting, and useful. Do you drill the common phrases?"
        "Listening to a podcast":
            "Japan Daily, Japan Pod 101 - it is a good mix"
        "Using a CD to practice conversations":
            "Maybe it was Pimsleur or Michel Thomas method. You are following along."
        "Chatting online to Japanese friends":
            "from couch surfing, you are giving you tips. But mostly talking english."
        "Attempting to learn as many Kanji as possible":
            "Heisig, you aren't even learning how to say them. Just what the key word is, and how to draw them."
        "Reading Manga":
            "this is hard too. What Manga do you have?"
        "Following along with the textbook":
            "This is so boring. But you are getting a few basics..."
    
    # get your goal, why is it they are learning Japanese ? Or should I set this for them ?

    menu:
        "Why do you want to learn Japanese?"
        "Looking for love?":
            "You are searching for love? Do you have Yellow Fever?" # actually we could play this out. You have a solid savings about 25% of a $400k house.
            # have someone suggest you marry a dictionary
            # or explore your loneliness, wanting to meet people. Sick of a lonely job, needing a bit of excitement - so moving to Japan for a year
        "To get into business":
            "What type of business?" # play this, as in the player doesn't yet know 
        "So I can watch Anime without subtitles":
            "Hmm, so you will spend a year, just to watch tv?"

    # Choose your school
    menu:     
        "I haven't applied yet. But I think I will study this school in..."
        "{b}Takadanobaba{/b}\nIt is near Waseda University so I can regularly interact with Japanese students.":
            $ school = 1
        "{b}Shinjuku{/b}\nWith many Chinese students so I will have to study hard.":
            $ school = 0
        "{b}Osaki{/b}\nWith English speaking teachers, to help me understand the key points.":
            $ school = 2

    return