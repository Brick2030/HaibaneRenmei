label story:
    stop music fadeout 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file is core of Visual Novel, later it can be split to chapters and routes if needed.  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    scene bg room
    play music "ost.mp3" fadeout 1


    show hikari a at left2
    hi "Hello haibanes"
    
    show hikari b at left1
    hi "I'm Hikari! Nice to meet you!"
    
    show hikari a at centre
    hi "This is a demo of Haibane Renmei visual novel!"
    
    show hikari a at right1
    hi "Lorem ipsum dolor sit amet,"
    
    show hikari a at right2
    hi "consectetur adipiscing elit"

    show hikari b at left2
    hi "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    
    show rakka b at left1
    show hikari a at right1
    stop music fadeout 1
    play music "ost2.mp3"
    
    hi "Oh!"
    ra "Hello Hikari!"
    ra "Ut enim ad minim veniam"

    show hikari b
    hi "quis nostrud exercitation"
    ra "ullamco laboris nisi ut aliquip ex ea commodo consequat"
    hi "I dont even know what that latin text means"
    stop music fadeout 1
    ra "Anyway, this is the end of demo."

    
    return
