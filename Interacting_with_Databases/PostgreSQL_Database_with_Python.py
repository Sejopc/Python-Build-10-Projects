# Psycopg2 needs to be installed.

# Download the PostgreSQL (pgAdmin) to your specific OS from here and follow the instructions: https://www.postgresql.org/download

# Then download psycopg2:

# pip install psycopg2-binary

# Now, dowload PostreSQL Server so we can connect using pgAdmin:
# brew update
# brew install postgresql

# Create Postgres SQL Directory where servers will be stored and assign proper permissions:
# sudo mkdir /usr/local/var/postgres
# sudo chmod 775 /usr/local/var/postgres
# sudo chown construct /usr/local/var/postgres

# Initialize the PostgreSQL directory:
# initdb /usr/local/var/postgres

# Make sure PostgreSQL is now running on the appropiate port (5432):
# lsof -nP -iTCP -sTCP:LISTEN | grep 5432

# CHECK THIS LINK FOR ALL INFO ON POSTGRESQL SERVICE:
# https://chartio.com/resources/tutorials/how-to-start-postgresql-server-on-mac-os-x/

# CREATE USER "postgres" (only if PostgreSQL was installed with Homebrew)
# /usr/local/opt/postgres/bin/createuser -s postgres

# Go to pgAdmin panel, add a server, and fill the details (Host: localhost, port: 5432, user: postgres, password: postgres123) and SAVE.

# Once connected, create a new database (let's call it database1), choose postgres user and connect.

# Now, on next script (PostgreSQL-Selecting_Inserting_Deleting_and_Updating_SQL_Records.py) we configure the PostgreSQL database by setting DB parameters to connect by means of psycopg2.