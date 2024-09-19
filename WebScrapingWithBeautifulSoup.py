from bs4 import BeautifulSoup
import requests # For sending HTTP requests
import time # For adding delays between requests

# Base URL of the website to scrape
root = "https://subslikescript.com"

# Fetch the initial page listing movies starting with 'A'
result = requests.get(f"{root}/movies_letter-A") # Can be tweaked to scrape more pages if needed
content = result.text

# Parse the HTML content of the page
soup = BeautifulSoup(content,'lxml')

# Locate the pagination section to determine the number of pages
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')

# Extract the last page number
last_page = pages[-2].get_text()
links = []

# Pagination: Loop through the pages
for page in range(1, int(last_page)+1):
    result = requests.get(f"{root}/movies_letter-A?page={page}")
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    # Find the section containing movie links
    box = soup.find('article', class_='main-article')

    # Extract all links to individual movie pages
    for link in box.find_all('a', href=True):
        links.append(link['href'])

    # Prefix each link with the base URL
    for i in range(len(links)):
        links[i] = f"{root}{links[i]}"

    # Loop through each link and scrape the movie transcript
    for link in links:
        try:
            # print(link)
            result = requests.get(link)
            content = result.text
            soup = BeautifulSoup(content, 'lxml')

            # Extract the title and the transcript content
            box = soup.find('article', class_='main-article')
            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator='.')

            # Save the transcript as a text file named after the movie title
            with open(f"{title}.txt", "w") as file:
                file.write(transcript)

        # Error handling in case of broken links or issues during requests
        except:
            print("--------Link not working!!!!!!!-------")
            print(link)
            pass

        # Delay to avoid overwhelming the server
        time.sleep(1)


