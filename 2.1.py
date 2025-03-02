inttuple = (5, 10, 15)
floattuple = (10.1, 18.5, 18.4)
stringtuple = ("car", "bike", "truck")
mixedtuple = (5, "car", 10.1)

print(inttuple)
print(floattuple)
print(stringtuple)
print(mixedtuple)

print(inttuple[0])
print(stringtuple[-1])

print(floattuple[1:3])
print(mixedtuple[:2])
print(mixedtuple[2:])
print("Colon",mixedtuple[0:3:2])



tuple1= (1, 2, 3, 1, 1 )
print("Occurence",tuple1.count(1))
print("Index",tuple1.index(2))

print(len(inttuple))
print(max(floattuple))
print(min(floattuple))
print(sum(inttuple))

list1 = list(tuple1)
print(list1)
tuple2 = tuple(list1)
print(tuple2)

a, b, c, d, e = tuple1
print(a, b, c, d, e)
        





