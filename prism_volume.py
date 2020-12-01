#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on November 2020
# This program calculates the volume of a
#    square-based prism with user inputted dimensions


def main():
    # this function calculates volume

    # input
    square_length = int(input("Enter square length (cm):"))
    prism_height = int(input("Enter prism_height (cm):"))

    # process
    base_area = square_length**2
    volume = base_area*prism_height

    # output
    print("")
    print("The volume is {} cm²".format(volume))


if __name__ == "__main__":
    main()
