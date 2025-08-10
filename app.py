from scraper import scrape_jobs
from flask import Flask
app = Flask(_name_)

@app.route('/')
def run_scraper():
    # 🟢 Import and run your scraper function here
    result = scrape_jobs()  # replace with your actual scraper function name
    return f"Scraping done. Found {len(result)} jobs."
if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
