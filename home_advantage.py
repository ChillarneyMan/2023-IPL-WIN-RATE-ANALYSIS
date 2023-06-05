import pandas as pd

from base import TEAMS, plot_bar_chart, home_away_win_rate, Team


def home_ground_advantage(IPL_data: pd.DataFrame, team_list: list[Team]) -> pd.DataFrame:
    """
    Calculate the home ground advantage for each team.

    Args:
        IPL_data (pd.DataFrame): IPL data by team.

    Returns:
        pd.DataFrame: DataFrame with the home ground advantage for each team. Has the
        following columns: Team, Home Win Rate, Away Win Rate.
    """
    teams: list[str] = []
    home_win_rates: list[float] = []
    away_win_rates: list[float] = []

    for team in team_list:
        home_wins, away_wins = home_away_win_rate(IPL_data, team)
        teams.append(team.name)
        home_win_rates.append(home_wins)
        away_win_rates.append(away_wins)

    # Create a DataFrame with the results for plotting purposes
    data_frame = pd.DataFrame(
        {
            'Team': teams,
            'Home Win Rate': home_win_rates,
            'Away Win Rate': away_win_rates
        }
    )

    # Plot the results
    plot_bar_chart(data_frame, 'Team', 'Home Win Rate',
                   'Home Win Rate per Team', 'Team',
                   'home_win_rate.png')
    plot_bar_chart(data_frame, 'Team', 'Away Win Rate',
                   'Away Win Rate per Team', 'Team', 'away_win_rate.png')

    return data_frame


def main():
    """
    Take the IPL data and calculate the home ground advantage for each team. Plot
    the results. Print the results as a DataFrame.
    """
    # Load the IPL data
    IPL_data = pd.read_csv('data/2023 IPL Teams.csv')

    # Calculate the home ground advantage for each team
    home_advantage_data = home_ground_advantage(IPL_data, TEAMS)

    # Print the results
    print(home_advantage_data)


if __name__ == '__main__':
    main()
