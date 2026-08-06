--Levels
INSERT INTO level (name) VALUES
('Intern'),
('Junior'),
('Mid'),
('Senior');

--Employment Types
INSERT INTO employment_type (name) VALUES
('Full-time'),
('Part-time'),
('Internship'),
('Contract');

--Skills
INSERT INTO skill (name) VALUES
('Python'),
('SQL'),
('PostgreSQL'),
('SQLite'),
('Git'),
('Docker'),
('Linux'),
('Pandas'),
('NumPy'),
('Power BI'),
('FastAPI'),
('Flask'),
('TensorFlow'),
('AWS'),
('JavaScript'),
('React'),
('Machine Learning'),
('Excel'),
('C#'),
('Java');

--Companies
INSERT INTO company (name) VALUES
('Nubank'),
('Mercado Livre'),
('iFood'),
('Stone'),
('Google'),
('Microsoft'),
('OpenAI'),
('CloudWalk'),
('PicPay'),
('XP Inc.');

--Users
INSERT INTO users
(
    name,
    email,
    preferred_location,
    minimum_salary,
    preferred_level_id,
    preferred_employment_type_id,
    preferred_work_mode
)
VALUES
('Ian', 'ian@email.com', 'Rio de Janeiro', 2500, 1, 3, 1),
('Maria', 'maria@email.com', 'São Paulo', 6000, 2, 1, 2),
('Lucas', 'lucas@email.com', 'Remote', 9000, 3, 1, 2),
('Julia', 'julia@email.com', 'Curitiba', 5000, 2, 1, 0),
('Pedro', 'pedro@email.com', 'Remote', 12000, 4, 1, 2),
('Ana', 'ana@email.com', 'São Paulo', 7000, 2, 1, 1);

--Jobs
INSERT INTO job
(
    title,
    description,
    salary,
    location,
    company_id,
    level_id,
    employment_type_id,
    work_mode,
    created_at
)
VALUES
(
'Backend Intern',
'Assist the backend team developing internal APIs using Python.',
2800,
'São Paulo',
1,
1,
3,
1,
CURRENT_TIMESTAMP
),

(
'Data Analyst',
'Analyze business metrics and create dashboards.',
6500,
'São Paulo',
3,
2,
1,
2,
CURRENT_TIMESTAMP
),

(
'Machine Learning Engineer',
'Develop and deploy machine learning models.',
25000,
'Remote',
7,
4,
1,
2,
CURRENT_TIMESTAMP
),

(
'Backend Developer',
'Develop scalable backend services.',
9500,
'São Paulo',
2,
3,
1,
1,
CURRENT_TIMESTAMP
),

(
'Python Developer',
'Develop automation and backend applications.',
8500,
'Belo Horizonte',
8,
2,
1,
2,
CURRENT_TIMESTAMP
),

(
'Business Intelligence Analyst',
'Create reports and dashboards for business teams.',
7000,
'São Paulo',
10,
2,
1,
1,
CURRENT_TIMESTAMP
),

(
'Data Engineer',
'Build and maintain ETL pipelines.',
18000,
'São Paulo',
5,
4,
1,
1,
CURRENT_TIMESTAMP
),

(
'Software Engineer',
'Develop enterprise software solutions.',
15000,
'Rio de Janeiro',
6,
3,
1,
2,
CURRENT_TIMESTAMP
),

(
'AI Research Intern',
'Support research on machine learning models.',
6000,
'Remote',
7,
1,
3,
2,
CURRENT_TIMESTAMP
),

(
'Backend Engineer',
'Build APIs and microservices.',
12000,
'Rio de Janeiro',
4,
3,
1,
1,
CURRENT_TIMESTAMP
);


--User skills
INSERT INTO userskill (user_id, skill_id) VALUES
-- Ian
(1,1),
(1,2),
(1,4),
(1,5),

-- Maria
(2,2),
(2,10),
(2,18),

-- Lucas
(3,1),
(3,6),
(3,7),
(3,11),
(3,14),

-- Julia
(4,15),
(4,16),
(4,5),

-- Pedro
(5,1),
(5,8),
(5,9),
(5,13),
(5,17),

-- Ana
(6,1),
(6,2),
(6,8),
(6,10),
(6,18);

--Job Skills
INSERT INTO jobskill (job_id, skill_id) VALUES
-- Backend Intern
(1,1),
(1,2),
(1,5),
(1,11),

-- Data Analyst
(2,1),
(2,2),
(2,8),
(2,10),
(2,18),

-- Machine Learning Engineer
(3,1),
(3,5),
(3,6),
(3,8),
(3,9),
(3,13),
(3,14),
(3,17),

-- Backend Developer
(4,1),
(4,3),
(4,5),
(4,6),
(4,7),
(4,11),

-- Python Developer
(5,1),
(5,2),
(5,4),
(5,5),
(5,12),

-- Business Intelligence Analyst
(6,1),
(6,2),
(6,8),
(6,10),
(6,18),

-- Data Engineer
(7,1),
(7,2),
(7,3),
(7,5),
(7,6),
(7,7),
(7,14),

-- Software Engineer
(8,2),
(8,5),
(8,6),
(8,15),
(8,19),

-- AI Research Intern
(9,1),
(9,8),
(9,9),
(9,13),
(9,17),

-- Backend Engineer
(10,1),
(10,3),
(10,5),
(10,6),
(10,7),
(10,11);

--Application
INSERT INTO application
(user_id, job_id, status, applied_at)
VALUES

(1,1,1,CURRENT_TIMESTAMP),
(1,9,0,CURRENT_TIMESTAMP),

(2,2,2,CURRENT_TIMESTAMP),

(3,4,1,CURRENT_TIMESTAMP),
(3,7,0,CURRENT_TIMESTAMP),

(4,8,3,CURRENT_TIMESTAMP),

(5,3,1,CURRENT_TIMESTAMP),
(5,9,1,CURRENT_TIMESTAMP),

(6,6,2,CURRENT_TIMESTAMP),
(6,2,1,CURRENT_TIMESTAMP);