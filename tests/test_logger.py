import unittest
from logger_utils.colory_pprint import ColoryPPrint

class TestColoryPPrint(unittest.TestCase):
    def test_default_logging(self):
        logger = ColoryPPrint()
        self.assertIsInstance(logger, ColoryPPrint)

    def test_custom_styles(self):
        logger = ColoryPPrint()
        logger.red.bold({"message": "Test message"})  # Ensure no exceptions are raised

if __name__ == "__main__":
    unittest.main()
