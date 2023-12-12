label story:
    stop music fadeout 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file is core of Visual Novel, later it can be split to chapters and routes if needed.  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    scene background1
    play music "ost.mp3" fadeout 1

    #testing new assets
    show chieneutral at centre with dissolve 
    ch "hello world"
    
    stop music fadeout 1
    ch "Anyway, this is the end of demo."

    
    return
