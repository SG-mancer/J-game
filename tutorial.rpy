# A tutorial for the player. So they understand what is going on
label tutorial:
    menu:
        "Do you want me to explain how to play"
        "Yes":
            call FullTutorial
        "I have a specific question":
            call tutorialTopics
        "No":
            return
        
    return

label FullTurorial:
    x "this game... doesn't have a full tutorial yet"
    return

label tutorialTopics:
    menu:
        "what choices should I make?":
            x "good question, well asked."
        "how do I win?":
            x "I don't know"
    return
    
    