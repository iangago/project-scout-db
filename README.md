# ScoutDB

A job market data collection and analytics project designed to explore
**how real-world job listing data can be collected, normalized, stored,**
**and analyzed**.

This project was built as a practical exercise in working with external,
imperfect data.

Instead of focusing on building a complete job-search application, ScoutDB
focuses on the data pipeline behind one:

* collecting job listings from an external API
* cleaning and normalizing inconsistent data
* storing structured information in a relational database
* querying and transforming the data
* analyzing the resulting dataset with Pandas
* visualizing the results through a Streamlit dashboard

The project uses real job listings rather than a manually constructed
dataset, which introduced several limitations and data-quality problems
that had to be handled during development.

---

## Core Idea

ScoutDB is primarily a **data processing and exploratory analysis project**.

The original idea was to build a structured database that could support
job searching and matching. During development, however, the project
became more focused on the underlying data problem:

> How do you turn inconsistent external job listings into structured,
> queryable, and analyzable data?

The data source does not provide every field consistently. Salary,
employment type, seniority level, and work mode may be missing, while job
descriptions are truncated.

Rather than artificially filling these gaps, ScoutDB preserves the
available information and makes data completeness part of the analysis.

---

## Features

### API Data Collection

* Collect job listings from the Adzuna API
* Search using multiple job-related queries
* Request multiple pages of results
* Store raw API responses before processing
* Combine results from different searches

### Data Cleaning & Normalization

* Normalize raw API responses into a consistent structure
* Standardize fields before database insertion
* Convert timestamps into appropriate datetime representations
* Normalize categorical information
* Handle missing values
* Separate reliable API-provided information from inferred information

### Duplicate Handling

The API can return the same or very similar job listings across different
search queries.

ScoutDB therefore handles duplicate records using the identifiers
provided by the source rather than treating every API response as a
unique job.

### Relational Database

The cleaned job data is stored in SQLite using related tables for entities
such as:

* jobs
* companies
* employment types
* seniority levels

This allows job information to be queried without unnecessarily
duplicating categorical data.

### SQL Analysis

The project includes SQL queries for answering questions about the
collected dataset, such as:

* Which jobs match a particular search?
* Which companies are hiring?
* How are listings distributed across different categories?
* What employment information is available?
* How complete is the collected data?

### Pandas Analysis

Pandas is used after the database layer to transform the SQL results into
DataFrames for exploratory analysis.

Examples include:

* counting job titles
* grouping listings
* analyzing missing values
* calculating salary statistics
* preparing data for visualization

### Analytics Dashboard

A Streamlit dashboard provides a visual overview of the collected
dataset.

The dashboard includes:

* total number of listings
* number of companies
* employment-type distribution
* most common job titles
* salary statistics
* company distribution
* data completeness
* access to the analyzed dataset

The dashboard is intended as an analytical interface rather than a
complete job-search frontend.

---

## Data Pipeline

The overall pipeline can be summarized as:

```text
                Adzuna API
                    │
                    ▼
             Raw API Responses
                    │
                    ▼
             Data Cleaning
                    │
                    ▼
            Normalized Job Data
                    │
                    ▼
                 SQLite
                    │
             ┌──────┴──────┐
             ▼             ▼
        SQL Queries     Pandas
             │             │
             └──────┬──────┘
                    ▼
             Streamlit Dashboard
```

This separation makes it possible to collect and process data without
coupling the database to the presentation layer.

---

## Data Model

The database is structured around jobs and their related entities.

### `jobs`

Stores information directly associated with a job listing:

* `id`
* `external_id`
* `title`
* `url`
* `description`
* `salary`
* `location`
* `company_id`
* `level_id`
* `employment_type_id`
* `work_mode`
* `created_at`

### `companies`

Stores companies associated with job listings.

* `id`
* `name`

### `levels`

Stores available seniority levels.

* `id`
* `name`

### `employment_types`

Stores employment categories.

* `id`
* `name`

The relationships allow multiple job listings to reference the same
company, level, or employment type.

---

## Working With Imperfect Data

One of the main lessons from this project was that external APIs rarely
provide a perfectly structured dataset.

For example, some fields returned by the API were frequently missing:

| Field           | Availability                 |
| --------------- | ---------------------------- |
| Salary          | Frequently unavailable       |
| Employment type | Partially available          |
| Seniority level | Unavailable in many listings |
| Work mode       | Unavailable in many listings |
| Company         | Mostly available             |
| Location        | Available                    |
| Title           | Available                    |
| Description     | Available but truncated      |

Rather than inventing values for missing fields, ScoutDB preserves the
missing information.

This also allows the dashboard to measure data completeness, making
the limitations of the source visible.

---

## Dashboard

The final dashboard focuses on exploratory analysis of the collected job
market data.

