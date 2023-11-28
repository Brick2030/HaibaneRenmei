# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


############### CHARACTERS ##################################################
define hi = Character("Hikari")
define re = Character("Reki")
define ra = Character("Rakka")


################## POSITIONS #################################################
transform left2:
    xalign 0.0
    yalign 1.0
    
transform left1:
    xalign 0.25
    yalign 1.0
    
transform centre:
    xalign 0.5
    yalign 1.0

transform right1:
    xalign 0.75
    yalign 1.0
    
transform right2:
    xalign 1.0
    yalign 1.0
 
############################################################

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show hikari a at left2
    hi "Test message again"
    play music "ost.mp3" fadeout 1
    
    show hikari b at left1
    hi "Hello world!"
    
    show hikari a at centre
    hi "Testing git stuff"
    
    show hikari a at right1
    hi "Sometimes this might be boring"
    
    show hikari a at right2
    hi "New feature to git test 1"
    show hikari b at left2
    hi "Test"
    
    show rakka b at left1
    show hikari a at right1
    
    hi "Oh!"
    ra "Hello Hikari!"
    ra "Stop saying those weird words"
    show hikari b
    hi "Dont worry! I was testing new features!"
    ra "Sounds impressive"
    hi "Also we need to figure it out how to add smooth effects, like in DDLC"
    ra "Yeah.. We are moving too fast..."

    return
