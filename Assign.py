import re

hand = open("regex_sum_453260.txt")
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y

sum=0
for z in x:
    sum = sum + int(z)

print(sum)
print("Hello World")
