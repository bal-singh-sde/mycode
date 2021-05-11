#!/usr/bin/env python3

weathers = [ "winter", "spring", "summer", "fall"]
yn = ["yes", "no"]

user_input = input("Please enter you favourite season(Winter, Spring, Summer, Fall): ").lower()
while user_input not in weathers:
    print("Please enter a valid season")
    user_input = input("Please enter you favourite season(Winter, Spring, Summer, Fall): ")

if user_input == weathers[0]:
    snow = input("Do you like snow?(yes or no): ").lower()
    while snow not in yn:
        print("Please enter a valid input:")
        snow = input("Do you like snow?(yes or no): ").lower()
    if snow == yn[0]:
        print("Best places to travel during snow season are: ")
        print("North pole,AK" + " -- " + "Yellowstone National Park,WY" + " -- " + "Colorado Springs, CO")
    else:
        print("Best places to travel during winter season are: ")
        print("Chiang Mai, Thailand" + " -- " + "Dolomites, Italy")

# spring
elif user_input == weathers[1]:
    print("Best places to travel during spring season are: ")
    print("Panama City Beach, FL" + " -- " + "Grand Cayman, Caribbean")

#summer
elif user_input == weathers[2]:
    print("Best places to travel during summer season are: ")
    print("San Diego,CA" + " -- " + "Paris" + " -- " + "Hawaii")

#fall
else:
    print("Best places to travel during fall season are: ")
    print("Bar Harbor, Maine" + " -- " + "Ozark National Forest, Arkansas" + " -- " + "Eastern Shore, Maryland")



