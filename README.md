## python-logger-package
A lightweight Python package for logging messages to the terminal, enhancing visibility and traceability of events in
applications. This package is not meant to be used for logging to files, but rather for logging to the terminal.
to install the package, run `pip install ./python-logger-package` in directory containing the repository as this is not
published to PyPI or any other package repository.

Other than that, the package is pretty self-explanatory. The package contains a `log` function which can be used to log
messages to the terminal. The takes the following arguments:
- `debug_level: str`: The string can literally be anything, but here are some suggestions:
    - `DEBUG`: For debugging messages
    - `INFO`: For informational messages
    - `WARNING`: For warning messages
    - `ERROR`: For error messages
- `source: str`: The source of the message, this can be anything, but it is recommended to use the name of the file
  where the message is logged from for traceability
- `message: str`: The message to be logged
all of these arguments are not required, but might be a good idea to use them for traceability and visibility of the
messages. The `log` function will print the message to the terminal.