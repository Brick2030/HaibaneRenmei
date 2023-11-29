label story:
    stop music fadeout 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file is core of Visual Novel, later it can be split to chapters and routes if needed.  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    scene bg room
    play music "ost.mp3" fadeout 1


    show hikari a1 at left2
    hi "Hello haibanes"

    
    hi a2 "I'm Hikari! Nice to meet you!"
    hi a1 "This is a demo of Haibane Renmei visual novel!"
    hi "Lorem ipsum dolor sit amet,"
    hi a2 "consectetur adipiscing elit"
    hi "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    
    show rakka b at left2
    show hikari a1 at right1
    stop music fadeout 1
    play music "ost2.mp3"
    
    hi "Oh!"
    ra "Hello Hikari!"
    ra " Ut enim ad minim"
    hi a2 "quis nostrud exercitation"
    ra "ullamco laboris nisi ut aliquip ex ea commodo consequat"
    hi a1 "I dont even know what that latin text means"
    stop music fadeout 1
    ra "Anyway, this is the end of demo."

    
    return
