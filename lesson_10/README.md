# <span style="color:violet"> SQLite3, PostgreSQL</span>


## <span style="color:purple">Materials</span>

- [Python & databases](https://proglib.io/p/kak-podruzhit-python-i-bazy-dannyh-sql-podrobnoe-rukovodstvo-2020-02-27)


```python
# PostgreSQL:

# # Create the file repository configuration:
# sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt -->
# --> $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# # Import the repository signing key:
# wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# # Update the package lists:
# sudo apt-get update

# # Install the latest version of PostgreSQL.
# # If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
# sudo apt-get -y install postgresql

# sudo -u postgres psql


# CREATE USER admin WITH PASSWORD '12345678';
# ALTER ROLE admin SET client_encoding TO 'utf8';
# ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
# ALTER ROLE admin SET timezone TO 'UTC';

# CREATE DATABASE quiz;
# GRANT ALL PRIVILEGES ON DATABASE quiz TO admin;

# ALTER USER admin CREATEDB;


# sudo service postgresql restart
# sudo service postgresql stop
```