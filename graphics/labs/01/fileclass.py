
class census:
    '''Loads in census data, takes the filename on initialization'''

    def __init__(self, filename):
        '''Initializes the census object'''
        self.data = []
        filename = str(filename)
        try:
            with open(filename,'r') as data:
                for wholeLine in data:
                    num = wholeLine[213:226]
                    num = num.strip()
                    word = wholeLine[226:316]
                    word = word.strip()

                    test = []
                    test.append(word)
                    test.append(int(num))

                    self.data.append(test)

                    self.data.sort()
        except IOError as e:
            print("File did not exist")
            print(str(e))

    def display(self):
        '''This will display the entire census data sorted by district'''
        for i in range(len(self.data)):
            print (str(self.data[i][1]).ljust(21)+' '+self.data[i][0])

    def searchByNum(self, num):
        '''This will find one line of the census matching the number desired'''
        for i in range(len(self.data)):
            if self.data[i][1] == int(num):
                print (str(self.data[i][1]).ljust(21)+' '+self.data[i][0])
                return
        print ("Num not found!")

    def searchByDistrict(self, area):
        '''This will find one line of the census matching the district desired'''
        area = str(area)
        for i in range(len(self.data)):
            if self.data[i][0] == area:
                print (str(self.data[i][1]).ljust(21)+' '+self.data[i][0])
                return
        print ("District not found!")
