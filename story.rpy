
# Handle if the story has a scene here - called every week
label story:
    t "story goes here"
    return

label beginning:
    show text "The incidents described in this game never took place.\nSo many people travel to and study in Japan it is likely\nthat some will find their names in the following text.\n\nNo reference is intended to anyone living or dead." at truecenter
    with dissolve
    pause 10
    hide text
    with dissolve

    scene bg japanflight
    pause 5
    "Sydney - 9:30am Saturday 28 March 2015"
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

    "9:40am - After watching the safety demonstration, the Boeing 777 heads to the runway for immediate departure."
    "9:55am - The seatbelt sign turns off, and you open your bag and pull out your new organiser."

    # Introducting the Planner, offering a TUTORIAL
    nvl clear
    "Wanting to be as productive and focused as possible, you get out your study journal."
    "It is a present to yourself to track your goals, study timetable and appointments."
    menu:
        "Do you want to learn how to use your organiser (how to play J-game)?"
        "Yes, watch the tutorial.":
            call tutorial
        "No, I'll be fine with the organiser.":
            # Flavour text depending on the character
            if z == ryan:
                "hi Ryan"
            elif z == barry:
                "hi Barry"
    

    # Choose starting study methods
    nvl clear
    "10:20am - You watch the flight tracker for a minute and notice the plane is still over NSW: 12,000m above sea level, doing 770km/hr."
    "You think of how you have prefered studying Japanese so far."

    nvl clear
    menu:
        "You think the best way to improve your listening-speaking skills is to:"
        "- listen and follow along with an audio course.":
            $ studMeths.append('text-book')
        "- focus on drilling phrases before a situation (i.e. practice asking for directions before going out).":
            $ studMeths.append('text-book')
        "- through listening and watching Japanese content, with a pocket book for writing new words and phrases you come across.":
            $ studMeths.append('text-book')
    
    nvl clear
    menu:
        "To improve your reading-writing skills, you would recommend:"
        "- Readings lots, with a dictionary close by.":
            $ studMeths.append('text-book')
        "- Reading graded books.":
            $ studMeths.append('text-book')
        "- Practicing constructing new sentences each each day.":
            $ studMeths.append('text-book')

    nvl clear
    "You also have recently started using a Flash card/Spaced Repetition App."
    "At first it was to learn Kanji, but now you think..."

    menu:
        "{b}Kanji scares you{/b}, so you use a book called Remembering The Kanji. It claims once you memorise all of them kanji it will make learning grammar etc. easier. Remembering the mnemonics in the book is hard and you already have maximum reviews required each day.":
            $ studMeths.append('text-book')
        "{b}Kanju worries you{/b}, a blogger recommended learning them in the order Japanese kids learn them at school. You downloaded and setup a public deck of cards. Each day you learn 10-20 new kanji with how they pronounced in a sentence or two.":
            $ studMeths.append('text-book')
        "{b}Kanji is a bridge you will get to{/b}. You have focused on mastering hiragana and katakana first, learning new vocabulary based on themes (some crazy like the names of Yamanote line stations, others useful like parts of the body), each list a new deck in your flash card application. That takes as long to make as it does to practice in a week.":
            $ studMeths.append('text-book')


    #
    # The boredom of a flight - you will decide things to do during the flights remaining 8.5 hours.
    # You will get interupted by drinks, meals, turbulance (maybe)...
    #
    define flt_count = 0
    $ forgot_text = True
    $ flt_movie = False
    

    while flt_count < 20:
        nvl clear
        # Handling events (i.e. informing you of crossing the equator etc.)
        #
        if flt_movie:
            # If watching movie only a few events will be shown
            if flt_count == 1:
                "10:55am - The meal carts have been rolled out, and you will soon get a meal"
                $ flt_count = 9
            elif flt_count > 17:
                "16:15 - the meal carts have been rolled out"
                $ flt_count = 19
            elif flt_count == 20:
                "16:40 - the plane is now desending, and the meal is quickly cleared away."
            "You continue to watch the movie"
        else:            
            if flt_count == 0:
                "10:30am - The plane is now over the NSW/QLD border, flying 775km/hr at 12,000m."
            elif flt_count == 1:
                "10:55am - The meal carts have been rolled out, and you will soon get a meal"
            elif flt_count == 3:
                "11:45am - The meal is cleared away"
            elif flt_count == 5:
                "12:35am - now flying over PNG"
            elif flt_count == 9:
                "12:15 Tokyo Time - You have crossed the equator and wind your watch back an hour"
            elif flt_count == 13:
                "13:45 - you are now over Guam 910km/hr at 12,000m. The flight makes a small deviation."
            elif flt_count == 17:
                "15:25 - now flying over Tokyo Islands 915km/hr at 12,000m"
            elif flt_count == 19:
                "16:15 - the meal carts have been rolled out"
            elif flt_count == 20:
                "16:40 - the plane is now desending, and the meal is quickly cleared away."
            else:
                # Menu choosing what to do
                # - - - -
                menu:
                    "You contemplate what to do..."
                    "Study":
                        menu:
                            "What do you want to study?"
                            "Textbook" if forgot_text:
                                $ forgot_text = False
                                "As you reach into you bag for your textbook, you remember putting it down on the seat next to you in the Departure Lounge."
                                "When you got up to talk on your phone you didn't pick it up, and then walked to the window before deciding to wander the lounge for a few minutes."
                                "Your poor text book is now hundreds if not thousands of kilometers away..."
                                pause 2
                                "Maybe someone will find it, and be inspired to learn Japanese too."
                            "The back of your eyelids":
                                "You sleep"
                                $ flt_count += 1
                    "Go to the toilet":
                        "You stand up, and push past your seat mate to join the line of the toilet."
                        $ flt_count +=1
                    "Watch movie":
                        $ flt_movie = True
        $ flt_count += 1

    # The aircraft lands, and you continue the adventure
    "16:55 - The aircraft lands"
            
    jump looper




# ARE THE BELOW EVEN USEFUL?
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

# Buying a Teikiken - rail communter pass
label getTeikiken:
    # Buy a 6 month train ticket called a "Teikiken"
    # This should be called during weeks 1 (during the begining) and 25
    $ costX = teiTcst[homeStn]
    $ costY = stnTcst[homeStn]
    $costS = (250*costY) - costX
    
    menu:
        "Do you want to buy a Teikiken?\nA trip from home to school costs ¥[costY], what equals about ¥[costY]0 a week. You could instead pay ¥[costX] for a six month {b}Teikiken{/b}ticket.\nSaving you ¥[costS]"
        "yes, buy Teikiken":
            $ teikiken = True
            $ yenYen -= costX
            $ spentY += costX
        "no, I'm good.":
            $ teikiken = False
    
    return