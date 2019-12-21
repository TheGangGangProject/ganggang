# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nash", image="nasher",
                     who_color="#D7C2A0")
define k = Character("Kiyoshi", image="kiyo",
                     who_color="#03fc84")
define t = Character("Tohiro", image="tohi",
                     who_color="#2e5fdb")
transform player:
       xalign 0
       yalign 0.65
transform charleft:
       xalign 0.76
       yalign 0.65
transform charright:
       xalign 0.24
       yalign 0.65
transform charmid:
       xalign 0.5
       yalign 0.65
#define wipeleft = ImageDissolve("left.png", 1.0, ramplen=128)
# The game starts here.

label prefix:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bgroom.jpg") to the
    # images directory to show it.

label start:

    scene bg cityscape


    "Morioh, a small town on the edge of Japan.\n "
jump meat


label meat:
   


    return