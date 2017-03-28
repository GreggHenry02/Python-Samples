class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=0
    
    # Add your code here
    def computeDifference(self):
        min = 101;
        max = -1;
        # print "computerDifference, %d %d" % (min,max)
        for x in self.__elements:
            if x < min:
                min = x
            if x > max:
                max = x
            self.maximumDifference = max-min        
            
# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference			
