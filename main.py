from db import database as db
from db import seed
from clean import clean_data as cd
from raw import raw_data as rd
from api import adzuna_api as aa
from data_processing import normalization as n
import dashboard as ds

def main():

    # Request and load api information
    aa.search_all_terms("")

    # Normalize and load raw data
    n.normalize_all_jobs(rd.load_raw_data())

    # Initialize database
    db.initialize_database()

    # Seed database
    seed.seed_database()

    # Insert all jobs in the database
    db.fill_jobs(cd.load_clean_data())

    # Run the dashboard for the user
    ds.run_dashboard("")

if __name__ == "__main__":
    main()
