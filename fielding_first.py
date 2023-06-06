"""
Arnav Khare & Aditi Manjunath
CSE 163
this file implements the function field_bat_win_rate
"""
import pandas as pd
from base import cutsom_bar_chart


def field_bat_win_rate(IPL_data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the average win rate for teams who choose to field or bat first
    and plot the results. Plot is saved as field_bat_win_rate.png

    Args:
        IPL_data (pd.DataFrame): IPL data by team.

    Returns:
        pd.DataFrame: DataFrame with the home ground advantage for each team.
        Has the following columns: Team, Home Win Rate, Away Win Rate.
    """
    field_data = IPL_data[IPL_data['toss_decisions'] == 'Field']
    bat_data = IPL_data[IPL_data['toss_decisions'] == 'Bat']
    field_winners = field_data[field_data['toss_winner'] ==
                               field_data['winner']]
    bat_winners = bat_data[bat_data['toss_winner'] == bat_data['winner']]
    field_win_rate = len(field_winners) / len(field_data)
    bat_win_rate = len(bat_winners) / len(bat_data)
    # Create a DataFrame to plot
    data = {
        'Metrics': ['Field', 'Bat'],
        'Rates': [field_win_rate, bat_win_rate]
    }
    df = pd.DataFrame(data)
    cutsom_bar_chart(df, data['Metrics'], data['Rates'],
                     'Toss Decision Win Rates', 'Field or Bat',
                     'Win Rates', 'Field_Bat_Win_Rate.png')
    return df


def main():
    IPL_data = pd.read_csv('data/2023 IPL Teams.csv')

    field_bat_data = field_bat_win_rate(IPL_data)

    print(field_bat_data)


if __name__ == '__main__':
    main()
