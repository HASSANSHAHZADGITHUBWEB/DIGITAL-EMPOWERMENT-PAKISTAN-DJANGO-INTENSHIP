import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = "https://www.pbs.gov.pk/contacts"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extract data from table rows (you can customize this part)
    table = soup.find('table')
    rows = table.find_all('tr')

    # Create a list to hold the data
    data = []

    # Loop through the rows and extract the data
    for row in rows:
        columns = row.find_all('td')
        columns = [col.text.strip() for col in columns]
        data.append(columns)

    # Convert the list into a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv('scraped_data.csv', index=False)

    print("Data has been scraped and saved to scraped_data.csv")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
