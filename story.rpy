
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

    ## You are at Cootamundra Airport waiting to change to a Dreamliner (Boeing 787) for your flight to Narita Airport.
    ## Alone, you are now setting out to learn Japanese in a year...

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

    #
    #
    # https://www.eadeverell.com/language-learning-methods/
    # https://www.fluentu.com/blog/how-to-study-a-language/
    # https://www.usa.edu/blog/study-techniques/
    # https://matadornetwork.com/bnt/7-tips-for-learning-a-foreign-language-on-the-road/
    # https://matadornetwork.com/abroad/the-5-ways-we-learn-languages-and-which-style-is-right-for-you/
    #
    #

    # Choose your school
    menu:     
        "I haven't applied yet. But I think I will study this school in..."
        "{b}Takadanobaba{/b}\nIt is near Waseda University so I can regularly interact with Japanese students.":
            $ school = 1
        "{b}Shinjuku{/b}\nWith many Chinese students so I will have to study hard.":
            $ school = 0
        "{b}Osaki{/b}\nWith English speaking teachers, to help me understand the key points.":
            $ school = 2

    o "Good luck in Japan. \n Bring back a good looking translator ;)"
    z "I will miss Kanbogan."
    o "Nah, the place will be finished with the plant closing."
    return