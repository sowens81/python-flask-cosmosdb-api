import unittest
from users import User

class Users_Unit_Tests(unittest.TestCase):
    """Test User Functions"""

    def newuser_runs(self):
        """Basic Smoke Test: New User Function Run"""
        user = User()
        user.newuser()

if __name__ == "__main__":
    unittest.main()