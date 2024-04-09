import sys
from datetime import datetime


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "Luke Skywalker"
    print(f"Hello, {name}!")
    print_current_time()


def print_current_time():
    time = datetime.now()
    print(f"Current time is {time}")
    print(f"Year {time.year}\nMonth: {time.month}\nDay: {time.day}")
    print(f"Hour {time.hour}\nMinutes: {time.minute}\nDay: {time.second}")
    print(f"Formatted date: {time.strftime('%m/%d/%Y')}")


if __name__ == '__main__':
    main()
