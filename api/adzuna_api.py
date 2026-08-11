import requests
from config import ADZUNA_APP_ID, ADZUNA_APP_KEY
from raw import raw_data as rd

app_id = ADZUNA_APP_ID
app_key = ADZUNA_APP_KEY

def get_raw_jobs(term):
    raw_jobs = []

    for i in range (1, 20):
        url = f"https://api.adzuna.com/v1/api/jobs/br/search/{i}"

        params = {
            "app_id": app_id,
            "app_key": app_key,
            "where": "Rio de Janeiro",
            "what": term,
            "results_per_page": 20,
            "content-type": "application/json"
        }
        
        response = requests.get(url, params=params)

        response.raise_for_status()

        data = response.json()

        raw_results = data['results']

        for j in range(0, len(raw_results)):
            raw_jobs.append(raw_results[j])

        if len(raw_results) < 20:
            break

    return raw_jobs

def search_all_terms():
    JOB_SEARCH_TERMS = [
        ["software developer", []],
        ["software engineer", []],
        ["backend developer", []],
        ["frontend developer", []],
        ["full stack developer", []],
        ["data analyst", []],
        ["data scientist", []],
        ["machine learning engineer", []],
        ["devops engineer", []],
    ]

    for term in JOB_SEARCH_TERMS:
        term[1] = get_raw_jobs(term[0])

    rd.save_raw_data(JOB_SEARCH_TERMS)




