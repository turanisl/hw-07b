# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4,5,3),'Right')

    def testRightTriangleD(self):
        self.assertEqual(classifyTriangle(5,12,13),'Right')

    def testRightTriangleE(self):
        self.assertEqual(classifyTriangle(13,5,12),'Right')

    def testEquilateralTriangleLarge(self):
        self.assertEqual(classifyTriangle(200,200,200),'Equilateral')

    def testEquilateralTriangleMedium(self):
        self.assertEqual(classifyTriangle(50,50,50),'Equilateral')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(5,5,3),'Isoceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,5),'Isoceles')

    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(3,5,5),'Isoceles')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(4,5,6),'Scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(6,4,5),'Scalene')

    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(5,6,4),'Scalene')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(3,1,2),'NotATriangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(2,3,1),'NotATriangle')

    def testNotATriangleD(self):
        self.assertEqual(classifyTriangle(1,2,10),'NotATriangle')

    def testZeroInputA(self):
        self.assertEqual(classifyTriangle(0,3,4),'InvalidInput')

    def testZeroInputB(self):
        self.assertEqual(classifyTriangle(3,0,4),'InvalidInput')

    def testZeroInputC(self):
        self.assertEqual(classifyTriangle(3,4,0),'InvalidInput')

    def testNegativeInputA(self):
        self.assertEqual(classifyTriangle(-1,3,4),'InvalidInput')

    def testNegativeInputB(self):
        self.assertEqual(classifyTriangle(3,-1,4),'InvalidInput')

    def testNegativeInputC(self):
        self.assertEqual(classifyTriangle(3,4,-1),'InvalidInput')

    def testAboveMaximumA(self):
        self.assertEqual(classifyTriangle(201,3,4),'InvalidInput')

    def testAboveMaximumB(self):
        self.assertEqual(classifyTriangle(3,201,4),'InvalidInput')

    def testAboveMaximumC(self):
        self.assertEqual(classifyTriangle(3,4,201),'InvalidInput')

    def testNonIntegerInputA(self):
        self.assertEqual(classifyTriangle(3.5,4,5),'InvalidInput')

    def testNonIntegerInputB(self):
        self.assertEqual(classifyTriangle(3,4.5,5),'InvalidInput')

    def testNonIntegerInputC(self):
        self.assertEqual(classifyTriangle(3,4,5.5),'InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()