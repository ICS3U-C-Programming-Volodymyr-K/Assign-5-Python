#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 05, 19, 2025
# This program calculates volume of cylinder

import math


# Another function specifically made for calculation
def calculation(height, radius):
    # Calculates volume of cylinder
    volume = math.pi * radius ** 2 * height
    # Returns back the value of volume to original function
    return volume


def main():
    # prints welcoming message.
    print(
        "Hello, today this program shall calculate/find the volume of a right cylinder by obtaining its radius and height."
    )
    user_input = input("Do you want to calculate the volume of the right cylinder?")
    # Gets the input on question if user wants to calculate the volume.
    if user_input.lower() == "yes" or user_input.lower() == "yes.":
        # While true will make the code to go forever until the user will insert right input
        while True:
            # If the user's input will be yes it will execute specific section of code.
            height = input("Insert height of your cylinder.")
            radius = input("Insert radius of your cylinder.")
            # Gets both input for height and radius from the user
            try:
                # Checks if radius and height meets the requirements.
                radius = float(radius)
                height = float(height)
                if radius > 0 and height > 0:
                    # Calls a function
                    volume = calculation(height, radius)
                    print(f"Your volume is, {volume} m^3")
                    # This break is used to overcome infinite loop
                    break
                # if input is negative, will insert this input.
                else:
                    print("Your value should be positive.")
                    # This break is used to overcome infinite loop
                    break
            except Exception:
                print("The value should be a float and positive.")
    # If user says no on a first question.
    else:
        for counter in range(0, 5):
            # Gets the input once more in a loop
            user_input = input(
                "Do you want to calculate the volume of the right cylinder?"
            )
            counter = counter + 1
            if user_input.lower() == "yes" or user_input.lower() == "yes.":
                # Breaks the loop if the user says yes eventually
                print("Restart the code and say yes on first question.")
                break
        else:
            while True:
                # If the user's input will be yes it will execute specific section of code.
                height = input("Insert height of your cylinder.")
                radius = input("Insert radius of your cylinder.")
                # Gets both input for height and radius from the user
                try:
                    # Checks if radius and height meets the requirements.
                    radius = float(radius)
                    height = float(height)
                    if radius > 0 and height > 0:
                        # Calls a function
                        volume = calculation(height, radius)
                        print(f"Your volume is, {volume} m^3")
                        # This break is used to overcome infinite loop
                        break
                    # if input is negative, will insert this input.
                    else:
                        print("Your value should be positive.")
                        # This break is used to overcome infinite loop
                        break
                except Exception:
                    print("The value should be a float and positive.")


if __name__ == "__main__":
    main()
