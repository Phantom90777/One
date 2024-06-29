accounting/
|-- main.py
|-- dirty_main.py
|-- application/
    |-- __init__.py
    |-- salary.py
    |-- db/
        |-- __init__.py
        |-- people.py

import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

def main():
    print(f"Current date and time: {datetime.datetime.now()}")
    calculate_salary()
    get_employees()

if __name__ == '__main__':
    main()

def calculate_salary():
    print("Calculating salary...")
def get_employees():
    print("Getting employees...")

from application.salary import *
from application.db.people import *

def main():
    print(f"Current date and time: {datetime.datetime.now()}")
    calculate_salary()
    get_employees()

if __name__ == '__main__':
    main()
#requests==2.28.1

accounting/
|-- main.py
|-- dirty_main.py
|-- application/
|   |-- __init__.py
|   |-- salary.py
|   |-- db/
|       |-- __init__.py
|       |-- people.py
|-- requirements.txt