# Setting up back-end

## 1. The database

In your terminal, change directory from root to /back-end and run:

`psql -U <username> -d salescout -a -f ./db/salescout.sql`

## 2. Python

In your terminal, change directory from root to /back-end and run:
`pip install -r requirements.txt`

(Once all necessary packages are added, run `pip freeze > ./requirements.txt`).
