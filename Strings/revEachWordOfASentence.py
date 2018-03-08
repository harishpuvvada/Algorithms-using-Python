#Reverse characters of each word in a sentence(whitespace separated)
def rev(s):
    words = s.split()
    result = ""
    for word in words:
        result += word[::-1]
        result += " "

    return result


print(rev("Harish is a Student"))
