# this solution includes larger squares of wasted walking
# not just North <> South

def directions_reduction(directions_list):
    directions_dictionary = {
        "NORTH": [1, 0],
        "SOUTH": [-1, 0],
        "EAST": [0, 1],
        "WEST": [0, -1]
    }
    print(directions_dictionary["NORTH"])
    k = 0
    while k < len(directions_list):
        pos = [0, 0]
        temp_pos = pos
        i = 0
        while i < len(directions_list):
            temp_pos[0] = temp_pos[0] + directions_dictionary[directions_list[i]][0]
            temp_pos[1] = temp_pos[1] + directions_dictionary[directions_list[i]][1]
            if temp_pos == [0, 0]:
                del directions_list[:i+1]
                print(directions_list)
                i = 0
            else:
                i += 1
        k += 1
    print(directions_list)
    return directions_list

print(directions_reduction(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST",
                            "NORTH", "WEST"]))
