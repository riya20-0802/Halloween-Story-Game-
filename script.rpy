# Backgrounds and Sprites
image bg patch = Transform("images/bg_patch.png", size=(1920, 1080))
image bg shop = Transform("images/bg_shop.png", size=(1920, 1080))
image bg party = Transform("images/bg_party.png", size=(1920, 1080))

image mochi neutral = Transform("images/mochi_neutral.png", zoom=1.2)
image spook scared = Transform("images/spook_scared.png", zoom=1.5, ypos=0.40)
image luna potion = Transform("images/luna_potion.png", zoom=2.0, yanchor=1.0, ypos=0.85)
image luna wand = Transform("images/luna_wand.png", zoom=2.2, yanchor=1.0, ypos=0.85)
image mochi pumpkin = Transform("images/mochi_pumpkin.png", zoom=0.3, yanchor=1.0, ypos=0.9)

# Characters
define m = Character("Mochi", color="#a2d2ff")
define s = Character("Spook", color="#ffc6ff")
define l = Character("Luna", color="#bdb2ff")
define player = Character("[player_name]", color="#b5e2fa")

label start:
    python:
        player_name = renpy.input("Enter your detective name:", default="Riya")
        player_name = player_name.strip()
        if not player_name:
            player_name = "Riya"

    scene bg patch
    with fade 

    "It's 11 pm on Halloween Eve."
    "You walked up to the pumpkin patch to check on the giant festival pumpkin..."

    "Except it's GONE!"
    "All that's left is a giant pile of pink glitter and a half-eaten candy corn."

    show spook scared:
        xalign 0.5
        yalign 0.35
    with dissolve 

    s "Eek! [player_name]! It disappeared! I turned my back for TWO SECONDS to chase a butterfly and it just went POOF!"
    player "Spook, calm down! Did you see anyone suspicious?"
    s "Well, Mochi was sneaking around the fence and Luna was testing her glowing potions nearby!"

    menu:
        "Who do you want to question first?"

        "Interrogate Mochi the Cat":
            jump talk_mochi

        "Check out Luna's potion shop":
            jump talk_luna

# Option A: Mochi the Cat
label talk_mochi:
    scene bg patch 
    show mochi neutral:
        xalign 0.5
        yalign 0.45
        xanchor 0.5
        yanchor 0.5
    with dissolve

    m "Meow! If you're going to interrogate me, it better come with some tuna."
    player "Mochi, why were you near the giant pumpkin right before it vanished?"
    m "I was following Luna! She was carrying a glowing pink potion and mumbling about making the pumpkin floating-size."
    m "She dropped a trail of glitter heading straight toward her shop!"

    jump visit_shop

# Option B: Luna's Shop Directly
label talk_luna:
    scene bg shop
    with fade
    show luna potion:
        xalign 0.3
        yalign 0.45
    with dissolve

    l "Oh! Hey [player_name]! Don't step on that spilled potion, it'll make your shoes turn into bats!"
    player "Luna... did one of your spells go wrong again?"
    l "Ok, look, I tried to cast a levitation spell on the Giant Pumpkin so we could float it down the main street for the parade..."
    l "But... I accidentally used my shrinking potion instead! I'm sorry!"
    l "Now I can't find where it rolled under my messy workbench!"
    player "Wait, is that Mochi sitting on a pumpkin?!"
    l "Oh my gosh! There it is! That's the great pumpkin!...or the great little pumpkin hehe"

    jump resolve_mystery

# Scene 2: The Potion Shop Search
label visit_shop:

    scene bg shop
    with fade

    show luna potion:
        xalign 0.3
        yalign 0.45

    show mochi pumpkin:
        xalign 0.75
        yalign 0.45

    player "Luna! Mochi says you vanished the festival pumpkin!"

    l "I didn't mean to! My levitation spell backfired and shrank it down to the size of an apple!"
    
    show spook scared:
        xalign 0.15
        yalign 0.35
    with dissolve

    s "Wait... [player_name], look at Mochi!"
    s "Is he... sitting on it?!"

    m "What? It's the perfect height for a footrest."

    jump resolve_mystery

# Climax and Ending
label resolve_mystery:

    scene bg shop
    with fade

    show spook scared:
        xalign 0.15
        yalign 0.35

    show mochi pumpkin:
        xalign 0.78
        yalign 0.45
        zoom 0.8

    show luna wand:
        xalign 0.55
        yalign 0.45

    l "Hold still, Mochi! *Reversio Grandis!*"

    "Luna waves her wand, shooting a beam of sparkly purple light directly at the tiny pumpkin!"

    "POOF!"

    scene bg party
    with fade

    "The pumpkin expands back to its massive size, carrying the whole festival squad with it!"

    player "Another case closed!"
    "HAPPY HALLOWEEN!"

    return