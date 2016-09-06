import sys

if len(sys.argv) < 2:
    print("usage: fileread.py <filename>")
    sys.exit()

filename = str(sys.argv[1])

try:
    a = []
    with open(filename,'r') as data:

        for wholeLine in data:
            num = wholeLine[213:226]
            num = num.strip()
            word = wholeLine[226:316]
            word = word.strip()

            test = []
            test.append(word)
            test.append(num)

            a.append(test)

        a.sort()
except IOError as e:
    print("File did not exist")
    print(str(e))

for i in range(len(a)):
    print (a[i][1].ljust(21)+' '+a[i][0])
