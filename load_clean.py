import pandas as pd

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
    print(df.head())

    # return loaded DataFrame
    return df

# Call the function and store the result in the gdp_data variable
gdp_data = load_csv("C:\\Users\\psingh\\Desktop\\Personal\\Cambridge\\Year 1\\D100\\gdp_rep0_structure\\gdp_data.csv")

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

    print(df_clean.head(8))

# Clean the data
gdp_cleaned = clean_data(gdp_data)

                     


