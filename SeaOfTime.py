def start_game():
    print("You have washed ashore the Sea of Time...")
    print("After many seasons of exploring the island, you have just discovered a mystical artifact while sheltering in a cave.")
    print("This artifact allows you to travel through time, and communicate with the land's ancestors. Your goal is to find the legendary treasure of the Seven Seas.")
    first_choice()

def first_choice():
    print("\nYou stand at the edge of a cliff with the artifact in your hand.")
    print("1. Use the artifact to travel to the past.")
    print("2. Use the artifact to travel to the future.")
    choice = input("What do you do? (1/2): ")

    if choice == '1':
        travel_past()
    elif choice == '2':
        travel_future()
    else:
        print("Invalid choice. Please select 1 or 2.")
        first_choice()

def travel_past():
    print("\nYou travel to the past and find yourself at a bustling shop at the edge of the sea.")
    print("1. Visit the tavern to gather information.")
    print("2. Head to the docks to find a map.")
    choice = input("What do you do? (1/2): ")

    if choice == '1':
        visit_tavern()
    elif choice == '2':
        head_to_docks()
    else:
        print("Invalid choice. Please select 1 or 2.")
        travel_past()

def travel_future():
    print("\nYou travel to the future and find yourself in a high-tech city.")
    print("1. Visit the library to research the treasure's location.")
    print("2. Find a local hacker to help you decode ancient maps.")
    choice = input("What do you do? (1/2): ")

    if choice == '1':
        visit_library()
    elif choice == '2':
        find_hacker()
    else:
        print("Invalid choice. Please select 1 or 2.")
        travel_future()

def visit_tavern():
    print("\nAt the tavern, you hear rumors about a hidden cave with clues to the treasure.")
    print("1. Follow the rumors to the cave.")
    print("2. Bribe a local for more precise information.")
    choice = input("What do you do? (1/2): ")

    if choice == '1':
        follow_rumors()
    elif choice == '2':
        bribe_local()
    else:
        print("Invalid choice. Please select 1 or 2.")
        visit_tavern()

def head_to_docks():
    print("\nAt the docks, you find an old mapmaker who offers you a map in exchange for a favor.")
    print("1. Agree to do the favor.")
    print("2. Refuse and try to steal the map.")
    choice = input("What do you do? (1/2): ")

    if choice == '1':
        do_favor()
    elif choice == '2':
        steal_map()
    else:
        print("Invalid choice. Please select 1 or 2.")
        head_to_docks()

def visit_library():
    print("\nAt the library, you find records of a legendary treasure guarded by a time-traveling guardian.")
    print("1. Research the guardian's weakness.")
    print("2. Look for the treasure's exact location.")
    choice = input("What do you do? (1/2): ")

    if choice == '1':
        research_weakness()
    elif choice == '2':
        find_location()
    else:
        print("Invalid choice. Please select 1 or 2.")
        visit_library()

def find_hacker():
    print("\nThe hacker agrees to help you decode the ancient maps in exchange for a piece of the treasure.")
    print("1. Agree to the deal.")
    print("2. Threaten the hacker to get the information for free.")
    choice = input("What do you do? (1/2): ")

    if choice == '1':
        agree_deal()
    elif choice == '2':
        threaten_hacker()
    else:
        print("Invalid choice. Please select 1 or 2.")
        find_hacker()

def follow_rumors():
    print("\nFollowing the rumors, you find the hidden cave and inside it, clues to the treasure's location.")
    print("1. Decipher the clues yourself.")
    print("2. Return to the present and use modern technology to help.")
    choice = input("What do you do? (1/2): ")

    if choice == '1':
        decipher_clues()
    elif choice == '2':
        use_technology()
    else:
        print("Invalid choice. Please select 1 or 2.")
        follow_rumors()

def bribe_local():
    print("\nThe local gives you a detailed map leading directly to the treasure.")
    print("1. Follow the map.")
    print("2. Cross-check the map with other sources.")
    choice = input("What do you do? (1/2): ")

    if choice == '1':
        follow_map()
    elif choice == '2':
        cross_check()
    else:
        print("Invalid choice. Please select 1 or 2.")
        bribe_local()

def do_favor():
    print("\nYou complete the favor and receive a map. The map leads you to a guarded island.")
    print("1. Plan a stealthy approach to the island.")
    print("2. Attack the guards head-on.")
    choice = input("What do you do? (1/2): ")

    if choice == '1':
        stealthy_approach()
    elif choice == '2':
        head_on_attack()
    else:
        print("Invalid choice. Please select 1 or 2.")
        do_favor()

def steal_map():
    print("\nYou try to steal the map but get caught and thrown into a jail cell.")
    print("The adventure ends here. Better luck next time!")
    play_again()

def research_weakness():
    print("\nYou find the guardian's weakness and prepare to face it.")
    print("1. Confront the guardian in the future.")
    print("2. Return to the past to gather more allies.")
    choice = input("What do you do? (1/2): ")

    if choice == '1':
        confront_guardian()
    elif choice == '2':
        gather_allies()
    else:
        print("Invalid choice. Please select 1 or 2.")
        research_weakness()

def find_location():
    print("\nYou discover the treasure's exact location in the future.")
    print("1. Head directly to the treasure.")
    print("2. Set traps to protect yourself from potential threats.")
    choice = input("What do you do? (1/2): ")

    if choice == '1':
        head_to_treasure()
    elif choice == '2':
        set_traps()
    else:
        print("Invalid choice. Please select 1 or 2.")
        find_location()

def agree_deal():
    print("\nThe hacker helps you decode the map and reveals the treasure's location.")
    print("1. Go to the treasure's location with the hacker.")
    print("2. Double-cross the hacker and go alone.")
    choice = input("What do you do? (1/2): ")

    if choice == '1':
        go_with_hacker()
    elif choice == '2':
        go_alone()
    else:
        print("Invalid choice. Please select 1 or 2.")
        agree_deal()

def threaten_hacker():
    print("\nThe hacker refuses to help you and alerts the authorities.")
    print("The adventure ends here. Better luck next time!")
    play_again()

def decipher_clues():
    print("\nYou successfully decipher the clues and find the treasure in the past!")
    print("Congratulations, you have completed the adventure!")
    play_again()

def use_technology():
    print("\nUsing modern technology, you easily find the treasure.")
    print("Congratulations, you have completed the adventure!")
    play_again()

def follow_map():
    print("\nYou follow the map and find the treasure hidden on a remote island.")
    print("Congratulations, you have completed the adventure!")
    play_again()

def cross_check():
    print("\nCross-checking the map, you find inconsistencies and realize it's a trap.")
    print("You narrowly escape and the adventure continues.")
    print("1. Search for more reliable information.")
    print("2. Confront the person who gave you the map.")
    choice = input("What do you do? (1/2): ")

    if choice == '1':
        search_more_info()
    elif choice == '2':
        confront_person()
    else:
        print("Invalid choice. Please select 1 or 2.")
        cross_check()

def stealthy_approach():
    print("\nYou sneak onto the island and find the treasure hidden in a cave.")
    print("Congratulations, you have completed the adventure!")
    play_again()

def head_on_attack():
    print("\nYou attack the guards head-on but are outnumbered and captured.")
    print("The adventure ends here. Better luck next time!")
    play_again()

def confront_guardian():
    print("\nArmed with the knowledge of its weakness, you defeat the guardian and claim the treasure.")
    print("Congratulations, you have completed the adventure!")
    play_again()

def gather_allies():
    print("\n
