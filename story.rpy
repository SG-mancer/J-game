
# Handle if the story has a scene here
label story:
    t "story goes here"
    return

# Oslo (o) and Jack (z)*the player chat about the plant shutting down...
# > select school,
label beginning:
    show text "Lost in Transition" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve

    # background of Kanbogon
    $ week_count = 2
    o "Sad that next year we will be pulling this plant down next year. I don't think Kanbogon will survive.\nDid they offer you much of a {b}redundancy{/b} package?"
    z "$37,000. I was expecting the just 16 weeks pay minimum for 9 years.\nBut the boss said something about how I had {i}inspired him by moving here at 18 and working hard as an apprentice.{/i}"
    o "This was your first job wasn't it Jack?\nYou came here right after high school?"
    menu:
        "I planned to work a year up here, then go to uni. But then I was offered an apprenticeship.":
            $ Knowl[3] += 4
            $ Talen[0] += 2
            o "I always thought you were smart. Are you planning to go back to Uni now?"
        "I had tried to join the Army in Year 11.\nI think moving away from home was my goal.":
            $ Knowl[3] += 2
            $ Talen[1] += 2
            $ Skill[3] += 2
            o "I never knew that. You are still young, will you apply to the Army again now?"
    z "I was planning to use my long service leave next year to go to a {b}language school{/b} in Japan.\nThe Japanese school year starts in April, what sort of lines up with a Feb/March shutdown."
    o "A language school? Why not just get a shack at Hakuba or Niseko, living off Sapporo beer, soba and ramen?\nAfter 9 years in snowys you love the mountains now, right?"
    o "How is your Japanese though?\nHave you been secretly studying it the past few years since your holiday there?"
    menu:
        "I have tried to teach myself with a textbook.\nIt is not easy to follow.":
            $ Talen[0] += 3
            $ Skill[0] += 1
            $ Knowl[0] += 2
        "I picked up computer program.\nIt is pretty basic.":
            $ Skill[0] += 2
            $ Skill[1] += 2
            $ Knowl[0] += 2
    z "No. I have always wanted to learn a second language, two years ago when I went there I loved the place. So maybe if"
    z "No, just {b}1 year in Tokyo{/b}. A {i}Language Student Visa lasts 1year 3months{/i} — 2years.\n{b}The school year starts in April{/b}, and the plant shuts down last week of Feburary."
    o "Wow. So you sound like you have this sorted.\nWhich school have you applied too?"

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