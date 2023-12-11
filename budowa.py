def get_multiple_values(n):
    values = input().strip().split(' ')
    for x in range(n):
        values[x] = int(values[x])
    return values


n, m = get_multiple_values(2)
while(n < 1 or n > 1500 or m < 1 or m > 2):
    print('Podano nieprawidlowe wartosci. Sprobuj ponownie.')
    n, m = get_multiple_values(3)

airport = []
for i in range(n):
    row = input()
    while len(row) != n:
        print('Podano nieprawidlowa ilosc pol. Sprobuj ponownie.')
        row = input()
    airport.append([])
    for k in range(n):
        airport[i].append(row[k])

def copy_ap(airport):
    cp = []
    for i in range(len(airport)):
        cp.append([])
        for k in range(len(airport)):
            cp[i].append(airport[i][k])
    return cp

def check_field(airport, id, y, x, vertical, max_length, length=0):
    if length == max_length:
        return length
    good = True
    if airport[y][x] != '.':
        good = False
    else:
        allowed_surr = '.X'+id
        if y - 1 >= 0:
            if airport[y-1][x] not in allowed_surr:
                good = False
        if y + 1 < len(airport):
            if airport[y+1][x] not in allowed_surr:
                good = False
        if x - 1 >= 0:
            if airport[y][x-1] not in allowed_surr:
                good = False
        if x + 1 < len(airport):
            if airport[y][x+1] not in allowed_surr:
                good = False
    if good:
        airport[y][x] = id
        if vertical:
            if y + 1 < len(airport):
                return check_field(airport, id,  y + 1, x, vertical, max_length, length=length+1)
            else:
                return length + 1
        else:
            if x + 1 < len(airport):
                return check_field(airport, id, y, x + 1, vertical, max_length, length=length+1) 
            else:
                return length + 1
    return length

print()

def print_ap(airport):
    for x in range(n):
        s = ''
        for y in range(n):
            s += airport[x][y]
        print(s)


max_length = 0
for y in range(n):
    for x in range(n):
        for l in range(1, n+1):
            airp1 = copy_ap(airport)
            v_length1 = check_field(airp1, '1', y, x, True, l)
            airp2 = copy_ap(airport)
            h_length1 = check_field(airp2, '1', y, x, False, l)
            if m == 2:
                for y2 in range(n):
                    for x2 in range(n):
                        airp11 = copy_ap(airp1)
                        v_length2 = check_field(airp11, '2', y2, x2, True, l)
                        airp12 = copy_ap(airp1)
                        h_length2 = check_field(airp12, '2', y2, x2, False, l)
                        if (v_length1 == v_length2 or v_length1 == h_length2) and v_length1 > max_length:
                            max_length = v_length1
                        airp21 = copy_ap(airp2)
                        v_length2 = check_field(airp21, '2', y2, x2, True, l)
                        airp22 = copy_ap(airp2)
                        h_length2 = check_field(airp22, '2', y2, x2, False, l)
                        if (h_length1 == v_length2 or h_length1 == h_length2) and h_length1 > max_length:
                            max_length = h_length1
            else:
                if v_length1 > h_length1:
                    if v_length1 > max_length:
                        max_length = v_length1
                else:
                    if h_length1 > max_length:
                        max_length = h_length1
            
print(max_length)