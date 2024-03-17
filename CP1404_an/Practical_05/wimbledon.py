"""
CP1404/CP5632 Practical
Wimbledon file reader
"""
FILENAME = "wimbledon.csv"


def main():
    """Progam that collects wimbledon data and displays champions and winning countries"""
    wimbledon_data = get_data()
    champion_data = get_champion_data(wimbledon_data)
    for champion, wins in champion_data.items():
        print(f"{champion} {wins}")
    winning_countries = get_country_wins(wimbledon_data)
    print(f"\nThese {len(winning_countries)} have won wimbledon: \n{' '.join(winning_countries)}")


def get_country_wins(wimbledon_data):
    """Get the unique list of countries that have won wimbledon"""
    country_wins = {}
    for data in wimbledon_data:
        country_wins[data[1]] = country_wins.get(data[1], 0) + 1
    winning_countries = list(country_wins.keys())
    return sorted(winning_countries)


def get_champion_data(wimbledon_data):
    """Get wimbledon champions and their associated numer of wins"""
    champion_data = {}
    for data in wimbledon_data:
        champion_data[data[2]] = champion_data.get(data[2], 0) + 1  # dictionary of champion wins
    return champion_data


def get_data():
    """Extracts the data for wimbledon events, winners, countries, scores"""
    wimbledon_data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip the first line containing titles
        for line in in_file:
            wimbledon_data.append(line.strip().split(","))
    return wimbledon_data


main()
