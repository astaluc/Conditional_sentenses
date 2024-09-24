import statistics
import math
import pathlib
print(20240924)

'''print("iveskite zodi")
word = input()
if len(word) < 5:
    print(f'zodis {word} yra labai trumpas')
elif len(word) < 10:
    print(f'zodis {word} yra vidutinis')
else:
    print(f'zodis {word} yra ilgas')
'''
if 5 > 4 and 3 < 8 and 7 < 14:
    print("and")

if 5 > 4 or 3 < 8 or 7 > 14:
    print("or")

print("Salyginiia sakiniai if")
print("Uzduotys 2/3.2-3")
'''
print("Iveskite amziu")
amzius = int(input())
if amzius >= 18:
    print("jus galite balsuoti")
'''
'''print("Iveskite pazymius")
paz1 = int(input())
paz2 = int(input())
paz3 = int(input())
print(statistics.mean([paz1, paz2, paz3, 3]))
print(sum([paz1, paz2, paz3]) / len([paz1, paz2, paz3]))
vidurkis = sum([paz1, paz2, paz3]) / len([paz1, paz2, paz3])
if vidurkis > 0 or vidurkis == 5:
    print("vidurkis teigiamas")
print( input() )
'''
print("Uzduotys 3/3.4")
sk = 6
if sk % 5 == 0:
    print("\n", sk * 1, "\n", sk * 2, "\n", sk * 3, "\n", sk * 4, "\n", sk * 5)
if sk % 2 == 0:
    print("\n", sk, "\n", sk ** 2, "\n", sk / 2, "\n", math.sqrt(sk))

print()
print("Salyginiia sakiniai if_elif")
print("Uzduotys 1/2.5")
sk1 = 5
sk2 = 10
sk3 = 15
if sk1 > sk2:
    print("sk1 > sk2")
elif sk2 > sk3:
    print("sk2 > sk3")
elif sk3 > sk1:
    print("sk3 > sk1")

print("Uzduotys 2/2.6")
if sk1 == sk2:
    print("sk1 = sk2")
elif sk2 == sk3:
    print("sk2 = sk3")
elif sk1 == 0:
    print("sk1 = 0")
elif sk2 < 0:
    print("sk2 < 0")
elif sk3 > 0:
    print("sk3 > 0")

print("Uzduotys 2/3.7")
paz = 8
if paz == 10:
    print("puiku")
elif paz >= 9:
    print("labai gerai")
elif paz >= 7:
    print("gerai")
elif paz >= 5:
    print("patenkinamai")
elif paz < 5:
    print("egzaminas neislaikytas")

print()
print("Uzduotys 7-9")
'''
print("Iveskite skaiciu")
skaicius = int(input())
if skaicius % 2 == 0:
    print("lyginis")
else:
    print("nelyginis")
'''
'''print("Iveskite skaiciu")
skaicius = int(input())
if skaicius % 7 == 0:
    print("dalinasi is 7")
else:
    print("nesidalina is 7")
'''
file_format = pathlib.Path('main.py').suffix
if file_format == '.py':
    print("failas .py")
else:
    print("failas ne .py")

print("Uzduotys 1/2.10")
skaicius = 7
if skaicius % 2 == 0:
    print("skaicius lyginis")
elif skaicius % 5 == 0:
    print("skaicius dalinasi is 5")
elif skaicius == 3:
    print("skaicius dalinasi is 5")
else:
    print("klaida")