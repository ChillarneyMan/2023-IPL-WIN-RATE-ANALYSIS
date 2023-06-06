"""
Arnav Khare & Aditi Manjunath
CSE 163
This is a file that implements the team_average_economy function and
team_average_strikerate function
"""
# Data
import pandas as pd
import numpy as np
# Plotting
import plotly.graph_objs as go
# Project
import base


# Get available teams (data is available)
both_available_teams = [team for team in base.TEAMS if all((team.bowl_data,
                        team.batting_data))]
bowl_available_teams = [team for team in base.TEAMS if team.bowl_data]
bat_available_teams = [team for team in base.TEAMS if team.batting_data]


# ---- Calculations ----
def team_average_economy(team: base.Team) -> float:
    """
    Calculate the average economy of a team.

    Args:
        team (main.Team): The team to calculate the average economy for.

    Returns:
        float: The average economy of the team.
    """
    bowl_data = pd.read_csv(team.bowl_data)
    return bowl_data['Economy'].mean()


def team_average_strikerate(team: base.Team) -> float:
    """
    Calculate the average strike rate of a team.

    Args:
        team (main.Team): The team to calculate the average strike rate for.

    Returns:
        float: The average strike rate of the team.
    """
    bat_data = pd.read_csv(team.batting_data)
    return bat_data['Strike Rate'].mean()


def main():
    # Get IPL data
    ipl_data = pd.read_csv('data/2023 IPL Teams.csv')
    # ---- Bowling Plots ----

    economies = [team_average_economy(team) for team in bowl_available_teams]
    winrates = [np.mean(base.home_away_win_rate(ipl_data, team))
                for team in bowl_available_teams]
    team_names = [team.name for team in bowl_available_teams]
    bowl_stats = [
        go.Scatter(
            x=[e],
            y=[w],
            mode='markers',
            name=t
        ) for e, w, t in zip(economies, winrates, team_names)
    ]
    bowl_layout = go.Layout(
        title='Economy vs Win Rate',
        xaxis=dict(
            title='Economy'
        ),
        yaxis=dict(
            title='Win Rate'
        ),
        showlegend=True
    )
    fig = go.Figure(data=bowl_stats, layout=bowl_layout)
    base.plot_figure(fig, "economy_winrate.png")

    # ---- Batting Plots ----
    strikerates = [team_average_strikerate(team)
                   for team in bat_available_teams]
    winrates = [np.mean(base.home_away_win_rate(ipl_data, team))
                for team in bat_available_teams]
    team_names = [team.name for team in bat_available_teams]
    bat_stats = [
        go.Scatter(
            x=[s],
            y=[w],
            mode='markers',
            name=t
        ) for s, w, t in zip(strikerates, winrates, team_names)
    ]
    bat_layout = go.Layout(
        title='Strike Rate vs Win Rate',
        xaxis=dict(
            title='Strike Rate'
        ),
        yaxis=dict(
            title='Win Rate'
        ),
        showlegend=True
    )
    fig = go.Figure(data=bat_stats, layout=bat_layout)
    base.plot_figure(fig, 'strikerate_winrate.png')


if __name__ == '__main__':
    main()
