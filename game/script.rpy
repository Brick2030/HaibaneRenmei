# The script of the game goes in this file.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Some script file. Do even need this file? Probably starts the scene. Not sure if it can be started from somewhere else  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# The game starts here.


# Testing experimental branch.

image background_video = Movie(size =(1600,900), channel="movie", play="gui/MainMenu/main_menu.ogv", loop=True)



image continue_feather:
    "gui/feather/frame_00.png"
    pause 0.1
    "gui/feather/frame_01.png"
    pause 0.1
    "gui/feather/frame_02.png"
    pause 0.1
    "gui/feather/frame_03.png"
    pause 0.1
    "gui/feather/frame_04.png"
    pause 0.1
    "gui/feather/frame_05.png"
    pause 0.1
    "gui/feather/frame_06.png"
    pause 0.1
    "gui/feather/frame_07.png"
    pause 0.1
    "gui/feather/frame_08.png"
    pause 0.1
    "gui/feather/frame_09.png"
    pause 0.1
    "gui/feather/frame_10.png"
    pause 0.1
    "gui/feather/frame_11.png"
    pause 0.1
    "gui/feather/frame_12.png"
    pause 0.1
    "gui/feather/frame_13.png"
    pause 0.1
    "gui/feather/frame_14.png"
    pause 0.1
    "gui/feather/frame_15.png"
    pause 0.1
    "gui/feather/frame_16.png"
    pause 0.1
    "gui/feather/frame_17.png"
    pause 0.1
    "gui/feather/frame_18.png"
    pause 0.1
    "gui/feather/frame_19.png"
    pause 0.1
    "gui/feather/frame_20.png"
    pause 0.1
    "gui/feather/frame_21.png"
    pause 0.1
    "gui/feather/frame_22.png"
    pause 0.1
    "gui/feather/frame_23.png"
    pause 0.1
    "gui/feather/frame_24.png"
    pause 0.1
    "gui/feather/frame_25.png"
    pause 0.1
    repeat


init -2:
    image ctc_anchored:
        alpha 1.0 
        yalign 1.0 xalign 0.95
        "continue_feather"


screen ctc_screen:
    add ctc_anchored

label start:


call story
return
