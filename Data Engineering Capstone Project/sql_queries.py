create_demographics = """
CREATE TABLE IF NOT EXISTS public.demographics (
    city                   VARCHAR,
    state                  VARCHAR,
    media_age              FLOAT,
    male_population        INT,
    female_population      INT,
    total_population       INT,
    num_veterans           INT,
    foreign_born           INT,
    average_household_size FLOAT,
    state_code             VARCHAR(2),
    race                   VARCHAR,
    count                  INT
);
"""

drop_demographics = "DROP TABLE IF EXISTS demographics;"

demographic_insert = """
INSERT INTO demographics (city, state, media_age, male_population, female_population, total_population, \
num_veterans, foreign_born, average_household_size, state_code, race, count) VALUES (%s, %s, %s, %s, \
%s, %s, %s, %s, %s, %s, %s, %s)"""

create_temperature = """
CREATE TABLE IF NOT EXISTS temperature (
    timestamp                      DATE,
    average_temperature            FLOAT,
    average_temperature_uncertainty FLOAT,
    city                           VARCHAR,
    country                        VARCHAR,
    latitude                       VARCHAR,
    longitude                      VARCHAR
);
"""

temperature_insert = ("""
INSERT INTO temperature (timestamp, average_temperature, average_temperature_uncertainty, city, country, \
latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s)""")

drop_temperature = "DROP TABLE IF EXISTS weather;"

drop_table_queries = [drop_demographics, drop_temperature]
create_table_queries = [create_demographics, create_temperature]