from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(_name_)

def scrape_jobs():
    url = "https://remoteok.io/remote-dev-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    for job in soup.find_all('tr', class_='job'):
        title = job.find('h2', itemprop='title')
        company = job.find('h3', itemprop='name')
        if title and company:
            jobs.append({
                'title': title.text.strip(),
                'company': company.text.strip()
            })
    print(f"Scraped {len(jobs)} jobs")  # Debug line
    return jobs

@app.route('/')
def home():
    jobs = scrape_jobs()
    return f"Scraping complete. Found {len(jobs)} jobs."

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
