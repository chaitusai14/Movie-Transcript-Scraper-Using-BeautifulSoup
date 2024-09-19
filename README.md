# Movie Transcript Scraper using BeautifulSoup

This project is a Python-based web scraper designed to scrape movie transcripts from [Subslikescript.com](https://subslikescript.com), a website that hosts movie scripts and subtitles. The script fetches all movie transcripts that start with the letter 'A' and stores them locally as text files. The tool leverages `BeautifulSoup` for parsing HTML content and `requests` for sending HTTP requests.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Error Handling](#error-handling)
- [Improvements and Customization](#improvements-and-customization)
- [Contribution](#contribution)

## Features

- **Automated Web Scraping**: Automatically extracts movie links from paginated lists and retrieves transcript data from individual movie pages.
- **Efficient Pagination Handling**: Scrapes multiple pages by detecting the number of pages and iterating through them.
- **Error Handling**: Detects and logs broken links to ensure the scraping process continues despite errors.
- **Throttled Requests**: Introduces a delay between requests to avoid overwhelming the server or being blocked.

## Prerequisites

To run this script, ensure that you have Python 3.x installed on your machine and that the following dependencies are available:

### Dependencies
- **BeautifulSoup4**: For parsing the HTML content of web pages.
- **requests**: For sending HTTP requests to the website.
- **lxml**: For fast HTML parsing.

You can install the required libraries using the following command:

```bash
pip install beautifulsoup4 requests lxml
```

## How It Works

1. **Initial Request**: The script starts by sending an HTTP GET request to the page that lists all movies starting with the letter "A".
2. **Parse HTML**: The HTML content is parsed using `BeautifulSoup` to extract the pagination information (i.e., how many pages of movie listings exist).
3. **Iterate Pages**: The script loops through each page in the pagination and extracts links to individual movie pages.
4. **Scrape Movie Data**: For each movie link, the script fetches the movie title and its transcript.
5. **Save to File**: Each movie transcript is saved as a `.txt` file named after the movie title in the local directory.

### Key Components:
- **Base URL**: The root URL of the website is defined as `https://subslikescript.com`.
- **Pagination Handling**: The script finds the pagination element and determines the total number of pages to iterate through.
- **Link Extraction**: Each page contains a list of movies, and their individual links are extracted and stored for further processing.
- **Transcript Retrieval**: For each movie page, the transcript and title are fetched, and the content is saved in a text file.

### Delay Between Requests
The script introduces a 1-second delay between requests to avoid overwhelming the website and to mimic human browsing behavior. This delay can be modified in the code as needed.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/chaitusai14/Movie-Transcript-Scraper-Using-BeautifulSoup.git
cd movie-transcript-scraper
```

2. Run the scraper:

```bash
python WebScrapingWithBeautifulSoup.py
```

3. The transcripts will be saved in the current directory as `.txt` files, named after the movie title.

## Error Handling

The script contains basic error handling to log any issues related to broken links or failed HTTP requests. If a link fails, it prints an error message with the faulty URL but continues scraping the remaining pages.

```plaintext
--------Link not working!!!!!!!-------
<faulty-link>
```

### Improvements and Customization

Feel free to modify or extend the script for your specific needs. Some potential improvements include:
- **Randomized Delay**: Introduce a random delay between requests to further mimic human browsing behavior.
- **Extended Character Support**: Ensure that movie titles are sanitized before saving files to avoid issues with special characters in file names.
- **Concurrency**: Implement asynchronous requests or multiprocessing to speed up the scraping process.
- **Enhanced Error Handling**: Improve the error handling by specifying exceptions and adding retries for failed requests.

## Contribution

Contributions are welcome! Please feel free to open issues, submit pull requests, or fork the repository to add more features or improve the existing code.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a pull request

