import sys
from datetime import datetime


def main():
    print_greeting()
    print_current_time()


def print_greeting():
    name = sys.argv[1] if len(sys.argv) > 1 else "[Luke Skywalker]"
    hour = datetime.now().hour
    greeting = "morning" if hour in range(0, 12) else "afternoon" if hour in range(12, 18) else "evening"
    print(f"Good {greeting}, {name}!")


def print_current_time():
    time = datetime.now()
    print(f"Current time is {time}")
    print(f"Year {time.year}\nMonth: {time.month}\nDay: {time.day}")
    print(f"Hour {time.hour}\nMinutes: {time.minute}\nDay: {time.second}")
    print(f"Formatted date: {time.strftime('%m/%d/%Y')}")


if __name__ == '__main__':
    main()
