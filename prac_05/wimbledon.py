"""Game, Set, Match"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX_NUMBER = 1
CHAMPION_INDEX_NUMBER = 2


def main():
    """Get data from file and display champion, number of times winning and winning countries"""
    champion_to_win_count = {}
    lines = open_in_file_to_read()
    # print(lines)
    display_champion_and_win_count(champion_to_win_count, lines)
    display_champion_country(lines)


def display_champion_country(lines):
    """Display winning countries"""
    countries = [line[COUNTRY_INDEX_NUMBER] for line in lines]
    countries.remove("Country")
    print(f"These {len(set(countries))} countries have won Wimbledon: ")
    print(", ".join(sorted(set(countries))))


def display_champion_and_win_count(champion_to_win_count, lines):
    """Display champions and the number of times they won"""
    champions = [line[CHAMPION_INDEX_NUMBER] for line in lines]
    champions.remove("Champion")
    print("Wimbledon Champions: ")
    for champion in champions:
        champion_to_win_count[champion] = champion_to_win_count.get(champion, 0) + 1
    for champion in champion_to_win_count:
        print(f"{champion} {champion_to_win_count[champion]}")


def open_in_file_to_read():
    """Open file to read record"""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        lines = [line.strip().split(",") for line in in_file.readlines()]
    return lines


main()
