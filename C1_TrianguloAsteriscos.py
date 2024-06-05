def TrianguloAsterisco(i, t=0):
    if i == 0:
        return 0
    else:
        print(' ' * ( i + 1 ) + '*' * ( t * 2 + 1 ))
        return TrianguloAsterisco( i - 1, t + 1 )

print(TrianguloAsterisco(5))