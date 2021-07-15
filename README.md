# Web Test Example

Automated Web UI test example

## Requirements

1. Python 3.8+


## Installation

1. Create a Python 3 virtual environment (say, venv).
1. Enter the virtual environment.
1. Install dependencies
   ```shell
   pip install -r requirements.txt
   ```

## Execution

To run the target Web site:

1. Enter the virtual environment.
1. Run the Web server
   ```shell
   FLASK_APP=main fsk run
   ```
1. Now the Web site is available at http://localhost:5000

Target Web pages:

1. Hidden element exception: http://localhost:5000/hidden_element