from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

def scrape_wuzzuf(pages=41, progress_callback=None):
    """
    Scrape job data from Wuzzuf website
    
    Args:
        pages: Number of pages to scrape
        progress_callback: Optional function to report progress
    """
    job_title = []
    companies = []
    locations = []
    employment_types = []
    work_modes = []
    skills = []

    for i in range(0, pages):
        try:
            # Report progress if callback exists
            if progress_callback:
                progress_callback(i, pages, f"Scraping page {i+1} of {pages}...")
            
            response = requests.get(
                f"https://wuzzuf.net/search/jobs?q=data%20&start={i}&a=hpb",
                timeout=10,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
            )

            soup = BeautifulSoup(response.text, 'html.parser')
            jobs = soup.find_all('div', class_="css-pkv5jc")

            for job in jobs:
                # Job Title
                title_elem = job.find('a', class_="css-o171kl")
                title = title_elem.text if title_elem else "N/A"
                job_title.append(title)

                # Company
                company_elem = job.find('a', class_="css-ipsyv7")
                company = company_elem.text if company_elem else "N/A"
                companies.append(company)

                # Location
                location_elem = job.find('span', class_="css-16x61xq")
                location = location_elem.text if location_elem else "N/A"
                locations.append(location)

                # Employment Type
                emp_type_elem = job.find('span', class_="css-uc9rga eoyjyou0")
                employment_type = emp_type_elem.text if emp_type_elem else "N/A"
                employment_types.append(employment_type)

                # Work Mode
                work_mode_elem = job.find('span', class_="css-uofntu eoyjyou0")
                work_mode = work_mode_elem.text if work_mode_elem else 'None'
                work_modes.append(work_mode)

                # Skills
                all_skills = job.find_all('a', class_="css-o171kl")
                skill = [skill.text for skill in all_skills]
                skills.append(' '.join(skill) if skill else 'None')

            time.sleep(1)  # Be respectful to the server

        except Exception as e:
            print(f"Error on page {i}: {e}")
            continue

    df = pd.DataFrame({
        "job_title": job_title,
        "companies": companies,
        "locations": locations,
        "employment_types": employment_types,
        "work_modes": work_modes,
        "skills": skills
    })
    df['scrape_date'] = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M")

    return df