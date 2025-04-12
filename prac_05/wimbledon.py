"""
Wimbledon
Estimate: 30 minutes
Actual:   50 minutes
"""

import csv
FILENAME = "wimbledon.csv"

def main():
    """Read Wimbledon data from a CSV file,
    process it, and display the results."""

    data = extract_data()
    champion_to_count = count_champions(data)
    countries_string = collect_countries(data)

    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion}: {count}")
    print()

    countries = countries_string.split(", ")
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(countries_string)

def extract_data():
    """Extract required data from the CSV file."""
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) >= 3:
                country = parts[1]
                champion = parts[2]
                data.append((country, champion))
    return data

def count_champions(data):
    """Count the number of times each champion appears in the data."""
    champion_to_count = {}
    for country, champion in data:
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
    return champion_to_count

def collect_countries(data):
    """Collect all the countries of the champions in alphabetical order,
    and return them as a single string separated by commas."""
    countries = sorted({country for country, champion in data})
    countries_string = ', '.join(countries)
    return countries_string


main()
