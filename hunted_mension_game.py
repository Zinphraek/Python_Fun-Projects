import copy, random

def get_target_room_list(room_list, excluded_rooms):
    return [room for room in room_list if room not in excluded_rooms]


def initialize_rooms_content(item_list, room_list):
    rooms_content = {}
    random.shuffle(item_list)
    rooms = get_target_room_list(room_list, ["Basement", "Entrance Hall"])
    for i, room in enumerate(rooms):
        rooms_content[room] = {
            "item": item_list[i] if i < len(item_list) else None,
            "cockroaches": 0,
            "bug_spray": 0,
            "map": False,
            "bug_nest": False,
            "mango": False
        }
    # Entrance Hall always holds the Map relocator as a pressable button.
    rooms_content["Entrance Hall"] = {
        "item": "Map relocator",
        "cockroaches": 0,
        "bug_spray": 0,
        "map": False,
        "bug_nest": False,
        "mango": False
    }

    rooms_content["Basement"] = {
        "item": "Map relocator",
        "cockroaches": 0,
        "bug_spray": 0,
        "map": False,
        "bug_nest": False,
        "mango": False
    }
    return rooms_content


def place_initial_map(rooms_content):
    """
    Randomly selects a room (excluding Entrance Hall) and places the map there.
    """
    available_rooms = get_target_room_list(list(rooms_content.keys()), ["Entrance Hall", "Basement"])
    if available_rooms:
        random.shuffle(available_rooms)
        selected_room = available_rooms[len(available_rooms) // 2]
        rooms_content[selected_room]["map"] = True
        print("The mansion owner was forgetful and couldn't remember where the map is located. "
              "Perhaps you can use the Map relocator button at the Entrance Hall to help find it.\n")
        return selected_room
    else:
        print("No available room to place the map.")
        return None


def add_bug_nest_and_mangoes(rooms_content):
    rooms = get_target_room_list(list(rooms_content.keys()), ["Entrance Hall", "Basement"])
    random.shuffle(rooms)
    mid_point = len(rooms) // 2
    bug_nest_room = rooms[mid_point]
    rooms_content[bug_nest_room]["bug_nest"] = True
    mangoes_count = 2
    while mangoes_count > 0:
        random.shuffle(rooms)
        candidate_room = rooms[len(rooms) // 2]
        if candidate_room != bug_nest_room and not rooms_content[candidate_room]["mango"]:
            rooms_content[candidate_room]["mango"] = True
            mangoes_count -= 1


def distribute_bug_spray(rooms_content, cockroach_count, bug_spray_count):
    rooms = get_target_room_list(list(rooms_content.keys()), ["Entrance Hall", "Basement"])
    spray_to_bug_ratio = bug_spray_count if cockroach_count < 1 else bug_spray_count / cockroach_count
    while spray_to_bug_ratio < 1.25:
        random.shuffle(rooms)
        mid_point = len(rooms) // 2
        if (rooms_content[rooms[mid_point]]["cockroaches"] == 0 and
            rooms_content[rooms[mid_point]]["bug_spray"] == 0):
            rooms_content[rooms[mid_point]]["bug_spray"] += 1
            bug_spray_count += 1
            spray_to_bug_ratio = bug_spray_count if cockroach_count < 1 else bug_spray_count / cockroach_count
        else:
            break
    return bug_spray_count


def get_next_room(current_room, direction, room_map):
    """Return the next room given the current room and a direction."""
    if direction in room_map[current_room]:
        return room_map[current_room][direction]
    else:
        return None


def spawn_cockroaches(rooms_content, is_cockroach_nest_active, cockroach_count, current_room):
    rooms = get_target_room_list(list(rooms_content.keys()), ["Entrance Hall", "Basement"])
    if is_cockroach_nest_active and cockroach_count < 2:
        while cockroach_count < 5:
            random.shuffle(rooms)
            mid_point = len(rooms) // 2
            if rooms[mid_point] != current_room and rooms_content[rooms[mid_point]]["cockroaches"] == 0:
                rooms_content[rooms[mid_point]]["cockroaches"] += 1
                cockroach_count += 1
            else:
                break
    return cockroach_count


def relocate_mansion_map(rooms_content, inventory):
    """
    Relocates the map to a new room (excluding Entrance Hall).
    If the map is currently placed somewhere, it is removed from there.
    """
    current_map_location = None
    if inventory['map']:
        print("You have already collected the map🗺️, there is no need to press the button.")
        return None
    else:
        for room, content in rooms_content.items():
            if content.get("map", False):
                current_map_location = room
                break
        available_rooms = get_target_room_list(list(rooms_content.keys()), ["Entrance Hall", "Basement"])
        if current_map_location in available_rooms:
            available_rooms.remove(current_map_location)
        if available_rooms:
            random.shuffle(available_rooms)
            new_location = available_rooms[len(available_rooms) // 2]
            rooms_content[new_location]["map"] = True
            if current_map_location and current_map_location != new_location:
                rooms_content[current_map_location]["map"] = False
            print("The map has been relocated.")
            return new_location
        else:
            print("No available room to relocate the map.")
            return None


def show_map(current_room, game_map, inventory):
    map_copy = copy.deepcopy(game_map)
    if inventory["map"]:
        print(map_copy.replace(current_room, f'** {current_room} **'))
    else:
        print("🤔💭 Hummm... The map 🗺️ hasn't been collected yet.\n")


def show_inventory(inventory):
    items_display = list(inventory['items'])
    if inventory.get("mangoes", 0) > 0:
        items_display.append(f"{inventory['mangoes']} mighty healing mangoes 🥭")
    if inventory.get("bug_spray", 0) > 0:
        items_display.append(f"{inventory['bug_spray']} bug spray bottles🧴")
    if inventory.get("map", False):
        items_display.append("The mension map 🗺️")
    print("\nYour Inventory:")
    for i, item in enumerate(items_display):
        print(f"{i + 1}. {item}")


def try_collect_item(room, rooms_content, inventory):
    if room in rooms_content and rooms_content[room]["item"] is not None:
        item = rooms_content[room]["item"]
        print("You see the", item if room != 'Entrance Hall' else 'Relocate map button', "here.")
        answer = input(f"Do you want to { 'pick it up' if room != 'Entrance Hall' else 'press it' }? (Y/N): ").upper()
        while answer not in ["Y", "N"]:
            answer = input("Invalid input. Please enter Y or N: ").upper()
        if answer == "Y":
            if room != "Entrance Hall":
                inventory["items"].append(item)
                rooms_content[room]["item"] = None
                print(f"You picked up the", item, "and added it to your inventory.")
            else:
                print("You pressed the Relocate map button.")
                relocate_mansion_map(rooms_content, inventory)
        else:
            print(f"You chose not to {f'pick it up the {item}' if room != 'Entrance Hall' else 'press the Map relocator button' } right now.")
    else:
        print("There is no item to collect in", room, ".")


def try_collect_bug_spray_or_mango(room, item, rooms_content, inventory):
    if room in rooms_content and rooms_content[room].get(item, False):
        print(f"You see a {'mango 🥭' if item == 'mango' else 'bug spray 🧴'} here.")
        answer = input("Do you want to pick it up? (Y/N): ").upper()
        while answer not in ["Y", "N"]:
            answer = input("Invalid input. Please enter Y or N: ").upper()
        if answer == "Y":
            if item == 'mango':
                inventory['mangoes'] += 1
            else:
                inventory['bug_spray'] += 1
            rooms_content[room][item] = False
            print(f"You picked up the {'mango 🥭' if item == 'mango' else 'bug spray 🧴'} and added it to your inventory.\n")
        else:
            print(f"You chose not to pick up the {'mango 🥭' if item == 'mango' else 'bug spray 🧴'} right now.\n")
    else:
        print(f"There is no {'mango 🥭' if item == 'mango' else 'bug spray 🧴'} to collect in the", room, ".\n")


def try_collect_map(room, rooms_content, inventory):
    if room in rooms_content and rooms_content[room]["map"]:
        print("You see the map 🗺️ here.")
        answer = input("Do you want to pick it up? (Y/N): ").upper()
        while answer not in ["Y", "N"]:
            answer = input("Invalid input. Please enter Y or N: ").upper()
        if answer == "Y":
            inventory["map"] = True
            rooms_content[room]["map"] = False
            print("You picked up the map 🗺️ and added it to your inventory.\n")
        else:
            print("You chose not to pick up the map 🗺️ right now.\n")
    else:
        print("There is no map to collect in", room, ".")


def use_spray(room, rooms_content, inventory, cockroach_count, health_points, game_over):
    if rooms_content[room]["cockroaches"] > 0:
        if inventory["bug_spray"] > 0:
            inventory["bug_spray"] -= 1
            rooms_content[room]["cockroaches"] -= 1
            cockroach_count = max(0, cockroach_count - 1)
            print("🫡 Nicely done, that's one cockroach🪳 down.\n")
        else:
            print("\n😱 Bad luck, you are out of bug spray🧴.\nOh no 😨, you just lost 3 health points.")
            health_points -= 3
            if health_points <= 0:
                game_over = True
        return cockroach_count, health_points, game_over
    else:
        print("There are no bugs here to spray.")
        return cockroach_count, health_points, game_over

def destroy_bug_nest(room, rooms_content, inventory, health_points, is_cockroach_nest_active,  game_over):
    if rooms_content[room]["bug_nest"]:
        if "Rusty Wrench" in list(inventory["items"]):
            is_cockroach_nest_active = False
            rooms_content[room]["bug_nest"] = False
            print("🫡 Nicely done, you destroyed the nest 🪹. No new cockroach will be spawned.\n")
        else:
            print("\n😱 Bad luck, you haven't collected the Rusty Wrench🔧 yet.\nOh no 😨, you just lost 5 health points.")
            health_points -= 5
            if health_points <= 0:
                game_over = True

    return  health_points, is_cockroach_nest_active, game_over

def show_status(health_points, inventory):
    print(f"\nYour health status is {health_points}/20.\nYou have collected the following items:")
    for i, item in enumerate(inventory['items']):
        print(f"\t{i + 1}. {item}")


def consume_mango(health_points, inventory):
    if inventory["mangoes"] > 0:
        new_health = 20 if (health_points + 10) > 20 else health_points + 10
        inventory["mangoes"] -= 1
        print("\nHumm yummy 🤗🤗🤗, this mango 🥭 was delicious.")
        return new_health
    else:
        print("Oh noo, 😥 you are out of the delicious mighty mangoes.")
        return health_points


def add_bug_damage(health_points):
    print("Oh noo, 🥵 you just lost 3 health points.")
    return health_points - 3


def try_collecting_room_content(room, rooms_content, inventory):
    try_collect_bug_spray_or_mango(room, 'bug_spray', rooms_content, inventory)
    try_collect_bug_spray_or_mango(room, 'mango', rooms_content, inventory)
    try_collect_item(room, rooms_content, inventory)
    if not inventory["map"]:
        try_collect_map(room, rooms_content, inventory)


def show_instructions(menu):
    for k, v in menu.items():
        print(f"{k}: {v}")


def check_and_fight_bugs(room, rooms_content, inventory, cockroach_count, health_points, game_over, room_map):
    if rooms_content[room]["cockroaches"] > 0:
        print("\nWatch out🥶, there is a cockroach!")
        valid_action = False
        next_room = room
        while not valid_action:
            user_input = input("Enter 'F' to fight or 'N', 'S', 'E', 'W' to run: ").upper()
            if user_input in ["N", "S", "E", "W"]:
                health_points = add_bug_damage(health_points)
                next_room_candidate = get_next_room(room, user_input, room_map)
                if next_room_candidate is None:
                    print("You cannot go that way from", room, ". Try a different direction.")
                    continue
                else:
                    next_room = next_room_candidate
                    valid_action = True
            elif user_input == 'F':
                cockroach_count, health_points, game_over = use_spray(room, rooms_content, inventory, cockroach_count, health_points, game_over)
                valid_action = True
            elif user_input == 'X':
                exit()
            else:
                print(f"{user_input} is not a valid entry.\nYou just lost 3 health points.")
                health_points = add_bug_damage(health_points)
        return next_room, cockroach_count, health_points, game_over
    else:
        return room, cockroach_count, health_points, game_over


def handle_user_input(current_room, user_input, game_over, inventory, game_map, menu, health_points, room_map, rooms_content):
    if user_input in ["N", "S", "E", "W"]:
        next_room = get_next_room(current_room, user_input, room_map)
        if next_room is None:
            print("You cannot go that way from", current_room, ". Try a different direction.")
            return current_room, health_points, game_over
        else:
            return next_room, health_points, game_over
    elif user_input == 'R':
        # Map relocator command, available only at Entrance Hall if the player has it.
        if current_room == "Entrance Hall":
                relocate_mansion_map(rooms_content)
        else:
            print("The Map relocator is only available at the Entrance Hall.")
        return current_room, health_points, game_over
    elif user_input == 'X':
        print("Thank you for playing")
        exit()
    elif user_input == 'H':
        show_map(current_room, game_map, inventory)
        return current_room, health_points, game_over
    elif user_input == 'M':
        show_instructions(menu)
        return current_room, health_points, game_over
    elif user_input == 'T':
        show_status(health_points, inventory)
        return current_room, health_points, game_over
    elif user_input == 'I':
        show_inventory(inventory)
        return current_room, health_points, game_over
    else:
        print("Invalid input.")
        return current_room, health_points, game_over


def main():
    # Initialize game state
    current_room = "Entrance Hall"  # starting room; no item here
    health_points = 20
    game_over = False
    is_cockroach_nest_active = True
    player_collected_all_items_and_was_informed = False
    cockroach_count = 0
    bug_spray_count = 0
    inventory = {"items": [], "bug_spray": 0, "map": False, "mangoes": 0}

    # Define the room connections
    room_map = {
        "Garage": {"E": "Restroom", "S": "Entrance Hall"},
        "Restroom": {"W": "Garage", "E": "Laundry Room", "S": "Living Room"},
        "Laundry Room": {"W": "Restroom", "E": "Basement"},
        "Basement": {"W": "Laundry Room"},
        "Entrance Hall": {"N": "Garage", "E": "Living Room"},
        "Living Room": {"W": "Entrance Hall", "E": "Dining Room", "N": "Restroom", "S": "Library"},
        "Dining Room": {"W": "Living Room", "N": "Kitchen"},
        "Kitchen": {"S": "Dining Room"},
        "Bedroom": {"E": "Library"},
        "Library": {"W": "Bedroom", "E": "Study Room", "N": "Living Room"},
        "Study Room": {"W": "Library"}
    }

    # Mansion map (display map)
    game_map = """
    [Garage]  -----  [Restroom]  ---- [Laundry Room] ------ [Basement]
      |                  |
      |                  |               [Kitchen]
      |                  |                   |
[Entrance Hall] ---[Living Room] ------ [Dining Room]
                         |
                         |
[Bedroom]   ------   [Library]   ------ [Study Room]
    """

    # Items randomly dispatched around the mansion
    item_list = ["Rusty Wrench",
                 "Silver Comb",
                 "Forgotten Medallion",
                 "Vintage Portrait",
                 "Enchanted Goblet",
                 "Magic Ladle",
                 "Haunted Locket",
                 "Ancient Grimoire",
                 "Dusty Tome"]

    rooms_content = initialize_rooms_content(item_list, list(room_map.keys()))
    add_bug_nest_and_mangoes(rooms_content)
    # Place the map in a random room at the beginning of the game
    place_initial_map(rooms_content)

    actions = {
        "N": "Move North",
        "S": "Move South",
        "E": "Move East",
        "W": "Move West",
        "I": "Show Inventory",
        "H": "Show Mansion Map (if collected)",
        "R": "Relocate Map (only in Entrance Hall)",
        "M": "Show Menu",
        "T": "Show Status",
        "X": "Exit Game"
    }

    show_instructions(actions)
    # Main game loop
    while not game_over:
        cockroach_count = spawn_cockroaches(rooms_content, is_cockroach_nest_active, cockroach_count, current_room)
        bug_spray_count = distribute_bug_spray(rooms_content, cockroach_count, bug_spray_count)

        print("\nYou are in", current_room)
        user_input = input("Enter a direction (N, S, E, W) or a command: ").upper()

        if user_input not in actions.keys():
            print("Invalid input. Please enter a valid command from the menu.")
            continue

        next_room, health_points, game_over = handle_user_input(
            current_room, user_input, game_over, inventory, game_map, actions, health_points, room_map, rooms_content)
        if next_room != current_room:
            current_room = next_room
            print("You moved to the", current_room)

        if rooms_content[next_room]["bug_nest"]:
            print("You entered the cockroaches 🪳 nest 🪹.\nYou need to destroy it with the *Rusty Wrench* 🔧 to keep it from producing more cockroaches 🪳.\n")
            user_input = input("Enter 'F' to fight, or 'N', 'S', 'E', 'W' to run, or 'X' to exit the game: ").upper()
            while user_input not in ['E', 'F', 'N', 'S', 'W', 'X']:
                user_input = input("Enter 'F' to fight, or 'N', 'S', 'E', 'W' to run, or 'X' to exit the game: ").upper()

            if user_input == 'X':
                print()
            elif user_input == 'F':
                health_points, is_cockroach_nest_active, game_over = destroy_bug_nest(
                    next_room, rooms_content, inventory, health_points, is_cockroach_nest_active, game_over)
            else:
                next_room, health_points, game_over = handle_user_input(
                    current_room, user_input, game_over, inventory, game_map, actions, health_points, room_map,
                    rooms_content)



        if current_room == "Basement" and len(inventory['items']) < 9:
            print("You have entered the Basement and encountered The Shadow Keeper ☣☢️🔱🩻🔱☢️☣ before collecting all relics.")
            print("☠️ NOM NOM...GAME OVER ☠️!\n Thanks for playing the game. Hope you enjoyed it.")
            game_over = True
            break

        if current_room == "Basement" and len(inventory['items']) >= 9:
            print("The Shadow Keeper ☣☢️🔱🩻🔱☢️☣ is lurking in this room. But don't worry you are unbeatable.")
            user_answer = input("Press 'A' to annilate it, or 'X' to exit teh game: ").upper()
            while user_answer not in ['A', 'X']:
                print("Invalid entry.")
                user_answer = input("Press 'A' to annilate it, or 'X' to exit teh game. ").upper()

            print(f"{"🫡🫡🫡. Congratulation you have sucessfully defeated the Shadow Keeper ☣☢️🔱🩻🔱☢️☣." if user_answer == 'A' else ""}\nThank you for playing 🫡🤗🫡. Hope you enjoyed.")
            game_over = True
            break

        try_collecting_room_content(current_room, rooms_content, inventory)
        current_room, cockroach_count, health_points, game_over = check_and_fight_bugs(
            current_room, rooms_content, inventory, cockroach_count, health_points, game_over, room_map)

        if health_points < 7:
            print(f"You are low on health points ({health_points}). Do you want to restore it? (Y/N)")
            user_answer = input().upper()
            if user_answer == 'Y':
                health_points = consume_mango(health_points, inventory)

        if len(inventory['items']) == 9:
            if not player_collected_all_items_and_was_informed:
                print("Congratulations! You have collected all relics.")
                print("Now, you may safely explore or even confront the curse.")
                player_collected_all_items_and_was_informed = True

if __name__ == "__main__":
    main()
