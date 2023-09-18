"""Counts stuff"""

def count(sequence, item):
    """ Stuff thats being counted"""
    number = 0
    for thing in sequence:
        if thing == item:
            number += 1
            return number
        return None
