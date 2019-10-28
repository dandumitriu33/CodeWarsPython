def connect_four(moves):
    dict_slots = {
        'A1':[1,1], 'B1':[1,2], 'C1':[1,3], 'D1':[1,4], 'E1':[1,5], 'F1':[1,6], 'G1':[1,7],
        'A2':[2,1], 'B2':[2,2], 'C2':[2,3], 'D2':[2,4], 'E2':[2,5], 'F2':[2,6], 'G2':[2,7],
        'A3':[3,1], 'B3':[3,2], 'C3':[3,3], 'D3':[3,4], 'E3':[3,5], 'F3':[3,6], 'G3':[3,7],
        'A4':[4,1], 'B4':[4,2], 'C4':[4,3], 'D4':[4,4], 'E4':[4,5], 'F4':[4,6], 'G4':[4,7],
        'A5':[5,1], 'B5':[5,2], 'C5':[5,3], 'D5':[5,4], 'E5':[5,5], 'F5':[5,6], 'G5':[5,7],
        'A6':[6,1], 'B6':[6,2], 'C6':[6,3], 'D6':[6,4], 'E6':[6,5], 'F6':[6,6], 'G6':[6,7]
    }
    A = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
    B = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6']
    C = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']
    D = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6']
    E = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6']
    F = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6']
    G = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6']


    def check_win(plist):
        for i in plist:
            y = i[0]
            x = i[1]
            if [y,x-1] in plist and [y,x-2] in plist and [y,x-3] in plist:
                return 'win'
            elif [y,x+1] in plist and [y,x+2] in plist and [y,x+3] in plist:
                return 'win'
            elif [y-1,x] in plist and [y-2,x] in plist and [y-3,x] in plist:
                return 'win'
            elif [y+1,x] in plist and [y+2,x] in plist and [y+3,x] in plist:
                return 'win'
            elif [y-1,x-1] in plist and [y-2,x-2] in plist and [y-3,x-3] in plist:
                return 'win'
            elif [y+1,x-1] in plist and [y+2,x-2] in plist and [y+3,x-3] in plist:
                return 'win'
            elif [y-1,x+1] in plist and [y-2,x+2] in plist and [y-3,x+3] in plist:
                return 'win'
            elif [y+1,x+1] in plist and [y+2,x+2] in plist and [y+3,x+3] in plist:
                return 'win'

    # placement section

    red_placements = []
    yellow_placements = []
    for i in moves:
        if i[2:] == 'Red':
            if i[0] == 'A':
                red_placements.append(dict_slots[A.pop()])
            if i[0] == 'B':
                red_placements.append(dict_slots[B.pop()])
            if i[0] == 'C':
                red_placements.append(dict_slots[C.pop()])
            if i[0] == 'D':
                red_placements.append(dict_slots[D.pop()])
            if i[0] == 'E':
                red_placements.append(dict_slots[E.pop()])
            if i[0] == 'F':
                red_placements.append(dict_slots[F.pop()])
            if i[0] == 'G':
                red_placements.append(dict_slots[G.pop()])
            if check_win(red_placements) == 'win':
                return 'Red'
                exit()
        elif i[2:] == 'Yellow':
            if i[0] == 'A':
                yellow_placements.append(dict_slots[A.pop()])
            if i[0] == 'B':
                yellow_placements.append(dict_slots[B.pop()])
            if i[0] == 'C':
                yellow_placements.append(dict_slots[C.pop()])
            if i[0] == 'D':
                yellow_placements.append(dict_slots[D.pop()])
            if i[0] == 'E':
                yellow_placements.append(dict_slots[E.pop()])
            if i[0] == 'F':
                yellow_placements.append(dict_slots[F.pop()])
            if i[0] == 'G':
                yellow_placements.append(dict_slots[G.pop()])
            if check_win(yellow_placements) == 'win':
                return 'Yellow'
                exit()
    return 'Draw'
    exit()      
            
print(connect_four(["F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red", 
"B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red", 
"F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red", 
"A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red", 
"B_Yellow", "B_Red"
]))
