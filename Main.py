# Create an empty list to store stops
trip_stops = []

import sys

# Check for non-interactive mode
if len(sys.argv) > 1 and sys.argv[1] == "auto":
    trip_example_stops = [
        "Nashville, TN",
        "Louisville, KY",
        "Ashville, NC\n"
    ]
    print()
    print("Running in non-interactive mode...")
    print("Here is a sample trip itinerary:\n")
    for stop in trip_example_stops:
        print(stop)
    sys.exit()


# Welcome messages to the user
print()
print("Welcome to the Road Trip Planner!")
print("This program lets you quickly and easily build and view a road trip itinerary.\n")

# Create a flag to control the menu loop
done = False

# Loop until the user chooses to quit
while done == False:

    # Show the main menu options
    print()
    print("1 - Add a stop")
    print("2 - View Itinerary")
    print("3 - Load example trip")
    print("4 - Show Instructions")
    print("5 - Remove a stop")
    print("6 - Quit")
    print()

    # Request user input
    choice = input("Please enter your selection: ")

    # User chooses to add a stop
    if choice == "1":
        stop = input("Enter the name of the stop: ")
        note = input("Enter an optional note for this stop (press Enter to skip): ")
        trip_stops.append({"name": stop, "note": note})

    # User chooses to view itinerary
    elif choice == "2":
        if not trip_stops:
            print("Your itinerary is empty.")
        else:
            print("Your Road Trip Itinerary:")
            for stop in trip_stops:
                print(f"- {stop['name']}")
                if stop["note"]:
                    print(f"    Note: {stop['note']}")

    # If the user chooses to load example trip
    elif choice == "3":
        trip_example_stops = [
            {"name": "Knoxville, TN", "note": "Start of the trip, home of the Volunteers!"},
            {"name": "Louisville, KY", "note": "Visit bourbon distillery"},
            {"name": "Ashville, NC", "note": "Hike Blue Ridge"}
        ]
        print("Example trip itinerary:")
        print()
        for stop in trip_example_stops:
            print(f"- {stop['name']}")
            if stop["note"]:
                print(f"    Note: {stop['note']}")

    elif choice == "4":
        print("Step 1: Add stops to your trip")
        print("Step 2: View your itinerary")
        print("Step 3: Load and Example if you want inspiration")
        print("Step 4: Quit when you're done")
        print()

    elif choice == "5":
        stop_to_remove = input("Enter the name of the stop to remove: ")
        found = False
        for stop in trip_stops:
            if stop["name"].lower() == stop_to_remove.lower():
                trip_stops.remove(stop)
                print(f"{stop_to_remove} has been removed from your trip.")
                found = True
                break
        if not found:
            print("That stop was not found in your itinerary.")

    # If the user chooses to quit
    elif choice == "6":
        done = True
        print("Goodbye.")

    else:
        print("Invalid option. Please enter an option 1 - 6.")


