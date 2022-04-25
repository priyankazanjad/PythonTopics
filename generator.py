# generator to print top ten square of values

def tensquare():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n +=1
values = tensquare()

for i in values:
    print(i)