#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: March 2022
# This program calculates perimeter of octagon with user input


def main():
    # this funcation tells you the perimeter of octagon

    # input
    one_side_measurement = int(input("Enter one side measurement(cm):"))
    print("")

    # process
    perimeter = 8 * one_side_measurement

    # output
    print("")
    print("Perimeter is {} cm".format(perimeter))
    print("\nDone.")


if __name__ == "__main__":
    main()
