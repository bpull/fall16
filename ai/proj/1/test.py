ranges = [range(2,6), range(1,6), range(6), range(6), range(5), range(4)]

count = 1
for cur_range,j in zip(ranges,range(2,-4,-1)):
    for i in cur_range:
        print (str(i+1)+","+str(i-j+1))
