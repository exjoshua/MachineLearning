#2018.06.22 经典汉诺塔问题

def move(n,a,b,c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

if __name__ == '__main__':
    move(3,'A','B','C')