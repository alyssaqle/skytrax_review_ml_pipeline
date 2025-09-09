# handles Snowflake connection/session
import os
from snowflake.snowpark import Session
from dotenv import load_dotenv

load_dotenv()  # reads .env

def get_session():
    params = {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "role": os.getenv("SNOWFLAKE_ROLE", "ANALYST"),
        "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
        "database": os.getenv("SNOWFLAKE_DATABASE", "SKYTRAX_REVIEWS_DB"),
        "schema": os.getenv("SNOWFLAKE_SCHEMA", "MARTS"),
    }
    return Session.builder.configs(params).create()


 