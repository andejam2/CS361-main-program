# Create an empty list to store stops
trip_stops = []

# Welcome messages to the user
print("Welcome to the Road Trip Planner!")
print("This program lets you build and view a road trip itinerary.")

# Create a flag to control the menu loop
done = False

# Loop until the user chooses to quit
while done == False:

    # Show the main menu options
    print("1 - Add a stop")
    print("2 - View Itinerary")
    print("3 - Load example trip")
    print("4 - Quit")
    print()

    # Request user input
    choice = input("Please enter your selection: ")

    # User chooses to add a stop
    if choice == "1":
        stop = input("Enter the name of the stop: ")
        trip_stops.append(stop)

    # User chooses to view itinerary
    elif choice == "2":
        for stop in trip_stops:
            print(stop)

    # If the user chooses to load example trip
    elif choice == "3":
        trip_example_stops = ["Nashville, TN", "Louisville, KY", "Ashville, NC"]
        print(trip_example_stops)

    # If the user chooses to quit
    elif choice == "4":
        done = True
        print("Goodbye.")

    else:
        print("Invalid option. Please try again.")


