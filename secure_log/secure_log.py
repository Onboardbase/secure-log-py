import os
from typing import TypedDict, Any, Optional

class OptionsDict(TypedDict):
    """
    Options for configuring the SecureLog class.

    Keys:
        disableOn: The environment variable value on which console logging should be disabled. Expected type: str.
        warnOnly: If True, only a warning is issued when a secret is detected in the log message. Otherwise the process exits. Expected type: bool.
    """
    disableOn: Optional[str]
    warnOnly: Optional[bool]

class SecureLog:
    """
    A class for secure logging.

    This class provides functionality to log messages securely, by checking for secrets in the log messages and printing them with a log prefix.

    Attributes:
        options (dict): A dictionary of options for configuring the secure logging.

    Methods:
        check_for_secrets(message): Checks if any secrets are present in the given message.
        secure_print(*args, **kwargs): Prints the log message securely.

    """

    def __init__(self, options: Optional[OptionsDict]=None):
        self.options = options or {}
        self.disable_on = self.options.get('disableOn')
        self.log_prefix = "[SECURE LOG]:"
        self.secrets = os.environ
        self.warnOnly = self.options.get('warnOnly', False)

    def check_for_secrets(self, message: str) -> None:
        """
        Checks if any secrets are present in the given message.

        Args:
            message (str): The log message to check for secrets.

        """
        for secret_key, secret_value in self.secrets.items():
            if secret_value and secret_value in message:
                printRed(f'{self.log_prefix} the value of the secret: "{secret_key}", is being leaked!')
                if not self.warnOnly:
                    raise PotentialSecretsLeak("potential secret leak")

    def secure_print(self, *args: Any, **kwargs: Any) -> None:
        """
        Prints the log message securely.

        Args:
            *args: Variable length argument list of log message parts.
            **kwargs: Arbitrary keyword arguments.

        """
        if self.disable_on and os.environ.get('PYTHON_ENV') == self.disable_on:
            return
        message = ' '.join(map(str, args))
        self.check_for_secrets(message)
        if not self.disable_on or os.environ.get('PYTHON_ENV') != self.disable_on:
            print(f'{self.log_prefix}', *args, **kwargs)

class PotentialSecretsLeak(Exception):
    "Raised when there is a secret in the log message"
    # pass

def printRed(s: str) -> None:
    print("\033[91m {}\033[00m".format(s))
    
