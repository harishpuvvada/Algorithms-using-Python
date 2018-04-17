#Famous fizzbuzz question with only one return statement

def fizzbuzz(i):
    res = ''
    if i%3==0:
        res += 'fizz'
    if i%5==0:
        res += 'buzz'

    return res


for i in range(25):
    print(i,fizzbuzz(i))
