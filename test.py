import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',  # Do Not Track Request Header
        }
        
        # Initialize a session
        session = requests.Session()
        
        # Send a GET request with headers and handle cookies
        response = session.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError on a bad status
        
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def extract_job_details(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    job_details = {}

    # Example selectors - these need to be adjusted based on the actual HTML structure
    job_details['title'] = soup.find('h1', class_='job-title').get_text(strip=True)
    job_details['company'] = soup.find('a', class_='company-name').get_text(strip=True)
    job_details['location'] = soup.find('span', class_='job-location').get_text(strip=True)
    job_details['description'] = soup.find('div', class_='job-description').get_text(strip=True)

    return job_details

def save_to_file(job_details, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for key, value in job_details.items():
                file.write(f"{key}: {value}\n\n")
        print(f"Job details saved to {filename}")
    except IOError as e:
        print(f"An error occurred while writing to file: {e}")

def main():
    url = 'https://www.linkedin.com/jobs/search/?currentJobId=3918800454'  # Replace with the actual job posting URL
    
    html_content = fetch_html(url)
    
    if html_content:
        job_details = extract_job_details(html_content)
        save_to_file(job_details, 'job_details.txt')

if __name__ == '__main__':
    main()

