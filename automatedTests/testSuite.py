# test_suite.py
import unittest
from automatedTests.Tests import RegisterTests


# Create the test suite
def create_test_suite():
    suite = unittest.TestSuite()

    # Add individual tests or test cases to the suite

    suite.addTest(RegisterTests('test_register'))

    return suite


if __name__ == "__main__":
    # Create the test suite
    suite = create_test_suite()

    # Set up the test runner
    runner = unittest.TextTestRunner()

    # Run the test suite
    runner.run(suite)
