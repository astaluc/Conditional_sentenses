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
'''print("Uzduotys 3/3.4")
sk = 6
if sk % 5 == 0:
    print("\n", sk * 1, "\n", sk * 2, "\n", sk * 3, "\n", sk * 4, "\n", sk * 5)
if sk % 2 == 0:
    print("\n", sk, "\n", sk ** 2, "\n", sk / 2, "\n", math.sqrt(sk))
if sk % 7 != 0:
    print("Iveskite skaiciu")
kint2 = int( input() )
suma = sk + kint2
skirtumas = sk - kint2
sandauga = sk * kint2
dalmuo = sk / kint2
print(f'suma {suma}, skirtumas {skirtumas}, sandauga {sandauga}, dalmuo {dalmuo}')
'''

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

print("Uzduotys 2/2.11")
if sk1 == sk2:
    print(f'skaicius {sk1} = {sk2}')
elif sk1 == sk3:
    print(f'skaicius {sk1} = {sk3}')
elif sk3 > sk1:
    print(f'skaicius {sk3} > {sk1}')
elif sk2 == 2 * sk3:
    print(f'skaicius {sk2} = {sk3} * 2')
elif sk1 % 3 == 0:
    print(f'skaicius {sk3} % 3 = 0')
else:
    print("klaida")

#nr = int( input("Iveskite skaiciu") )
#print( input() )
#skaicius = int(input())
print()
print("Uzduotys 1/2.12-14")
'''
nr1 = int( input("Iveskite skaiciu:") )
nr2 = int( input("Iveskite skaiciu:") )
nr3 = int( input("Iveskite skaiciu:") )
if nr1 > nr2 and nr1 > nr3:
    print("nr1 didziausiais")
elif nr2 > nr1 and nr2 > nr3:
    print("nr2 didziausiais")
else:
    print(f'{nr3} didziausias')
'''
'''nr1 = int( input("Iveskite skaiciu:") )
nr2 = int( input("Iveskite skaiciu:") )
nr3 = int( input("Iveskite skaiciu:") )
if nr1 < nr2 and nr1 < nr3:
    print("nr1 maziausias")
elif nr2 < nr1 and nr2 < nr3:
    print("nr2 maziausias")
else:
    print(f'{nr3} maziausias')
'''
paz1 = 7
paz2 = 8
paz3 = 9
print( statistics.mean([7, 8, 9]) )
paz_vidurkis = sum([paz1, paz2, paz3]) / len([paz1, paz2, paz3])
print(paz_vidurkis)
if paz_vidurkis >= 8 and paz_vidurkis <= 10:
    print("vidurkis [8-10]")
elif paz_vidurkis >= 5 and paz_vidurkis <= 8:
    print("vidurkis [5-8)")
else:
    print("vidurkis < 5")

print("Uzduotys 2/2.15")
if sk1 > sk2 or sk1 == 0:
    print(f'{sk1} > {sk2} or {sk1} = 0')
elif sk2 > sk1 or sk2 == 5:
    print(f'{sk2} > {sk1} or {sk2} = 5')
elif sk1 > sk2 and sk1 == 20:
    print(f'{sk1} > {sk2} and {sk1} = 20')
elif sk2 > sk1 and sk1 < 100:
    print(f'{sk2} > {sk1} and {sk2} < 100')
