# test_oathmeld.py
"""
Tests for OathMeld module.
"""

import unittest
from oathmeld import OathMeld

class TestOathMeld(unittest.TestCase):
    """Test cases for OathMeld class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OathMeld()
        self.assertIsInstance(instance, OathMeld)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OathMeld()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
