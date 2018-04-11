def permute(s):
    print(s)
    out = []

    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        # For every letter in string
        for i, let in enumerate(s):
            print(out)
            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(s[:i] + s[i+1:]):

                # Add it to output
                out += [let + perm]

    return out



'''    (or) '''


def permutations(string):
    """Create all permutations of a string with non-repeating characters
    """
    print(string)
    permutation_list = []
    if len(string) == 1:
        return [string]
    else:
        for char in string:
            for a in permutations(string.replace(char, "")):
                permutation_list.append(char + a)
    return permutation_list
