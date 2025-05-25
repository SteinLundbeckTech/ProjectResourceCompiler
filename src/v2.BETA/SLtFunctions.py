"""
    @Date                 : 24.05.2025
    @Author               : Stein Lundbeck
    @Name                 : SLT Assets tools
    @Description          : Different utilities and features, that minimizes duplicate code
    @Version              : 1.0.0.4
    @Latest               : 25.05.2025
"""
import os
from datetime import datetime

def print_str(val):
    """Prints string with current date and time"""
    print(f"{datetime.now()}\t{val}")

def input_str(val):
    """Takes input while printing string"""
    return input(f"{datetime.now()}\t{val}")

def timestamp():
    """Generates an unique timestamp"""
    return str(datetime.timestamp(datetime.now())).replace(".", "")

def increase(nr):
    """Adds 1 to nr"""
    return nr + 1

def up(nr):
    """Adds 1 to nr"""
    return increase(nr)

def decrease(nr):
    """Retracts 1 from nr"""
    return nr - 1

def down(nr):
    """Retracts 1 from nr"""
    return decrease(nr)

def to_list(items, separator = ",", remove_whitespace = False):
    """Creates separated list from defined items"""
    result = ""
    for item in items:
        if items.index(item) == 0:
            result = item
        else:
            if remove_whitespace:
                result += f"{separator}{item}"
            else:
                result += f"{separator} {item}"

    return result

def add_suffix(filename, suffix = "min"):
    """Adds suffix to filename"""
    return f"{filename[:filename.rfind(".")]}.{suffix}.{filename[filename.rfind("."):]}"

def cls():
    os.system("cls")

def diff_second(start_time, end_time):
    """Gets difference in secounds between two times"""
    return (end_time - start_time).total_seconds()

def diff_minute(start_time, end_time):
    """Gets difference in minutes between two times"""
    diff = diff_second(start_time, end_time)
    if diff >= 60:
        diff = diff / 60
    return diff
