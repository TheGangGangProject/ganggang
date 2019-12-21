# Characters
define ki = Character("Kiyoshi", image="kiyo",
                     who_color="#9be394")
define n = Character("Nico", image="nico",
                     who_color="#f09b5b")
define to = Character("Tohiro", image="tohi",
                     who_color="#5badf0")
define k = Character("Kosomos", image="kos",
                     who_color="#f59153")
define nvlk = Character("Kosomos", who_color="#f59153", kind=nvl)                     
define r = Character("Renato", image="ren",
                     who_color="#f59153")
define p = Character("Phillip", image="phi",
                     who_color="")

# Posistions/Transistions
transform charright:
       xalign 0.76
       yalign 0.65
transform charleft:
       xalign 0.24
       yalign 0.65
transform charmid:
       xalign 0.5
       yalign 0.65
define sceneswitch = Dissolve(.5)
define wipeinward = ImageDissolve("gradient reverse.png", 1.0, ramplen=128)
define wipedissolve = ImageDissolve("gradient.png", 1.0, ramplen=128)
define wipeweird = ImageDissolve("weird.png", 2.5, ramplen=250)
define wipeslide = ImageDissolve("swipe.png", 1.0, ramplen=128)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #Start on Black
    
    "I still look back on that day, the day I lost you."
    "The day I sacrificed my eyes for our love."  

    scene cg nico
    with wipeweird

    "I still sometimes see that bright smile of yours...{p=1}That smile drove me to madness."
    "It had been my destruction, yet also my drive."
    "I know that still, you exist somewhere on this god forsaken planet."
    "And no matter how far I have to go...{p=1}I will find you."
    scene black
    with wipeinward

    "I will find you...{p=1}Nico Chirskoy."

    scene cg teach
    with wipeinward

    "???" "This could revolutionize the medical industry. You could splice your self a new arm in the matter of hours!"
    "???" "This could be the key to immortality! Finally being able to get to the fountain of youth!"
    "???" "I see a future in this technology, and I hope you do too." 
    "???" "{p=1.5}This has been my speech, and thank you again for allowing me to talk to you all."
    "???" "Goodbye."
    "Board Member" "Wait, Mr.Bates!"
    "???" "Yes sir?"
    "Board Member" "Well, we would all like to compliment you on your presentation and your product."
    "???" "Well, why thank you!"
    "Board Member" "Yet, do you think you're going to go far with this endeavor, with your history and all."
    "???" "Time heals all wounds sir, but if people want to cling to faded scars...{p=1.0}I guess the fountain of youth will disappear once again."
    "???" "Now! If that is all you have for more, I will be leaving now."

    scene bg park
    with wipeslide

    show kos sad at charleft

    "???" "I hope they don't think less of me for that stoic crap..."
    "???" "I mean they complimented me and everything, that's means it was atleast somewhat a succsess."
    "???" "Ugghh, God I need to calm down."
    "He sits down on a metal park bench and lets out a large sigh."
    "???" "Remember what doc said, in and then out."

    nvlk "My name is Kaleb Bates. I'm a 32 year old man, currently trying to sell his medical ideas."
    nvlk "Although it's quite hard when people know you work with the mafia."
    nvlk "I was a high up in the Nekoyuza, the local gang that practically owns the place, where I was Kosomos. That's what's most people call me nowadays."

 







    return
