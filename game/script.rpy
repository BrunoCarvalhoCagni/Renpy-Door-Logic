# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    scene bg black

    "{i} Escolha uma das portas {/i}"

    jump highlight_doors_dialog


    return

label highlight_doors_dialog:
    call screen highlight_doors
    return

label dialog_door_1:
    
    "Door 1"
    jump highlight_doors_dialog

    return

label dialog_door_2:
    
    "Door 2"
    jump highlight_doors_dialog

    return

label dialog_door_3:
    
    "Door 3"
    jump highlight_doors_dialog

    return

label dialog_door_4:
    
    "Door 4"
    jump highlight_doors_dialog

    return
