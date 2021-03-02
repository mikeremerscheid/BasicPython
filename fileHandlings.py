# f = open("demofile.txt", "r")
# print(f.read())

f = open("demofile.txt", "r")
# print(f.read(5))
# print(f.readline())
# print(f.readline())
# print(f.readline())

for x in f: 
    print(x)

f.close()