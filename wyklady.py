def get_multiple_values(n):
    values = input().strip().split(' ')
    for x in range(n):
        values[x] = int(values[x])
    return values

def copy_arr(arr):
    cp = []
    for elt in arr:
        cp.append(elt)
    return cp

n = int(input())
while n < 2:
    print('Podano niewlasciwa liczbe wykladow. Sprobuj ponownie.')
    n = int(input())

class Lecture:
    def __init__(self, id, start, end):
        self.id = id
        self.start = start
        self.end = end

    def collide(self, lecture):
        return not (self.end <= lecture.start or lecture.end <= self.start)
    
    def collide_mult(self, lectures):
        for lecture in lectures:
            if self.collide(lecture):
                return True
        return False
    
    def get_coverage(self, lecset, remaining):
        lecset_mod = copy_arr(lecset)
        lecset_mod.remove(self)
        for lecture in remaining:
            if not lecture.collide_mult(lecset_mod):
                return lecture
    
def sort_lectures(lectures): 
    for i in range(1, len(lectures)):
        key = lectures[i]
        j = i - 1
        while j >= 0 and key.start < lectures[j].start:
                lectures[j + 1] = lectures[j]
                j -= 1
        lectures[j + 1] = key
 
lectures = []

for i in range(1, n + 1):
    start, end = get_multiple_values(2)
    while start < 1 or start >= end or end > 10**9:
        print('Podano niewlasciwe terminy rozpoczecia i zakonczenia. Sprobuj ponownie.')
        start, end = get_multiple_values(2)
    lectures.append(Lecture(i, start, end))

sort_lectures(lectures)

def choose_lecture_set(lectures, i):
    lecset = [lectures[i]]
    remaining = []
    for lecture in lectures:
        if lecture == lectures[i]:
            continue
        if not lecture.collide_mult(lecset):
            lecset.append(lecture)
        else:
            remaining.append(lecture)
    return (lecset, remaining)


def all_covered(lecset, remaining):
    for lecture in lecset:
        if lecture.get_coverage(lecset, remaining) == None:
            return False
    return True

max_lecset = []
max_remaining = []

for i in range(n):
    lecset, remaining = choose_lecture_set(lectures, i)

    while not all_covered(lecset, remaining):
        for lecture in lecset:
            if lecture.get_coverage(lecset, remaining) == None:
                lecset.remove(lecture)
                for rem in remaining:
                    if not rem.collide_mult(lecset):
                        lecset.append(rem)
                        remaining.remove(rem)
                        break
                remaining.append(lecture)
                break
    if len(lecset) > len(max_lecset):
        max_lecset = lecset
        max_remaining = remaining

print(len(max_lecset))
for lecture in max_lecset:
    coverage = lecture.get_coverage(max_lecset, max_remaining)
    print(lecture.id, coverage.id)

