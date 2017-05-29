import operator as op


def solution_asc(dic):

    sorted_x = sorted(dic.items(), key=op.itemgetter(0))

    return sorted_x

def solution_desc(dic):
    sorted_x = sorted(dic.items(), key=op.itemgetter(0),reverse=True)
    
    return sorted_x

print solution_asc({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})

print solution_desc({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})
