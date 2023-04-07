import requests
import csv

# Replace YOUR_API_KEY with your IMDb API key
API_KEY = '1zIyjGxMlnvITonvhlnvYEHEnbvhebvx'

# Define the base URL for IMDb API requests
BASE_URL = f'https://developer.imdb.com/?ref_=adx-bulk-essential/key/?apikey={API_KEY}'

# Define the list of fields to retrieve for each movie
FIELDS = ['Title', 'Year', 'Genre', 'Language', 'Country', 'Actors', 'Director', 'imdbRating', 'BoxOffice']

# Define the number of records to retrieve
NUM_RECORDS = 1500

# Define the output file name
OUTPUT_FILE = 'movies.csv'

# Define the headers for the CSV file
HEADERS = ['Title', 'Year', 'Genre', 'Language', 'Country', 'Starring Role', 'Director', 'IMDb Rating', 'Box Office']

# Make the requests to the IMDb API and write the results to the CSV file
with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(HEADERS)
    for i in range(1, NUM_RECORDS+1):
        # Make the request to the IMDb API for the movie information
        url = f'{BASE_URL}&type=movie&page={i}'
        response = requests.get(url)
        data = response.json()
        
        # Extract the relevant fields from the movie information
        row = []
        for field in FIELDS:
            if field in data:
                row.append(data[field])
            else:
                row.append('')
        
        # Write the movie information to the CSV file
        writer.writerow(row)

        # Sleep for a random interval between 1 and 5 seconds to avoid overloading the API
        time.sleep(random.uniform(1, 5))
