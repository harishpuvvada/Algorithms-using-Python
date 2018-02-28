def firstNotRepeatingCharacter(s):
    if len(s)==1:
        return s
    seen = {}
    for char in s:
        if char not in seen:
            seen[char]=1
        else:
            seen[char] +=1
    #print(seen)
    if len(seen)!=0:
        for k,v in seen.items():
            if v==1:
                return k
    return "_"
