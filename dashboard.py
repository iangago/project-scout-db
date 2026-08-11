import sqlite3
import pandas as pd
import streamlit as st


# -------------------------
# Database
# -------------------------


def run_dashboard(where):
    conn = sqlite3.connect("db/scout.db")

    query = """
    SELECT
        j.id,
        j.external_id,
        j.title,
        j.url,
        j.description,
        j.salary,
        j.location,
        c.name AS company,
        l.name AS level,
        e.name AS employment_type,
        j.work_mode,
        j.created_at
    FROM job AS j

    LEFT JOIN company AS c
        ON j.company_id = c.id

    LEFT JOIN level AS l
        ON j.level_id = l.id

    LEFT JOIN employment_type AS e
        ON j.employment_type_id = e.id
    """

    df = pd.read_sql_query(query, conn)

    conn.close()


    # -------------------------
    # Page
    # -------------------------

    st.set_page_config(
        page_title="ScoutDB",
        page_icon="📊",
        layout="wide"
    )

    st.title("ScoutDB")
    st.subheader(f"{where} Technology Job Market")

    st.write(
        "Exploratory analysis of job listings collected from the Adzuna API."
    )


    # -------------------------
    # Basic statistics
    # -------------------------

    total_jobs = len(df)

    companies = df["company"].dropna().nunique()

    salary_count = df["salary"].notna().sum()

    employment_count = df["employment_type"].notna().sum()


    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Jobs", total_jobs)
    col2.metric("Companies", companies)
    col3.metric(
        "Salary available",
        f"{salary_count} / {total_jobs}"
    )
    col4.metric(
        "Employment type",
        f"{employment_count} / {total_jobs}"
    )


    # -------------------------
    # Job titles
    # -------------------------

    st.divider()

    st.header("Job Titles")

    title_counts = (
        df["title"]
        .value_counts()
        .head(10)
    )

    st.bar_chart(title_counts)


    # -------------------------
    # Employment type
    # -------------------------

    st.header("Employment Type")

    employment_counts = (
        df["employment_type"]
        .fillna("Unknown")
        .value_counts()
    )

    st.bar_chart(employment_counts)


    # -------------------------
    # Salary
    # -------------------------

    st.header("Salary")

    salary_df = df.dropna(subset=["salary"])

    if len(salary_df) == 0:

        st.info("No salary information is available.")

    else:

        salary_values = salary_df["salary"] / 100

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Available",
            f"{len(salary_values)} / {total_jobs}"
        )

        col2.metric(
            "Median",
            f"{salary_values.median():,.2f}"
        )

        col3.metric(
            "Range",
            f"{salary_values.min():,.2f} – "
            f"{salary_values.max():,.2f}"
        )

        st.write("Available salary values")

        st.bar_chart(salary_values)


    # -------------------------
    # Companies
    # -------------------------

    st.divider()

    st.header("Companies")

    company_counts = (
        df["company"]
        .fillna("Unknown")
        .value_counts()
        .head(10)
    )

    st.bar_chart(company_counts)


    # -------------------------
    # Data completeness
    # -------------------------

    st.divider()

    st.header("Data Completeness")

    columns_to_check = {
        "Title": "title",
        "Description": "description",
        "Location": "location",
        "Created date": "created_at",
        "Company": "company",
        "Employment type": "employment_type",
        "Level": "level",
        "Salary": "salary",
        "Work mode": "work_mode"
    }

    completeness = {}

    for display_name, column in columns_to_check.items():

        completeness[display_name] = (
            df[column].notna().mean() * 100
        )

    completeness_df = pd.DataFrame(
        {
            "Field": completeness.keys(),
            "Completeness (%)": completeness.values()
        }
    )

    completeness_df = completeness_df.set_index("Field")

    st.bar_chart(completeness_df)


    # -------------------------
    # Raw data
    # -------------------------

    st.divider()

    st.header("Dataset")

    st.write(
        "Raw normalized records used for the analysis."
    )

    st.dataframe(
        df,
        use_container_width=True
    )


    # -------------------------
    # Limitations
    # -------------------------

    st.divider()

    st.header("Data Limitations")

    st.write(
        """
        The dataset was collected from the Adzuna API and contains
        incomplete information for several fields. Salary, employment
        type, level and work mode are frequently unavailable.

        Job descriptions are truncated by the source API, so they were
        not used for deeper text analysis.
        """
    )