Example analyses include:

### Job Titles

Shows the most frequently occurring job titles in the dataset.

This reveals the variety of titles used by companies for similar roles,
such as:

* Data Analyst
* Data Analyst II
* Senior Data Analyst
* Software Engineer
* Senior Software Engineer
* Staff Software Engineer

### Employment Type

Shows the distribution of the employment types actually provided by the
API.

### Salary

Salary analysis is performed only on listings where salary information is
available.

The dashboard displays statistics such as:

* number of listings with salary information
* minimum salary
* maximum salary
* median salary

### Companies

Shows companies with the highest number of listings in the collected
dataset.

### Data Completeness

Shows what percentage of listings contain information for each field.

This is particularly useful for understanding the limitations of the
external data source.

---

## Tech Stack

| Category                  | Technology   |
| ------------------------- | ------------ |
| Language                  | Python       |
| Database                  | SQLite       |
| Data Analysis             | Pandas       |
| Numerical Computing       | NumPy        |
| Visualization / Dashboard | Streamlit    |
| Data Source               | Adzuna API   |
| Version Control           | Git / GitHub |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/iangago/project-scout-db.git
```

Navigate into the project:

```bash
cd project-scout-db
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

The project requires access to the Adzuna API.

API credentials should be stored as environment variables rather than
committed to the repository.

Example:

```env
ADZUNA_APP_ID=your_app_id
ADZUNA_APP_KEY=your_app_key
```

The current location of the search market is set in Brasil as a whole. 

If you would like to provide a specific city or location inside Brasil change the functions bellow in the main.py:

```main
aa.search_all_terms("PREFERED_LOCATION_INSIDE_BRASIL")
ds.run_dashboard("PREFERED_LOCATION_INSIDE_BRASIL")
```

---

## Running the Program

Run the main program:

```bash
python -m streamlit run main.py
```

This handles the data collection and processing pipeline and the analytics dashboard that is built with Streamlit.

Streamlit will provide a local URL where the dashboard can be viewed.

---

## Project Status

**Version 1.0 — Complete**

The project has reached the point where the main learning objectives have
been achieved.

The final implementation covers:

* external API integration
* raw data collection
* data cleaning
* normalization
* relational database design
* SQLite
* SQL querying
* Pandas-based analysis
* exploratory data analysis
* data visualization
* Streamlit dashboard development

Further development is intentionally limited to avoid turning the project
into a full job-search platform.

---

## What I Learned

ScoutDB was primarily a learning project, and its value came from working
with the entire data lifecycle rather than from the final dashboard.

Through the project, I developed practical experience with:

### Working With APIs

* understanding API parameters
* pagination
* collecting results from multiple searches
* dealing with incomplete API responses
* preserving raw external data

### Data Engineering

* cleaning inconsistent external data
* normalization
* missing-value handling
* duplicate handling
* designing a relational schema
* separating raw data from processed data

### SQL

* relational modeling
* primary and foreign keys
* joins
* filtering
* aggregation
* grouping
* analytical queries

### Python Data Analysis

* Pandas DataFrames
* transforming SQL results into DataFrames
* grouping and aggregation
* missing-value analysis
* preparing data for visualization

### Data Visualization

* building analytical charts
* presenting distributions
* communicating data completeness
* creating an interactive Streamlit dashboard

Most importantly, the project demonstrated that working with real-world
data is significantly different from working with clean tutorial datasets.

---

## Limitations

The dataset is dependent on the information returned by the Adzuna API.

Some limitations include:

* salary information is frequently unavailable
* employment type is inconsistently provided
* seniority information is limited
* work mode is frequently unavailable
* job descriptions are truncated
* different searches can return overlapping listings
* job titles are not standardized

Because of these limitations, the project avoids making strong claims
where the underlying data is insufficient.

For example, the project does not attempt to infer the complete set of
skills required by companies from truncated descriptions.

---

## Development Notes

The Streamlit dashboard was developed with assistance from OpenAI's
ChatGPT.

The project architecture, database design, API integration, data
collection process, normalization strategy, SQL queries, and analytical
decisions were developed by me alone as part of the project development process.

AI assistance was used primarily as a development aid, while the resulting
code was done alone and concepts were reviewed and understood during implementation.

---

## Why I Stopped Developing It

The purpose of ScoutDB was to gain practical experience with data
collection, processing, databases, and analysis.

Once the project had successfully demonstrated the complete pipeline from
**external API → normalized data → relational database → analysis →
visualization**, additional features would have provided diminishing
learning value.

Rather than expanding the project into a larger application, development
was stopped after the core data workflow was completed.

The project can therefore serve as a foundation for future projects
involving machine learning and more advanced data analysis.

---

## Author

**Ian Gago Mendes**
