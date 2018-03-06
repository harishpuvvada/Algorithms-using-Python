# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line
#
# Sample Input 0
#
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample Output 0
#
# Berry
# Harry

if __name__ == '__main__':
    namscore = {}
    for _ in range(int(input())): #Reading N value
        name = input()              #reading name, score each time
        score = float(input())
        if score in namscore:
            namscore[score].append(name)  #if score already exists, append to list
        else:
            namscore[score] = [name]  #if not, create a new list
    k = sorted(namscore.keys())  #sorting keys
    sol = namscore[k[1]]   # storing the values of second min value in "sol"
    for i in sorted(sol):  # to print them in alphabetical order
        print(i)
