#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: April 2021
# This program calculates the cost of a pizza

import constants


def main():
    # This function calculates the cost

    # Input
    diameter = (
        int(input("Enter the diameter of the pizza that you want (inches): "))
    )

    # Process
    sub_total = (
        constants.LABOR + constants.RENT + (diameter * constants.MATERIALS)
    )
    tax = sub_total * constants.HST
    total = sub_total + tax

    # Output
    print("")
    print(
        "The cost of a {0} inch pizza is: ${1:,.2f}.".format(diameter, total)
    )
    print("\nDone.")


if __name__ == "__main__":
    main()
