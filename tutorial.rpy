# A tutorial for the player. So they understand what is going on
label tutorial:

    "Show pictures to demonstrate making choices on the planner page"
    "The effect"
    "And how to open the stats view"

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
    
# ---------------
# This is how we can see what each study method does, and change new ones to our selection
label pickMethods:
    nvl clear
    $ x = 0
    while x < len(studMeths):
        $ tester = studMeths[x]
        $ textY = sMflav[tester]
        if sMfocus[tester] == 0:
            "{color=#000000}{b}[tester]{/b}\n█ No{/color} stat cost\n[textY]"
        elif sMfocus[tester] == 1:
            "{color=#0000ff}{b}[tester]{/b}\n█ Social{/color} stat cost\n[textY]"
        elif sMfocus[tester] == 2:
            "{color=#00ff00}{b}[tester]{/b}\n█ Physical{/color} stat cost\n[textY]"
        elif sMfocus[tester] == 3:
            "{color=#ff0000}{b}[tester]{/b}\n█ Mental{/color} stat cost\n[textY]"
        elif sMfocus[tester] == 4:
            "{color=#00ffff}{b}[tester]{/b}\n█{/color} {color=#0000ff}Social{/color} + {color=#00ff00}Physical{/color} stat cost\n[textY]"
        elif sMfocus[tester] == 5:
            "{color=#ffff00}{b}[tester]{/b}\n█{/color} {color=#00ff00}Physica{/color} + {color=#ff0000}Mental{/color} stat cost\n[textY]"
        elif sMfocus[tester] == 6:
            "{color=#ff00ff}{b}[tester]{/b}\n█{/color} {color=#0000ff}SociaRl{/color} + {color=#ff0000}Mental{/color} stat cost\n[textY]"
        else:
            "{color=#ffffff}{b}[tester]{/b}\n█{/color} {color=#0000ff}Social{/color} + {color=#00ff00}Physical{/color} + {color=#ff0000}Mental{/color} stat cost\n[textY]"
        $ x += 1

    $ x = 0
    while x < len(wkendMeths):
        $ tester = wkendMeths[x]
        $ textY = sMflav[tester]
        if sMfocus[tester] == 0:
            "{color=#000000}{b}[tester]{/b}\n█ No{/color} stat cost\n[textY]"
        elif sMfocus[tester] == 1:
            "{color=#0000ff}{b}[tester]{/b}\n█ Social{/color} stat cost\n[textY]"
        elif sMfocus[tester] == 2:
            "{color=#00ff00}{b}[tester]{/b}\n█ Physical{/color} stat cost\n[textY]"
        elif sMfocus[tester] == 3:
            "{color=#ff0000}{b}[tester]{/b}\n█ Mental{/color} stat cost\n[textY]"
        elif sMfocus[tester] == 4:
            "{color=#00ffff}{b}[tester]{/b}\n█{/color} {color=#0000ff}Social{/color} + {color=#00ff00}Physical{/color} stat cost\n[textY]"
        elif sMfocus[tester] == 5:
            "{color=#ffff00}{b}[tester]{/b}\n█{/color} {color=#00ff00}Physica{/color} + {color=#ff0000}Mental{/color} stat cost\n[textY]"
        elif sMfocus[tester] == 6:
            "{color=#ff00ff}{b}[tester]{/b}\n█{/color} {color=#0000ff}Social{/color} + {color=#ff0000}Mental{/color} stat cost\n[textY]"
        else:
            "{color=#ffffff}{b}[tester]{/b}\n█{/color} {color=#0000ff}Social{/color} + {color=#00ff00}Physical{/color} + {color=#ff0000}Mental{/color} stat cost\n[textY]"
        $ x += 1
        

    jump timetable