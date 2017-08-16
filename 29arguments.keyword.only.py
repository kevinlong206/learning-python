def kwo(*a, c):
    print(a, c)

kwo(1, 2, 3, c=7)  #prints (1, 2, 3,) 7
kwo(c=4) #prints () 4

# kwo(1, 2)  #breaks,invalid syntax
