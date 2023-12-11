def read_two_values():
    v1, v2 = input().strip().split(' ')
    v1 = int(v1)
    v2 = int(v2)
    return v1, v2

n, m = read_two_values()
while(n < 1 or n > 100000 or m < 1 or n > min(n**2, 500000)):
    print('Podano nieprawidlowe wartosci. Sprobuj ponownie.')
    n, m = read_two_values()

class Board:
    def __init__(self, n):
        self.n = n
        self.buttons = []
        for x in range(n):
            self.buttons.append([])
            for y in range(n):
                self.buttons[x].append('')

    def get_row(self, r):
        return self.buttons[r]
    
    def get_column(self, c):
        column = []
        for x in range(self.n):
            for y in range(self.n):
                if y == c:
                    column.append(self.buttons[x][y])
        return column
    
    def is_field_empty(self, r, c):
        return self.buttons[r][c] == ''
    
    def add_button(self, i, r, c):
        self.buttons[r][c] = Button(i, r, c)

    def get_active_buttons(self):
        btns = []
        for x in range(n):
            row = self.get_row(x)
            btns += get_active_buttons(row)
        return btns
    
    def check_validity(self, r):
        if len(self.get_active_buttons()) == 0:
            return False
        for x in range(self.n):
            if len(get_active_buttons(self.get_row(x))) % 2 != r:
                return False
            if len(get_active_buttons(self.get_column(x))) % 2 != r:
                return False
        return True
            

def get_buttons(list):
    buttons = []
    for element in list:
        if isinstance(element, Button):
            buttons.append(element)
    return buttons

def get_active_buttons(list):
    buttons = []
    for element in list:
        if isinstance(element, Button) and element.active:
            buttons.append(element)
    return buttons

def get_inactive_buttons(list):
    buttons = []
    for element in list:
        if isinstance(element, Button) and not element.active:
            buttons.append(element)
    return buttons

class Button:
    def __init__(self, i, r, c):
        self.i = i
        self.r = r
        self.c = c
        self.active = False
        self.h_touched = False
        self.v_touched = False

board = Board(n)

for i in range(1, m + 1):
    r, c = read_two_values()
    while(True):
        if(r < 1 or r > n or c < 1 or c > n):
            print('Podano nieprawidlowe wartosci. Sprobuj ponownie.')
        elif not board.is_field_empty(r-1, c-1):
            print('To pole jest juz zajete. Sproboj ponownie.')
        else:
            break
        r, c = read_two_values()
    
    board.add_button(i, r-1, c-1)

solution = False
for r in range(2):
    if solution:
        break
    for x in range(n):
        for y in range(n):
            if not board.is_field_empty(x, y):
                row = board.get_row(x)
                btns_r = get_inactive_buttons(row)
                column = board.get_column(y)
                btns_c = get_inactive_buttons(column)

                if board.buttons[x][y].v_touched and board.buttons[x][y].h_touched:
                    board.buttons[x][y].active = True
                    if y + 1 < len(btns_r):
                        btns_r[y + 1].h_touched = True
                    if x + 1 < len(btns_c):
                        btns_c[x + 1].v_touched = True
                    continue
                if board.buttons[x][y].v_touched:
                    if len(btns_r) - 1 > -r:
                        if y + 1 < len(btns_r):
                            btns_r[y + 1].h_touched = True
                        board.buttons[x][y].active = True
                        continue
                if board.buttons[x][y].h_touched:
                    if len(btns_c) - 1 > -r:
                        if x + 1 < len(btns_c):
                            btns_c[x + 1].v_touched = True
                        board.buttons[x][y].active = True
                        continue
                        
                if len(btns_r) - 1 > -r and len(btns_c) - 1 > -r:
                    if y + 1 < len(btns_r):
                        btns_r[y + 1].h_touched = True
                    if x + 1 < len(btns_c):
                        btns_c[x + 1].v_touched = True
                    board.buttons[x][y].active = True
                
    solution = board.check_validity(r)

if solution:
    print('TAK')
    print(len(board.get_active_buttons()))
    for btn in board.get_active_buttons():
        print(btn.i)
else:
    print('NIE')