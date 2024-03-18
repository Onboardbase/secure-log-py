import os

cached_print = print
class SecureLog:
    """
    A class for secure logging.

    This class provides functionality to log messages securely, by checking for secrets in the log messages and printing them with a log prefix.

    Attributes:
        options (dict): A dictionary of options for configuring the secure logging.
        disable_on (str): The environment variable value on which logging should be disabled.
        disable_console_on (str): The environment variable value on which console logging should be disabled.
        log_prefix (str): The prefix to be added to the log messages.
        secrets (dict): A dictionary of environment variables containing secrets.

    Methods:
        check_for_secrets(message): Checks if any secrets are present in the given message.
        secure_print(*args, **kwargs): Prints the log message securely.

    """

    def __init__(self, options=None):
        self.options = options or {}
        self.disable_on = self.options.get('disableOn')
        self.disable_console_on = self.options.get('disableConsoleOn')
        self.log_prefix = 'Onboardbase Signatures here:'
        self.secrets = os.environ

    def check_for_secrets(self, message):
        """
        Checks if any secrets are present in the given message.

        Args:
            message (str): The log message to check for secrets.

        """
        for secret_key, secret_value in self.secrets.items():
            if secret_value and secret_value in message:
                cached_print(f'{self.log_prefix} {secret_value} is present in "{message}" and is a valid secret value for the key: "{secret_key}"')

    def secure_print(self, *args, **kwargs):
        """
        Prints the log message securely.

        Args:
            *args: Variable length argument list of log message parts.
            **kwargs: Arbitrary keyword arguments.

        """
        if self.disable_console_on and os.environ.get('NODE_ENV') == self.disable_console_on:
            return
        message = ' '.join(map(str, args))
        self.check_for_secrets(message)
        if not self.disable_console_on or os.environ.get('NODE_ENV') != self.disable_console_on:
            cached_print(f'{self.log_prefix}', *args, **kwargs)

print = SecureLog().secure_print

print(["today 12345jjj "])