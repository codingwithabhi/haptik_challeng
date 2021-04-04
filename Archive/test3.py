from itertools import combinations
a = [22, 6, 23, 10, 1, 3]
m = max(a)
a.remove(m)
def check(a):
    for i in range(1,len(a)):
        l = [sum(j) for j in combinations(a,i)]
        if m in l:
            return True
    return False

print(check(a))