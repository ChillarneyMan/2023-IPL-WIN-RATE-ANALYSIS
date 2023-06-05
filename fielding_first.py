import pandas as pd

from base import cutsom_bar_chart

def field_bat_win_rate(IPL_data: pd.DataFrame) -> pd.DataFrame:
    field_data = IPL_data[IPL_data['toss_decisions'] == 'Field']
    bat_data = IPL_data[IPL_data['toss_decisions'] == 'Bat']
    field_winners = field_data[field_data['toss_winner'] == field_data['winner']]
    bat_winners = bat_data[bat_data['toss_winner'] == bat_data['winner']]
    field_win_rate = len(field_winners) / len(field_data)
    bat_win_rate = len(bat_winners) / len(bat_data)

    # Create a DataFrame to plot
    data = {

        'Metrics': ['Field', 'Bat'],
        'Rates': [field_win_rate, bat_win_rate]

    }

    df = pd.DataFrame(data)

    #plot bar chart
    cutsom_bar_chart(df, data['Metrics'], data['Rates'],
                     'Toss Decision Win Rates', 'Field or Bat', 'Win Rates',
                     'Field_Bat_Win_Rate.png')
    return df




def main():
    IPL_data = pd.read_csv('data/2023 IPL Teams.csv')

    field_bat_data = field_bat_win_rate(IPL_data)

    print(field_bat_data)

if __name__ == '__main__':
    main()

