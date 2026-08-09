--COMPANY
-- Name and id of company
CREATE TABLE IF NOT EXISTS company (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

--Levels
CREATE TABLE IF NOT EXISTS level (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

--Employment types
CREATE TABLE IF NOT EXISTS employment_type (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

--SKILL
CREATE TABLE IF NOT EXISTS skill (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

--USER
--He could not have a preferred work mode i guess, so NULL
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    preferred_location TEXT,
    minimum_salary INTEGER,

    preferred_level_id INTEGER,
    preferred_employment_type_id INTEGER,

    preferred_work_mode INTEGER CHECK (preferred_work_mode IN (0, 1, 2)),
    
    FOREIGN KEY(preferred_level_id) REFERENCES level(id),
    FOREIGN KEY(preferred_employment_type_id) REFERENCES employment_type(id)
);

--JOB
-- I will do the application in python using enums
-- workmode ( 0 = On-Site
--            1 = Hybrid
--            2 = Remote )
-- maybe level and emnployment types wich are something that can change,
-- i create a separate table for both wich i can add or not
CREATE TABLE IF NOT EXISTS job (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    salary INTEGER,
    location TEXT,

    company_id INTEGER,
    level_id INTEGER,
    employment_type_id INTEGER,

    work_mode INTEGER CHECK (work_mode IN (0, 1, 2)),

    created_at DATETIME,

    FOREIGN KEY(level_id) REFERENCES level(id),
    FOREIGN KEY(employment_type_id) REFERENCES employment_type(id),
    FOREIGN KEY(company_id) REFERENCES company(id)
);

--JOBSKILL
CREATE TABLE IF NOT EXISTS jobskill (
    job_id INTEGER,
    skill_id INTEGER,

    PRIMARY KEY(job_id, skill_id),

    FOREIGN KEY(job_id) REFERENCES job(id),
    FOREIGN KEY(skill_id) REFERENCES skill(id)
);

--USERSKILL
CREATE TABLE IF NOT EXISTS userskill (
    user_id INTEGER,
    skill_id INTEGER,

    PRIMARY KEY(user_id, skill_id),

    FOREIGN KEY(user_id) REFERENCES user(id),
    FOREIGN KEY(skill_id) REFERENCES skill(id)
);

--APPLICATION
-- status ( 0 = Saved
--          1 = Applied
--          2 = Accepted
--          3 = Rejected )
CREATE TABLE IF NOT EXISTS application (
    id INTEGER PRIMARY KEY,

    user_id INTEGER,
    job_id INTEGER,

    status INTEGER CHECK (status IN (0, 1, 2, 3)),

    applied_at DATETIME,

    UNIQUE(user_id, job_id),

    FOREIGN KEY(user_id) REFERENCES user(id),
    FOREIGN KEY(job_id) REFERENCES job(id)
);