import statistics
import math
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

print("Salyginiia sakiniai")
print("Uzduotys 2/3")
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
'''
print("Uzduotys 3/3")
sk = 6
if sk % 5 == 0:
    print("\n", sk * 1, "\n", sk * 2, "\n", sk * 3, "\n", sk * 4, "\n", sk * 5)
if sk % 2 == 0:
    print("\n", sk, "\n", sk ** 2, "\n", sk / 2, "\n", math.sqrt(sk))
