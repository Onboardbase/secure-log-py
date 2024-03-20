# SecureLog

SecureLog is a Python library designed to enhance the security of logging by preventing the leakage of sensitive information. It checks log messages for secrets and prints them securely, ensuring that sensitive data is not exposed in logs.

## Features

- **Secure Logging**: Automatically checks log messages for secrets and prints them securely.
- **Environment-Specific Configuration**: Allows disabling console logging based on the environment variable value.
- **Warning or Exit**: Can be configured to either issue a warning or exit the process when a secret is detected.

## Installation

To install SecureLog, use pip:

```
pip install secure-log==0.1.1
```

## Usage

### Basic Usage

To use SecureLog, simply import the `SecureLog` class and create an instance:

```python
from secure_log import SecureLog

from secure_log import SecureLog
print = SecureLog().secure_print
```
You can override the default `print` function with `secure_print` or use `secure_print ` directly for printing.

### Configuration

You can configure SecureLog by passing an `OptionsDict` to the constructor. The `OptionsDict` can include the following keys:

- `disableOn`: The environment variable value on which console logging should be disabled. This checks the value of `PYTHON_ENV`. Expected type: `str`.
- `warnOnly`: If `True`, only a warning is issued when a secret is detected in the log message. Otherwise, the process exits. Expected type: `bool`.

Example:

```python
options = {
    "disableOn": "production",
    "warnOnly": True
}
secure_log = SecureLog(options=options)
secure_log.secure_print("This is a secure log message.")
```

### Handling Potential Secrets Leak

If a secret is detected in a log message, SecureLog can either issue a warning or exit the process, depending on the `warnOnly` option.

```python
secure_log.secure_print("This message contains a secret: SECRET_KEY")
```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before getting started.

## License

SecureLog is released under the [MIT License](LICENSE).

## Contact

For any questions or concerns, please open an issue on GitHub.