from clean import clean_data as cd
from db.database import initialize_database, fill_jobs
import db.seed as seed

def main():

    initialize_database()

    seed.seed_database()

    fill_jobs(cd.load_clean_data())


if __name__ == "__main__":
    main()
