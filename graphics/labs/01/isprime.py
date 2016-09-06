import sys

if len(sys.argv) < 2:
    print("usage: isprime.py ###")
    sys.exit()

elif int(sys.argv[1]) > 512:
    print("Choose a number less than 512")
    sys.exit()


test = int(sys.argv[1])
for i in range(2, test):
    if test % i is 0:
        print ("Not Prime!")
        sys.exit()

print ("Prime!")
