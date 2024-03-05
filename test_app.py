import unittest
from app import heavyLifter

class TestPlaceBox(unittest.TestCase):

    robotArm = heavyLifter("example.txt")

    def testPlaceBoxToPosition(self):
        """Test placing a box to a non-empty position."""
        elements = ["A", "B", "C"]
        place = 1
        box = "X"
        expectedResult = "BX"
        placedElements = self.robotArm.placeBoxToPosition(elements.copy(), place, box)
        self.assertEqual(placedElements, expectedResult)

if __name__ == '__main__':
    unittest.main()