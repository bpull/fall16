
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
                    lon = wholeLine[337:347]
                    lon = lon.strip()
                    lat = wholeLine[348:362]
                    lat = lat.strip()

                    test = []
                    test.append(word)
                    test.append(int(num))
                    test.append(lon)
                    test.append(lat)

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

    def saveKML(self, filename):
        '''This will write the district data from the census to a proper KML file to view on maps'''
        filename = str(filename)
        with open(filename,'w') as f:
            f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
            f.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">")
            f.write("<Document>")

            for item in self.data:
                f.write("<Placement>")
                f.write("<name>"+item[0]+"</name>")
                f.write("<LookAt>")
                f.write("<longitude>"+item[2]+"</longitude>")
                f.write("<latitude>"+item[3]+"</latitude>")
                f.write("</LookAt>")
                f.write("</Placement>")

            f.write("</Document>")
            f.write("</kml>")
