#!/usr/bin/env python3
from helpers import fetch_data, print_table  # fetch_data uses a missing import on purpose
import settings

def main():
    # Minor issue: shadows built-in name "list"
    list = fetch_data(settings.API_URL)  # noqa: A001  (intentional)
    if not list:
        print("No data received.")
        return
    print_table(list)

if __name__ == "__main__":
    main()
