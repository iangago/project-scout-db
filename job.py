# DATA STRUCTURE
#                "title": "Software Developer, Full Stack",
#                "company": "Katalyst Data Management",
#                "location": "Jo\u00e1, Rio de Janeiro",
#                "salary_min": null,
#                "salary_max": null,
#                "contract_type": null,
#                "contract_time": null,
#                "created": "2026-05-21T17:55:44Z",
#                "description": "Join the dynamic and collaborative team at Katalyst Data Management (KDM)! KDM is seeking an Intermediate Software Developer \u2013 Full Stack who thrives on solving complex problems and building modern, high \u2011 performance web applications. This is an exciting opportunity to work across the full technology stack \u2014 leveraging .NET 6, React, APIs, and SQL \u2014 to develop scalable solutions that support the oil and gas industry. Ideal candidates are comfortable working with minimal supervision, collaborat\u2026",
#                "url": "https://www.adzuna.com.br/details/5736881780?utm_medium=api&utm_source=d50a3d1c",
#                "adzuna_id": "5736881780"

def get_company_id(conn, company_name):
    #if its null
    if not company_name:
        return company_name

    id = conn.execute(
            "SELECT id FROM company WHERE name = ?",
            (company_name,) 
        ).fetchone()

    if id:
        return id[0]
    else:
        return id

def validate_job(clean_job):
    if not clean_job["title"] or not clean_job["adzuna_id"] or not clean_job["url"]:    
        print(f"{clean_job["title"]} Job Not Valid")
        return False
    else:
        return True

def insert_company(conn, company_name):
    #if its null
    if not company_name:
            return company_name

    # checks if it already exists
    id = get_company_id(conn, company_name)

    # if it doesnt it inserts
    if not id:
        with conn:
            conn.execute("""
                INSERT INTO company (name)
                VALUES (?)
                """, (company_name,)
            )

        id = get_company_id(conn, company_name)

    return id

def get_employment_type_id(conn, contract_type, contract_time):
    #I got both contract time and contract type wich could be deterimined to be the same employment type field
    if not contract_type and not contract_time:
        return contract_type

    #Here im giving priority to contract type field because its more descriptive
    if contract_type:
        id = conn.execute(
                    "SELECT id FROM employment_type WHERE name LIKE ?",
                    (contract_type,) 
                ).fetchone()

        if id:
            return id[0]
        else:
            return id

    if contract_time:
        id = conn.execute(
            "SELECT id FROM employment_type WHERE name LIKE ?",
            (contract_time,) 
        ).fetchone()

        if id:
            return id[0]
        else:
            return id


def insert_job(conn, clean_job):
    valid_job = validate_job(clean_job)

    if not valid_job:
        pass
    else:
        conn.execute("""
            INSERT INTO job (
                company_id,
                external_id,
                url,
                title,
                description,
                salary,
                location,
                employment_type_id,
                created_at      
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(external_id) DO NOTHING
        """, (
            insert_company(conn, clean_job["company"]),
            clean_job["adzuna_id"],
            clean_job["url"],
            clean_job["title"],
            clean_job["description"],
            clean_job["salary_min"],
            clean_job["location"],
            get_employment_type_id(conn, clean_job["contract_type"], clean_job["contract_time"]),
            clean_job["created"]
        ))
