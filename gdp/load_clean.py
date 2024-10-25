import csv
import pandas as pd
import pandas as pd
import requests
from typing import List


def load_gdp_by_country(country: str) -> pd.DataFrame:
    """
    Load gdp by country via EODHD API. Free tier user and can only query 20 times a day.
    Parameters:
    country (str): Country to load.
    
    Returns:
    DataFrame: Loads data as a pandas DataFrame.
    """
    url = f"https://eodhd.com/api/macro-indicator/{country}?indicator=gdp_current_usd&api_token=65549defed6b89.08154842&fmt=csv"
    data = requests.get(url).text
    myreader = csv.reader(data.splitlines())
    return pd.DataFrame(myreader)

def load_gdp(country_list: List[str]) -> pd.DataFrame:
    """
    Load gdp by country via EODHD API. Free tier user and can only query 20 times a day.
    Parameters:
    country_list (List[str]): List of countries to load.
    
    Returns:
    DataFrame: Loads data as a pandas DataFrame.
    """
    df_gdp = pd.DataFrame()
    for country in country_list:
        df_gdp = pd.concat([df_gdp, load_gdp_by_country(country)])
    return df_gdp


def load_csv(file_path):
    """
    Function to load a CSV file using pandas.
    
    Parameters:
    file_path (str): Path to the CSV file.
    
    Returns:
    DataFrame: Loads data as a pandas DataFrame.
    """
    # Load the CSV file
    df = pd.read_csv(file_path)

    # For previewing data
    # print(df.head())

    # return loaded DataFrame
    return df

def clean_data(df):
    """
    Function to clean the loaded GDP data.
    
    Parameters:
    df (DataFrame): The raw DataFrame loaded from the CSV file.
    
    Returns:
    DataFrame: Cleaned DataFrame, filtered for years 2000-2022.
    """
    # Drop the second row assuming it is blank
    df = df.drop(index=0)

    # Rename the 'Country' column to 'Country (GDP, current prices)'
    df = df.rename(columns={'GDP, current prices (Purchasing power parity; billions of international dollars)': 'Country'})

    # Filter columns for the years 2000 to 2022, assuming the year columns exist as actual years
    year_columns = [str(year) for year in range(2000, 2023)]
    
    # Select only the relevant year columns'
    country_column = 'Country'
    
    columns_to_keep = [country_column] + year_columns
    df_clean = df[columns_to_keep]

    return df_clean


                     


