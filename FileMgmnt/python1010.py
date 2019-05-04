import math   # This will import math module
import unicodedata
import random
mangoes = {0:"zero",1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
guava = 2
# mangoes = 2
str = guava is mangoes
print(str)         # Prints complete string
#print(chr(0x0bf2))
x=random.choices(mangoes)
# print("math.ceil(-45.17) : ", math.ceil(-45.17))
# print("math.ceil(100.12) : ", math.ceil(100.12))
# print("math.ceil(100.72) : ", math.ceil(100.72))
# print("math.floor(100.72) : ", math.floor(100.72))
#print ("math.ceil(119L) : ", math.ceil(119L))
print("math.ceil(math.pi) : ", math.ceil(math.pi))
print(f"Choices(mangoes) {x}")
print("choice([1, 2]) : ", random.choice([1, 2]))
print("choice({1: 'one', 2: 'two'} : ", random.choice({1: 'one', 2: 'two'}))
