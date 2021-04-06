from itertools import combinations
a = [1,2,3,6,8,21]
m = max(a)
a.remove(m)
def check(a):
    for i in range(1,len(a)+1):
        l = [sum(j) for j in combinations(a,i)]
        if m in l:
            return True
    return False

print(check(a))