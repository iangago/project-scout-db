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

--Users
INSERT INTO user
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
