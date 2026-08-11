from clean import clean_data as cd

def normalize_job(raw_job):
    return {
        "title": raw_job.get("title"),
        "company": raw_job.get("company", {}).get("display_name"),
        "location": raw_job.get("location", {}).get("display_name"),
        "salary_min": raw_job.get("salary_min"),
        "salary_max": raw_job.get("salary_max"),
        "contract_type": raw_job.get("contract_type"),
        "contract_time": raw_job.get("contract_time"),
        "created": raw_job.get("created"),
        "description": raw_job.get("description"),
        "url": raw_job.get("redirect_url"),
        "adzuna_id": raw_job.get("id")
    }

def normalize_all_jobs(raw_data):
    clean_data = [
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

    for i in range(len(raw_data)):

        for raw_job in raw_data[i][1]:
            clean_data[i][1].append(normalize_job(raw_job))

    cd.save_clean_data(clean_data)

    

    
