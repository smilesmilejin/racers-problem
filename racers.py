def non_winners(races):
    # Set to hold all drivers present in the dictionary
    all_drivers = set()
    # Set to hold drivers who won at least one race
    winners = set()
    
    for podium in races.values():
        # Add each driver to set of all drivers
        all_drivers.add(podium[0])
        all_drivers.add(podium[1])
        all_drivers.add(podium[2])

        # Only add the winner to the set of winners
        winners.add(podium[0])

    # Set to hold drivers who never won
    non_winners = set()

    for driver in all_drivers:
        if driver not in winners:
            non_winners.add(driver)
            
    return non_winners

races_1 = {
    "Suzuka": ("Tsunoda", "Latifi", "Stroll"),
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
    "Silverstone": ("Hamilton", "Latifi", "Tsunoda")
}
assert non_winners(races_1) == {"Latifi", "Stroll"}

races_2 = {
    "Mexico City": ("Pérez", "Hamilton", "Tsunoda"),
}
assert non_winners(races_2) == {"Hamilton", "Tsunoda"}

races_3 = {
    "Monaco": ("Leclerc", "Verstappen", "Sainz"),
    "Barcelona": ("Sainz", "Verstappen", "Leclerc"),
    "Zandvoort": ("Verstappen", "Sainz", "Leclerc")
}
# If all drivers present in the dictionary won a race
# then the return value should be an empty set
assert non_winners(races_3) == set()
print("All tests passed! Discuss time/space complexity if time remains")

"""
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------

Q: What should I do if invalid input is passed in?
A: You can assume that the input will be valid.

Q: Does capitalization matter?
A: Yes, you the input is case-sensitive. You code should treat "Sainz" and "SAINZ" as two different people.

Q: Does the order of returned data matter?
A: The required return type is a set, and sets are unordered in Python.

Q: What if every driver won at least one race?
A: An empty set should be returned.

Q: Who is Auberon's favorite F1 driver?
A: Yuki Tsunoda.

--------------------------------------------------



---------Hints for struggling candidates----------

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and desrcibe how they would do it using only pen and paper

- If your candidate still has difficulty forming an approach, encourage them to first attempt to return a set of all drivers in the dicitionary, regardless of what position they finished in.

- If your candidate gets an error when they incorrectly try to initialize their set using {}, encourage them to look up how to initialize an empty set in Python.

-------------------------------------------------

"""