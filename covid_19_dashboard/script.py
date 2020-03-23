import pandas as pd
import git


'''
    This function uses GitPython to pull from the CSSE COVID-19 Github
    and updates any changes.
'''
def update_covid19_repo():
    repo = git.Repo('../../COVID-19/')
    current = repo.head.commit

    # Pulls for any updates
    repo.remotes.origin.pull()

    # Check if any updates
    if current == repo.head.commit:
        print("No changes. Up to date.")
    elif current != repo.head.commit:
        print("Updates were made.")


'''
    This function reads csv from JHU CSSE COVID-19 Github Github folder and filters data 
    to retrieve weekly confirmed cases for all 52 states in the US. 

    https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv

'''
def get_weekly_stats():
    data = pd.read_csv('../../COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')

    # First 170 rows in file, to eliminate US counties for now
    data = data.head(170)

    # Reading the headers
    # print(data.columns)

    # Get weekly data from all 52 states
    weekly_data = data.loc[data['Country/Region'] == "US"]

    # Gives syntax error??
    # weekly_data = weekly_data.iloc[[0:2] + [-7:]]

    weekly_data = weekly_data.iloc[:, [0, 1, -7, -6, -5, -4, -3, -2, -1]]

    # Sort data from most confirm cases to least
    weekly_data = weekly_data.sort_values(data.columns[-1], ascending = False)

    # Save weekly modified CSV and JSON file
    weekly_data.to_csv('covid-19_weekly-modified-csv.csv')
    weekly_data.to_json('covid-19_weekly-modified-json.json')


# Run functions: 1) Update COVID-19 repository 2) Update modified CSV with recent changes
update_covid19_repo()
get_weekly_stats()