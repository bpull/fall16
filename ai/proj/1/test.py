ranges = [range(2,6), range(1,6), range(6), range(6), range(5), range(4)]

for cur_range,j in zip(ranges,range(2,-4,-1)):
    for i in cur_range:
        print (str(i+1)+","+str(i-j+1))

print ("---------------")
xranges = [range(3,-1,-1),range(4,-1,-1),range(5,-1,-1),range(5,-1,-1),range(5,0,-1),range(5,1,-1)]
yranges = [range(4), range(5), range(6), range(1,7), range(2,7), range(3,7)]
for rows,cols in zip(xranges,yranges):
    for i,j in zip(rows,cols):

        print (str(i+1)+","+str(j+1))
