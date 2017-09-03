cubes = [x**3 for x in range(10)]

odd_cubes1 = filter(lambda: cube % 2, cubes)
print(odd_cubes1)
odd_cubes2 = (cube for cube in cubes if cube % 2)
print(odd_cubes2)
