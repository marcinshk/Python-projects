#! python

class Area(object):
    def __init__(self, area):
        self.area = area
    def getArea(self):
        return self.area

class Country(Area):
    def __init__(self, name, capital, area):
        self.__name = name
        self.__capital = capital
        self.__population = population
        self.__neighbors = neighbors
        super(Country, self).__init__(area)

    def getArea(self):
        return self.area

    def getCapital(self):
        return self.__capital

    def describe(self):
        print "Name: " + self.__name
        print "Capital: " + self.__capital
        print "Area (sq. kilometers): " + str(self.area)


#--

#poland = Country('Poland', 'Warsaw', 300000)
