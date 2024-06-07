def TrianguloAsterisco(i, t=0):
    i = int(i)

    if i <= 0:
        return t
    else:
        print(' ' * ( i + 1 ) + '*' * ( t * 2 + 1 ))
        return TrianguloAsterisco( i - 1, t + 1 )