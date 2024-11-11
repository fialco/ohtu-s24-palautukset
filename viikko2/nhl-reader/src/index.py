
#Main before EX 13

"""
from player import PlayerReader, PlayerStats

def main():

    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()

"""

from player import PlayerReader, PlayerStats

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table


def main(console):
    console.print("NHL statistics by nationality", style="italic")
    season = Prompt.ask("Select season [orchid][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25]")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    
    while True:
        nationality = Prompt.ask("Select nationality [orchid][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR]")
        
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Top scorers of {nationality} season {season}")
        table.add_column("Name", style="cyan")
        table.add_column("Team", style="purple")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="green")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals+player.assists))
        
        console.print(table)


if __name__ == "__main__":
    console = Console()
    main(console)