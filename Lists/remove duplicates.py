
'''remove duplicates from a given list'''

def remove_duplicates(lst):
    seen = set()
    res = []
    for x in lst:
        if x not in seen:
            res.append(x)
            seen.add(x)
    return res