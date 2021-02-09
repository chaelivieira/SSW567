
import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    if(a >0 and b> 0 and c>0):
        if a == b and b == c:
            return 'Equilateral'
        elif((a*a + b*b) == c*c )or ((a*a+ c*c) == b*b ) or ((b*b + c*c) == a*a):
            return 'Right'
        elif( a == b and b != c) or ( a == c and b != c) or (b == c and b != a):
            return 'Isoceles'
        elif a != c and b!= c and a !=b:
            return 'Scalene'
        else:
            return 'NotATriangle'
    else:
        return 'NotATriangle'
    
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c))


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
 
    def testSet1(self): #tests right triangles
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(4,3,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(3,5,4),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5,3,4),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(4,5,3),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5,4,3),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(13,5,12),'Right','5,12,13 is a Right triangle')
        self.assertEqual(classifyTriangle(15,17,8),'Right','8,15,17 is a Right triangle')
        self.assertNotEqual(classifyTriangle(1,1,1),'Right','1,1,1 is an Equilteral triangle')
                
    def testMyTestSet2(self): #tests scalene triangles that are not right triangles
        self.assertEqual(classifyTriangle(1,2,3),'Scalene','1,2,3 Should be Scalene')
        self.assertEqual(classifyTriangle(2,4,6),'Scalene','2,4,6 Should be Scalene')
        self.assertEqual(classifyTriangle(10,15,30),'Scalene','10,15,30 Should be Scalene')
        self.assertNotEqual(classifyTriangle(15,17,8),'Scalene','8,15,17 Should be Right')

    def testMyTestSet3(self): #tests equilateral triangles that are not right triangles
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 Should be equilateral')
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 Should be Equilateral')
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','3,3,3 Should be Equilateral')
        self.assertNotEqual(classifyTriangle(0,0,0),'Equilateral','3,3,3 Should be NotATriangle')

    def testMyTestSet4(self): #tests isoceles triangles that are not right triangles
        self.assertEqual(classifyTriangle(1,1,2),'Isoceles','1,1,2 Should be Isoceles')
        self.assertEqual(classifyTriangle(1,2,1),'Isoceles','1,1,2 Should be Isoceles')
        self.assertEqual(classifyTriangle(2,1,1),'Isoceles','1,1,2 Should be Isoceles')
        self.assertEqual(classifyTriangle(22,23,22),'Isoceles','22,23,22 Should be Isoceles')
        self.assertEqual(classifyTriangle(13,13,3),'Isoceles','13,13,3 Should be Isoceles')
        self.assertNotEqual(classifyTriangle(12,13,3),'Isoceles','12,13,3 Scalene')

    def testMyTestSet5(self): #tests incorrect inputs
        self.assertEqual(classifyTriangle(0,1,2),'NotATriangle', '0,1,2 Should be NotATriangle')
        self.assertEqual(classifyTriangle(22,-23,22),'NotATriangle','22,-23,22 Should be NotATriangle')

    def testMyTestSet6(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 Should be equilateral')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(classifyTriangle(10,15,30),'Scalene','Should be Scalene')
        

if __name__ == '__main__':
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(3,4,5)
    runClassifyTriangle(3,4,5)
    runClassifyTriangle(13,5,12)
    runClassifyTriangle(15,17,8)
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(2,4,6)
    runClassifyTriangle(10,15,30)
    runClassifyTriangle(15,17,8)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(2,2,2)
    runClassifyTriangle(3,3,3)
    runClassifyTriangle(1,1,2)
    runClassifyTriangle(22,23,22)
    runClassifyTriangle(13,13,3)
    runClassifyTriangle(0,1,2)
    runClassifyTriangle(22,-23,22)
    runClassifyTriangle(1,1,1) 
    runClassifyTriangle(10,10,10)
    runClassifyTriangle(10,15,30)
    
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
       