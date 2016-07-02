# encoding: utf-8

# ?- my_last(X,[a,b,c,d]).
# X = d

def p01(data):
    return data[-1]

if __name__ == '__main__':
    print(p01([1, 2, 3, 4, 5]))