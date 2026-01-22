import unittest
from modus import modus


class TestModus(unittest.TestCase):
    """Test cases for the modus function"""
    
    def test_single_mode(self):
        """Test dataset with a single mode"""
        self.assertEqual(modus([1, 2, 2, 3, 4]), 2)
        self.assertEqual(modus([5, 5, 5, 1, 2, 3]), 5)
        
    def test_multiple_modes(self):
        """Test dataset with multiple modes (bimodal/multimodal)"""
        self.assertEqual(modus([1, 1, 2, 2, 3]), [1, 2])
        self.assertEqual(modus([1, 1, 2, 2, 3, 3]), [1, 2, 3])
        
    def test_single_element(self):
        """Test dataset with single element"""
        self.assertEqual(modus([5]), 5)
        self.assertEqual(modus([42]), 42)
        
    def test_all_unique(self):
        """Test dataset where all elements are unique"""
        result = modus([1, 2, 3, 4, 5])
        # All values have the same frequency, so all are modes
        self.assertEqual(sorted(result), [1, 2, 3, 4, 5])
        
    def test_empty_list(self):
        """Test empty dataset"""
        self.assertIsNone(modus([]))
        
    def test_with_strings(self):
        """Test with string values"""
        self.assertEqual(modus(['a', 'b', 'b', 'c']), 'b')
        self.assertEqual(modus(['x', 'x', 'y', 'y']), ['x', 'y'])
        
    def test_with_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(modus([-1, -1, -2, 0, 1]), -1)
        
    def test_with_floats(self):
        """Test with floating point numbers"""
        self.assertEqual(modus([1.5, 1.5, 2.0, 3.0]), 1.5)


if __name__ == '__main__':
    unittest.main()
