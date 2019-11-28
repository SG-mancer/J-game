
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