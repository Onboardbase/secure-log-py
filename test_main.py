import unittest
from unittest.mock import patch
from main import SecureLog

class SecureLogTests(unittest.TestCase):

    def setUp(self):
        self.log = SecureLog()

    def test_check_for_secrets(self):
        message = "This is a secret: 12345"
        expected_output = 'Onboardbase Signatures here: 12345 is present in "This is a secret: 12345" and is a valid secret value for the key: "SECRET_KEY"'
        with patch.dict('os.environ', {'SECRET_KEY': '12345'}):
            with patch('builtins.print') as mock_print:
                self.log.check_for_secrets(message)
                mock_print.assert_called_once_with(expected_output)

    def test_secure_print(self):
        with patch.dict('os.environ', {'NODE_ENV': 'production'}):
            with patch('builtins.print') as mock_print:
                self.log.secure_print("Log message")
                mock_print.assert_not_called()

        with patch.dict('os.environ', {'NODE_ENV': 'development'}):
            with patch('builtins.print') as mock_print:
                self.log.secure_print("Log message")
                mock_print.assert_called_once_with('Onboardbase Signatures here:', "Log message")

if __name__ == '__main__':
    unittest.main()