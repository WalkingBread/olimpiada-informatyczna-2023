def get_multiple_values(n):
    values = input().strip().split(' ')
    for x in range(n):
        values[x] = int(values[x])
    return values

n, k, a, b = get_multiple_values(4)
while n < 2 or n > 10**6 or k < 1 or k >= n or a <= n\
      or a >= b or b >= 10**18 or b + 1 - a > 10**6:
    print('Podano niewlasciwe wartosci. Sprobuj ponownie.')
    n, k, a, b = get_multiple_values(4)
    
text = input()
while len(text) != n:
    print('Podany tekst jest niewlasciwej dlugosci. Sprobuj ponownie.')
    text = input()

def next_letter(text, k):
    suffix = text[len(text) - k:]
    occurences = {}
    for i in range(len(text)-k):
        if text[i:i+k] == suffix:
            c = text[i+k]
            if c in occurences:
                occurences[c] += 1
            else:
                occurences[c] = 1
    max_oc = 0
    max_lt = 'a'
    for letter in occurences.keys():
        oc = occurences[letter]
        if (oc > max_oc) or (oc == max_oc and letter < max_lt):
            max_lt = letter
            max_oc = oc
    return max_lt

s = ''
for i in range(n, b):
    text += next_letter(text, k)
    if i + 1 >= a:
        s += text[i]
print(s)
