import matplotlib.pyplot as plt
import pandas as pd

def plot_gdp(df_gdp: pd.DataFrame) -> None:
    df_gdp = df_gdp.set_index('Country')
    df_gdp.T.plot()
    plt.ylabel('GDP (current US$)')

def plot_gdp_ggplot(df_gdp: pd.DataFrame) -> None:
    plt.style.use('ggplot')
    df_gdp = df_gdp.set_index('Country')
    df_gdp.T.plot(kind='bar')
    plt.ylabel('GDP (current US$)')