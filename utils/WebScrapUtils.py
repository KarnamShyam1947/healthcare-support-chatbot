from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import os

load_dotenv()

def map_schemes(raw_data):
    scheme = {
        "id": raw_data["slug"],
        "name": raw_data["schemeName"],
        "shortDescription": raw_data["briefDescription"],
        "category": raw_data["schemeCategory"][0],
        "state": raw_data["beneficiaryState"][0]
    }
    
    return scheme

def get_all():
    BASE_URL = 'https://api.myscheme.gov.in/search/v4/schemes?lang=en&q=[{"identifier":"schemeCategory","value":"Health %26 Wellness"}]&from=0&size=30'
    headers = {
        "x-api-key" : os.getenv("SCHEME_API_KEY")
    }

    data = requests.get(BASE_URL, headers=headers)
    json_data = data.json()
    schemes = json_data['data']['hits']['items']

    schemes = [map_schemes(scheme['fields']) for scheme in schemes]
    
    return schemes

def get(scheme):
    BASE_URL = f"https://www.myscheme.gov.in/schemes/{scheme}"

    html_doc = requests.get(url=BASE_URL)
    html_content = html_doc.content

    print("Scraping.............")
    soup = BeautifulSoup(html_content, 'html.parser')

    result = dict()
    
    name = soup.find('h1', class_='font-bold text-xl sm:text-2xl text-[#24262B] dark:text-white').text.strip()
    
    # Extract the state name
    state = soup.find('h3', class_='text-raven dark:text-indigo-100 text-base mt-2 hover:underline cursor-pointer').text.strip()

    # Extract the tags under the <div> with title attributes

    tags = [tag.text.strip() for tag in soup.find_all('div', title=True)]
    tags = tags if len(tags) <= 6 else tags[0:6]
    # print("Details : ")
    
    details = ""
    schemes = soup.find_all("div", id="details")
    # print(schemes[0].find_all())
    d1 = schemes[0].find_all("div", class_="mb-2")
    for d in d1:
        # print(d.text.strip())
        details += d.text.strip()


    application_process = []
    schemes = soup.find_all("div", id="application-process")
    d1 = schemes[0].find_all("li")
    if len(d1) != 0:
        for d in d1:
            # print(d.text.strip())
            application_process.append(d.text.strip())

    else:
        d1 = schemes[0].find_all("div", class_="mb-2")
        d1[1:]
        for idx, d in enumerate(d1):
            # print(idx, "   ", d.text.strip())
            application_process.append(d.text.strip())
                    
    documents_required = list()
    schemes = soup.find_all("div", id="documents-required")
    d1 = schemes[0].find_all("li")
    for d in d1:
        documents_required.append(d.text.strip())

    benefits = list()
    schemes = soup.find_all("div", id="benefits")
    d1 = schemes[0].find_all("blockquote")
    if len(d1) != 0:
        for d in d1:
            benefits.append(d.get_text().strip())
        
    else:
        d1 = schemes[0].find_all("li")
        for d in d1:
            benefits.append(d.text.strip())

    eligibility = []
    schemes = soup.find_all("div", id="eligibility")
    d1 = schemes[0].find_all("li")
    for d in d1:
        eligibility.append(d.text.strip())
        
    result['description'] = details
    result['applicationProcess'] = application_process
    result['documents'] = documents_required
    result['benefits'] = benefits
    result['eligibility'] = eligibility
    result['state'] = state
    result['tags'] = tags
    result['name'] = name
    result['id'] = scheme
    result['category'] = "HealthCare"

    return result
