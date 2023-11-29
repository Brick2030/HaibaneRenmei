# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# In this file transforming settings are defined to place objects on the scene                #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Found out that changing z changes size of characters. Z = 1.2 changes them to a perfect size. 

transform leftin(x=640, z=1.20):
    xcenter -400 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x


# This transform hides the character by moving them to the left.
transform rhide:
    subpixel True
    on hide:
        easeout .25 xcenter 2000





transform TEST():
#    easein 0.25 xcenter x
#    alpha 1.00 subpixel True
#    ease 0.25 xalign x


transform left2:
    zoom 1.2*1.00 alpha 1.00 subpixel True
    xalign 0.0
    yalign 1.0
    TEST
    
    
transform left1:
    zoom 1.2*1.00 alpha 1.00 subpixel True
    xalign 0.25
    yalign 1.0
    TEST
    
transform centre:
    zoom 1.2*1.00 alpha 1.00 subpixel True
    xalign 0.5
    yalign 1.0
    TEST

transform right1:
    zoom 1.2*1.00 alpha 1.00 subpixel True
    xalign 0.75
    yalign 1.0
    TEST
    
transform right2:
    zoom 1.2*1.00 alpha 1.00 subpixel True
    xalign 1.0
    yalign 1.0
    TEST


