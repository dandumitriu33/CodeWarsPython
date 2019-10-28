def dirReduc(directions_list):
    counters = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "WEST": "EAST",
        "EAST": "WEST"
    }
    i = 0
    while i < len(directions_list) - 1:
        if directions_list[i] == counters[directions_list[i+1]]:
            del directions_list[i:i+2]
            i = 0
        else:
            i += 1
    return directions_list


print(dirReduc(['EAST', 'EAST', 'WEST', 'NORTH', 'WEST', 'EAST', 'EAST', 'SOUTH', 'NORTH', 'WEST']))