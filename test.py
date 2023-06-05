import correlations
import base
import home_advantage
import fielding_first
from cse163_utils import assert_equals
import pandas as pd


def test_team_average_economy(gujarat_test_data):
    assert_equals(7.94, correlations.team_average_economy(gujarat_test_data))


def test_team_average_strikerate(gujarat_test_data):
    assert_equals(145.64,
                  correlations.team_average_strikerate(gujarat_test_data))


def test_home_away_win_rate(IPL_test, gujarat_test_data):
    assert_equals((0.5, 1), base.home_away_win_rate(IPL_test,
                                                    gujarat_test_data))
    

def test_home_ground_advantage(IPL_test, teams_list):
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