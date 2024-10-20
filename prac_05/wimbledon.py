"""
CP1404 - Prac 5
Program: Wimbledon
"""

FILENAME = 'wimbledon.csv'
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2

def main():
    """Load records from file and display details of champions."""
    records = load_records()
    champion_to_win_count, countries = process_records(records)
    display_results(champion_to_win_count, countries)

def load_records():
    """Create a list of records using data from CSV file."""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            records.append(parts)
    return records

def process_records(records):
    """Create a dictionary of champions to win count."""
    champion_to_win_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_win_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_win_count[record[CHAMPION_INDEX]] = 1
    return champion_to_win_count, countries


def display_results(champion_to_win_count, countries):
    """Display champions and winning countries."""
    print("Wimbledon Champions: ")
    for champion, win_count in champion_to_win_count.items():
        print(f"{champion} {win_count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon")
    print(", ".join(country for country in sorted(countries)))

main()