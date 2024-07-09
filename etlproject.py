import pandas as pd
import requests
from bs4 import BeautifulSoup

# Importing the required libraries

def extract(url):
    ''' This function extracts the required
    information from the website and saves it to a dataframe. The
    function returns the dataframe for further processing. '''
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table with the required attributes
        table = soup.find('table', attrs=table_attribs)
        
        # Convert the HTML table into a DataFrame
        df = pd.read_html(str(table))[0]
        
        return df
    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
        return None

def transform(df):
    ''' This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.'''
    
    # Example transformation (modify as per your specific data format)
    df['GDP (Billions USD)'] = df['GDP (Millions USD)'] / 1000.0
    
    # Round GDP to 2 decimal places
    df['GDP (Billions USD)'] = df['GDP (Billions USD)'].round(2)
    
    return df

def load_to_csv(df, csv_path):
    ''' This function saves the final dataframe as a `CSV` file 
    in the provided path. Function returns nothing.'''
    
    df.to_csv(csv_path, index=False)
    print(f"Data successfully saved to {csv_path}")

# URL and table attributes
url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_attribs = {'class': 'wikitable'}

# Extracting data
df = extract(url)

# Transforming data
if df is not None:
    df_transformed = transform(df)
    
    # Saving to CSV
    csv_path = 'country_gdp_data.csv'
    load_to_csv(df_transformed, csv_path)