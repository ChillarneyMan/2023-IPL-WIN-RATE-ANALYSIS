"""
Base module for IPL analysis. Contains the Team class, list of teams, 
and some used functions like calculating win rate.
"""
import pandas as pd
import plotly.express as px

import plotly.graph_objs as go
import plotly.io as pio

import os


class Team:
    """
    Team model.

    Attributes:
        name (str): Name of the team.
        stadium (str): Name of the stadium. 
    """
    def __init__(self, name: str, stadium: str, bowl_data: str = "", batting_data: str = "") -> None:
        self.name = name
        self.stadium = stadium
        self.bowl_data = bowl_data
        self.batting_data = batting_data


TEAMS: list[Team] = [
    Team(name='Royal Challengers Bangalore', stadium='M. Chinnaswamy Stadium', bowl_data="data/Royal Challengers Bangalore Bowling.csv", batting_data='data/Royal Challengers Bangalore Batting.csv'),
    Team(name='Chennai Super Kings', stadium='M. A. Chidambaram Stadium', bowl_data="data/Chennai Super Kings Bowling.csv", batting_data="data/Chennai Super Kings Batting.csv"),
    Team(name='Gujarat Titans', stadium='Narendra Modi Stadium', bowl_data="data/Gujarat Titans Bowling.csv", batting_data="data/Gujarat Titans Batting.csv"),
    Team(name='Kolkata Knight Riders', stadium='Eden Gardens', bowl_data="data/Kolkata Knight Riders Bowling.csv", batting_data='data/Kolkata Knight Riders Batting.csv'),
    Team(name='Punjab Kings', stadium='Inderjit Singh Bindra Stadium', bowl_data="data/Punjab Kings Bowling.csv", batting_data='data/Punjab Kings Batting.csv'),
    Team(name='Lucknow Super Giants', stadium='BRSABV Ekana Cricket Stadium', bowl_data="data/Lucknow Super Giants Bowling.csv", batting_data='data/Lucknow Super Giants Batting.csv'),
    Team(name='Delhi Capitals', stadium='Arun Jaitley Stadium', bowl_data="data/Delhi Capitals Bowling.csv", batting_data='data/Delhi Capitals Batting.csv'),
    Team(name='Mumbai Indians', stadium='Wankhede Stadium', bowl_data="data/Mumbai Indians Bowling.csv", batting_data='data/Mumbai Indians Batting.csv'),
    Team(name='Sunrisers Hyderabad', stadium='Rajiv Gandhi International Cricket Stadium', bowl_data="data/Sunrisers Hyderabad Bowling.csv", batting_data='data/Sunrisers Hyderabad Batting.csv'),
    Team(name='Rajasthan Royals', stadium='Sawai Mansingh Stadium', bowl_data="data/Rajasthan Royals Bowling.csv", batting_data='data/Rajasthan Royals Batting.csv')
]


# Create plots folder if it doesn't exist
if not os.path.exists('plots'):
    os.mkdir('plots')


def plot_figure(figure: go.Figure, file_name: str) -> None:
    """
    Plot a figure and save it as a png file.

    Args:
        figure (go.Figure): Figure to plot.
        file_name (str): Name of the file to save the plot.

    Returns:
        None, saves the plot as a png file.
    """
    pio.write_image(figure, os.path.join("plots", file_name))


def plot_bar_chart(data_frame: pd.DataFrame, x: str, y: str, title: str, color: str, file_name: str) -> None:
    """
    Plot a bar chart given a DataFrame and save it as a png file.

    Args:
        data_frame (pd.DataFrame): DataFrame to plot.
        x (str): Name of the x-axis.
        y (str): Name of the y-axis.
        title (str): Title of the plot.
        file_name (str): Name of the file to save the plot.

    Returns:
        None, saves the plot as a png file.
    """
    fig = px.bar(data_frame, x=x, y=y, color=color, title=title)
    fig.update_layout(showlegend=False)
    plot_figure(fig, file_name)


def cutsom_bar_chart(data_frame: pd.DataFrame, x: str, y: str, title: str, xaxis_title: str, yaxis_title: str, file_name: str) -> None:
     
     fig = go.Figure(data=[
         go.Bar(x=x, y=y)])
     
     fig.update_layout(
         title = title,
         xaxis_title = xaxis_title,
         yaxis_title = yaxis_title,
     )
     plot_figure(fig, file_name)


def home_away_win_rate(IPL_data: pd.DataFrame, team: Team) -> tuple[float, float]:
    """
    Calculate the home and away win rate for a given team.

    Args:
        IPL_data (pd.DataFrame): IPL data by team.
        team (Team): Team to calculate the win rate for.

    Returns:
        tuple[float, float]: Home and away win rate for the given team.
    """
    data = IPL_data[['team1', 'team2', 'winner', 'venue']]
    data = data[(data['team1'] == team.name) | (data['team2'] == team.name)]
    home_data = data[(data['venue'] == team.stadium)]
    away_data = data[(data['venue'] != team.stadium)]
    home_wins = home_data[(home_data['winner'] == team.name)]
    away_wins = away_data[(away_data['winner'] == team.name)]
    return (len(home_wins) / len(home_data)), (len(away_wins) / len(away_data))
