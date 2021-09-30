d = {'a': [['b', 7], ['c', 3]], 'b': [['a', 7], ['c', 2], ['e', 1], ['d', 2]], 'c': [['a', 3], ['b', 2], ['e', 5]], 'd': [['b', 2], ['2', 2], ['f', 1]], 'e': [['b', 1], ['c', 5], ['d', 2], ['f', 9]], 'f': [['d', 1], ['e', 9]]}
for i in d:
    d[i] = sorted(d[i], key=lambda student: student[1])


def menor(d, v, b):
    if d[v][0][0] == b and len(d[v][0]) > 1:
        return d[v][1]
    if d[v][0][0] == b and len(d[v][0]) == 1:
        return None
    return d[v][0]
        


def run(d):
    return menor(d, [*d][0], '')


print(run(d))