import csv
from typing import List
import pandas as pd
import requests

def load_gdp_by_country(country: str) -> pd.DataFrame:
    url = f"https://eodhd.com/api/macro-indicator/{country}?indicator=gdp_current_usd&api_token=65549defed6b89.08154842&fmt=csv"
    data = requests.get(url).text
    myreader = csv.reader(data.splitlines())
    return pd.DataFrame(myreader)

def load_gdp(country_list: List[str]) -> pd.DataFrame:
    df_gdp = pd.DataFrame()
    for country in country_list:
        df_gdp = pd.concat([df_gdp, load_gdp_by_country(country)])
    return df_gdp