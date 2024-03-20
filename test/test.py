import unittest
from unittest.mock import patch
from secure_log.secure_log import SecureLog, PotentialSecretsLeak

print(PotentialSecretsLeak)

class TestSecureLog(unittest.TestCase):
    @patch.dict('os.environ', {'PYTHON_ENV': 'development', 'PASSWORD': '8er8r'})
    def test_secure_log_in_development(self):
        secure_log = SecureLog(options={"disableOn": "production"})
        
        with self.assertLogs('root', level='INFO') as cm:
            secure_log.secure_print("this is a 8er8r ad")
            self.assertIn('[SECURE LOG]: the value of the secret: "PASSWORD", is being leaked!', cm.output[0])

    @patch.dict('os.environ', {'PYTHON_ENV': 'production', 'PASSWORD': '8er8r'})
    def test_secure_log_in_production(self):
        secure_log = SecureLog(options={"disableOn": "production"})
        with self.assertLogs('root', level='INFO') as cm:
            secure_log.secure_print("this is a 8er8r ad")
            self.assertNotIn('[SECURE LOG]: the value of the secret: "PASSWORD", is being leaked!', cm.output[0])

if __name__ == '__main__':
    unittest.main()