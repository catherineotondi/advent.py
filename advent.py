import random
import time

creature = ["dragon", "giant", "cobra", "chimpanzee"]
animal = random.choice(creature)
global weapon
weapon = "dagger"


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field, ")
    print_pause("filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked " + animal + " is ")
    print_pause("somewhere around here, and has been"
                " terrifying the nearby village. ")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)"
                "dagger.")


def player_decision_options():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    action_preference()


def action_preference():
    player_decision = user_answer("(Please enter 1 or 2).\n", ["1", "2"])

    if "1" in player_decision:
        house()
    elif "2" in player_decision:
        weapon_preference()
    else:
        print_pause("(Please enter 1 or 2)")


def user_answer(prompt, player_values):
    while True:
        player_decision = input(prompt).lower()
        if player_decision in player_values:
            return player_decision


def weapon_preference():
    global weapon
    print_pause("You peer cautiously in to the cave")
    if weapon == "sword":
        print_pause(
            "You've been here before and gotten all the good stuff."
            + " It's just an empty cave now"
        )
    else:
        print_pause("It turns out to be only a very small cave")
        print_pause("Your eye catches a glint of metal behind the rock")
        print_pause("You have found the magical sword of Ogoroth")
        print_pause("You discard your silly old dagger"
                    "and take the sword with you")
        weapon = "sword"
    print_pause("You walk back out to the field")
    player_decision_options()


def house():
    print_pause("You approached the door of the house.")
    print_pause(
        "You are about to knock when the door opens"
        " and steps out a" + " " + animal + " " + "."
    )
    print_pause("Eep! This the" + " " + animal + "'s" + " " + "house!")
    print_pause("The" + " " + animal + " " + "attacks you")
    print_pause(
        "You feel a bit under-prepared for this,"
        "what with only having a dagger"
    )
    run_fight()


def field():
    print_pause(
        "You run back in to the field."
        "Luckily, you dont seem to have been followed"
    )
    player_decision_options()


def fight():
    if weapon == "sword":
        print_pause(
            "As the " + animal + " moves to attack you,"
            "you unleash your new " + weapon + "."
        )
        print_pause(
            "The " + weapon + " of Ogoroth shines brightly in your hand"
            " as you brace yourself for attack."
        )
        print_pause(
            "But the " + animal + " takes one look at"
            "your shinning new toy and runs away"
        )
        print_pause("You have rid the town of the "
                    + animal + ". You are victorious!")

    else:
        print_pause("You tried your best.")
        print_pause("But your " + weapon + " is no match"
                    "for the " + animal + ".")
        print_pause("You have been defeated")
    start_playGame()


def run_fight():
    player_decision = user_answer("Would you like to"
                                  "(1)fight or" "(2)run away?\n", ["1", "2"])
    if "1" in player_decision:
        fight()
    elif "2" in player_decision:
        field()
    else:
        print_pause("(Please enter 1 or 2)")


def start_playGame():
    player_decision = user_answer("Would you like to play the"
                                  "game again? (y/n)", ["y", "n"])
    if "y" in player_decision:
        print_pause("Excellent! Restarting the game\n")
        enjoy_game()
    elif "n" in player_decision:
        finish_game()
    else:
        print_pause("Please enter (y/n)")


def finish_game():
    print_pause("Thank you, see you next time")


def enjoy_game():
    intro()
    player_decision_options()


enjoy_game()
