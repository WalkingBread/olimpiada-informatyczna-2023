def get_multiple_values(n):
    values = input().strip().split(' ')
    for x in range(n):
        values[x] = int(values[x])
    return values

n, p, M = get_multiple_values(3)
while(n < 2 or n > 1000 or p < 1 or p > n**2):
    print('Podano nieprawidlowe wartosci. Sprobuj ponownie.')
    n, p, M = get_multiple_values(3)

class Sat:
    def __init__(self, n):
        self.n = n
        self.code = ''
        for n in range(M):
            self.code += ' '

class SatSet:
    def __init__(self, n):
        self.sats = []
        for i in range(1, 2 * n+1):
            self.sats.append(Sat(i))

    def get_sat_by(self, n):
        return self.sats[n-1]
    
    def is_code_unique(self, sat1):
        for sat in self.sats:
            if sat1 == sat:
                continue
            if sat1.code == sat.code:
                return False
        return True

s = SatSet(n)

charset = ['A', 'B', 'C']

channels = []

class Channel:
    def __init__(self, char, pos):
        self.char = char
        self.pos = pos
        self.sats = []

def get_channel(char, pos):
    for channel in channels:
        if channel.char == char and channel.pos == pos:
            return True
    return False

def replace_char(s, i, nc):
    return s[0:i] + nc + s[i+1:]

max_pos = 0
for i in range(p):
    a, b = get_multiple_values(2)
    while a < 1 or a > n or b < n + 1 or b > 2*n:
        print('Podano nieprawidlowe wartosci. Sprobuj ponownie.')
        a, b = get_multiple_values(2)
    sat1 = s.get_sat_by(a)
    sat2 = s.get_sat_by(b)
    conn_established = False
    for k in range(M):
        if sat1.code[k] == ' ' and sat2.code[k] == ' ':
            for c in charset:
                if not get_channel(c, k):
                    sat1.code = replace_char(sat1.code, k, c)
                    sat2.code = replace_char(sat2.code, k, c)
                    channel = Channel(c, k)
                    channel.sats = [sat1, sat2]
                    channels.append(channel)
                    conn_established = True
                    if k > max_pos:
                        max_pos = k
                    break
            if conn_established:
                break

def get_channel_with(sats):
    for channel in channels:
        if channel.sats == sats:
            return True
    return False

def fill_gaps(s, max_pos):
    for y in range(len(s.sats)):
        sat = s.sats[y]
        for k in range(max_pos + 1):
            if sat.code[k] == ' ':
                for c in charset:
                    st = 0
                    e = n
                    if y < n:
                        st = n
                        e = 2 * n
                    f = True
                    for x in range(st, e):
                        if c == s.sats[x].code[k]:
                            if not get_channel_with([sat, s.sats[x]]):
                                f = False
                                break
                    if f:
                        sat.code = replace_char(sat.code, k, c)
                        break
    for sat in s.sats:
        if not s.is_code_unique(sat) and max_pos + 1 < M:
            max_pos = fill_gaps(s, max_pos + 1)
            break
    return max_pos

max_pos = fill_gaps(s, max_pos)

print(max_pos + 1)
for sat in s.sats:
    print(sat.code)