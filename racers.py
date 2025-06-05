def non_winners(races):
    # Write your solution here!
    # pass

    # create a winners_set include
        # loop thorugh the values in the races, add tutple[0] to the set

    # output = set()
    # loop through person 
        # start second element of tuple 
        # if it it not in the winners_set, add output
    
    # return output

    winners_set = set()

    for winners in races.values():
        winners_set.add(winners[0])
    
    output = set()

    for winners in races.values():
        for i in range(1, len(winners)):
            if winners[i] not in winners_set:
                output.add(winners[i])

    print(output)
    return output


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