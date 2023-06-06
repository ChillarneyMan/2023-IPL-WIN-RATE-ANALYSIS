"""
Arnav Khare & Aditi Manjunath
CSE 163
This is a test file that tests functions from base.py, correlations.py,
home_advantage.py, and fielding_first.py for bugs in the code
"""
import correlations
import base
import home_advantage
import fielding_first
from cse163_utils import assert_equals
import pandas as pd


def test_team_average_economy(gujarat_test_data):
    """
    tests the team_average_economy function from the correlations file

    Args:
        gujarat_test_data (Team): Team to calculate the win rate for.
    
    Returns:
        None
    """
    assert_equals(7.94, correlations.team_average_economy(gujarat_test_data))


def test_team_average_strikerate(gujarat_test_data):
    """
    tests the team_average_strikerate function from the correlation file

     Args:
        gujarat_test_data (Team): Team to calculate the win rate for.
    
    Returns:
        None
    """
    assert_equals(145.64,
                  correlations.team_average_strikerate(gujarat_test_data))


def test_home_away_win_rate(IPL_test, gujarat_test_data):
    """
    tests home_away_win_rates from the base file

     Args:
        IPL_test (pd.DataFrame): IPL data by match.
        gujarat_test_data (Team): Team to calculate the win rate for.
    
    Returns:
        None
    """
    assert_equals((0.5, 1), base.home_away_win_rate(IPL_test,
                                                    gujarat_test_data))


def test_home_ground_advantage(IPL_test, teams_list):
    """
    tests the home_ground_advantage from the home_advantage file

     Args:
        IPL_test (pd.DataFrame): IPL data by match.
        teams_list (list[base.Team]): list of teams (Team)
    
    Returns:
        None
    """
    data_frame = pd.DataFrame(
        {
            'Team': ['Gujarat Titans', 'Chennai Super Kings'],
            'Home Win Rate': [0.5, 1.0],
            'Away Win Rate': [1.0, 0.0]
        }
    )
    assert_equals(data_frame, home_advantage.home_ground_advantage(IPL_test,
                                                                   teams_list))


def test_field_bat_win_rate(IPL_test):
    """
    tests the field_bat_win_rate function from the fielding_first file
    
    Args:
        IPL_test (pd.DataFrame): IPL data by match.
    
    Returns:
        None
    """
    data_frame = pd.DataFrame(
        {
            'Metrics': ['Field', 'Bat'],
            'Rates': [2/3, 0.0]
        }
    )
    assert_equals(data_frame, fielding_first.field_bat_win_rate(IPL_test))


def main():
    test_gujarat = base.Team(name='Gujarat Titans',
                             stadium='Narendra Modi Stadium',
                             bowl_data="data/Test Gujarat Bowling.csv",
                             batting_data="data/Test Gujarat Batting.csv")
    test_chennai = base.Team(name='Chennai Super Kings',
                             stadium='M. A. Chidambaram Stadium',
                             bowl_data="data/Test Chennai Bowling.csv",
                             batting_data="data/Test Chennai Batting.csv")
    test_team_average_economy(test_gujarat)
    test_team_average_strikerate(test_gujarat)
    test_IPL_data = pd.read_csv('data/Test IPL Teams Data.csv')
    test_home_away_win_rate(test_IPL_data, test_gujarat)
    teams_list = [test_gujarat, test_chennai]
    test_home_ground_advantage(test_IPL_data, teams_list)
    test_field_bat_win_rate(test_IPL_data)


if __name__ == '__main__':
    main()
