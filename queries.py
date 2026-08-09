# =====================================
# BASIC EXPLORATION
# =====================================

# Total users
def total_users_query():
    print("Total users:\n")

    query = """
    SELECT COUNT(id) AS Total_users
    FROM user
    """

    return query

# Total jobs
def total_jobs_query():
    print("Total jobs:\n")

    query = """
    SELECT COUNT(id) AS Total_jobs
    FROM job
    """

    return query

# Total companies
def total_companies_query():
    print("Total companies:\n")

    query = """
    SELECT COUNT(id) AS Total_companies
    FROM company
    """

    return query

# =====================================
# COMPANY ANALYTICS
# =====================================

# Companies with the most openings
def companies_most_openings_query():
    print("Companies with the most openings:\n")

    query = """
    SELECT company_id, company.name, COUNT(company_id) AS openings
    FROM job
    JOIN company
        ON job.company_id = company.id
    GROUP BY company.id
    ORDER BY COUNT(company_id) DESC
    """

    return query

# Average salary by company
def avg_salary_companies_query():
    print("Average salary by company:\n")

    query = """
    SELECT company_id, company.name, AVG(job.salary) AS average_salary
    FROM job
    JOIN company
        ON job.company_id = company.id
    GROUP BY company.id
    ORDER BY AVG(job.salary) DESC
    """

    return query

# Highest paying companies
def highest_paying_companies_query():
    print("Highest paying skills:\n")

    query = """
    SELECT company_id, company.name, job.salary AS salary
    FROM job
    JOIN company
        ON job.company_id = company.id
    ORDER BY job.salary DESC
    """

    return query

# =====================================
# SKILL ANALYTICS
# =====================================

# Most requested skills
def most_requested_skills_query():
    print("Most requested skills:\n")

    query = """
    SELECT skill.name, COUNT(skill.id) AS appearances
    FROM jobskill
    JOIN skill
        ON jobskill.skill_id = skill.id
    GROUP BY skill.id
    ORDER BY COUNT(skill.id) DESC
    """

    return query

# Skills required for AI jobs
def skills_ai_jobs_query():
    print("Skills required for AI jobs:\n")

    query = """
    SELECT skill.name, COUNT(skill.id) AS appearances
    FROM jobskill
    JOIN skill
        ON jobskill.skill_id = skill.id
    JOIN job
        ON jobskill.job_id = job.id
    WHERE job.title LIKE "%AI%" OR job.title LIKE "%machine learning%"
    GROUP BY skill.id 
    ORDER BY COUNT(skill.id) DESC
    """

    return query

# Skills required for internships
def skills_internships_query():
    print("Skills required for internships:\n")

    query = """
    SELECT skill.name, COUNT(skill.id) AS appearances
    FROM jobskill
    JOIN skill
        ON jobskill.skill_id = skill.id
    JOIN job
        ON jobskill.job_id = job.id
    JOIN level
        ON job.level_id = level.id    
    WHERE level.name = "Intern"
    GROUP BY skill.id 
    ORDER BY COUNT(skill.id) DESC
    """

    return query

# =====================================
# USER ANALYTICS
# =====================================

# Users with the most applications
def users_most_applications_query():
    print("Users with the most applications:\n")

    query = """
    SELECT user.name, COUNT(user.id) AS applied_jobs
    FROM application
    JOIN user
        ON user.id = application.user_id
    GROUP BY user.id
    ORDER BY COUNT(user.id) DESC
    """

    return query

# Average expected salary
def avg_expected_salary_query():
    print("Average expected salary:\n")

    query = """
    SELECT user.name, COUNT(user.id) AS applied_jobs, AVG(job.salary) AS avg_expected_salary
    FROM application
    JOIN user
        ON user.id = application.user_id
    JOIN job
        ON job.id = application.job_id
    GROUP BY user.id
    """

    return query

# =====================================
# MATCHING
# =====================================

# Jobs matching Ian's skills
def jobs_matching_user_skill_query(username):
    print(f"Jobs matching {username}'s skills:\n")

    query = f"""
    SELECT job.title, COUNT(userskill.skill_id) AS skills_matched
    FROM userskill
    JOIN user
        ON user.id = userskill.user_id
    JOIN jobskill
        ON userskill.skill_id = jobskill.skill_id
    JOIN job
        ON jobskill.job_id = job.id
    JOIN skill
        ON userskill.skill_id = skill.id
    WHERE user.name = '{username}'
    GROUP BY job.title
    ORDER BY COUNT(userskill.skill_id) DESC
    """

    return query

# Users matching Backend Intern
def users_matching_job_skill_query(jobname):
    print(f"Users matching {jobname}'s skills:\n")

    query = f"""
    SELECT user.name, COUNT(userskill.skill_id) AS skills_matched
    FROM userskill
    JOIN user
        ON user.id = userskill.user_id
    JOIN jobskill
        ON userskill.skill_id = jobskill.skill_id
    JOIN job
        ON jobskill.job_id = job.id
    JOIN skill
        ON userskill.skill_id = skill.id
    WHERE job.title = '{jobname}'
    GROUP BY user.name
    ORDER BY COUNT(userskill.skill_id) DESC
    """

    return query
