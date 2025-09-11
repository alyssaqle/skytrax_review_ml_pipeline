"""Test script for establishing a Snowflake session and running a sample query.

This script connects to Snowflake using the get_session utility and runs a test query to verify the connection.
"""

from src.connection import get_session


def main():
    """Establish a Snowflake session and run a sample query.

    Connects to Snowflake using get_session and prints the result of a test query.
    If the sample table does not exist, prints an error message.
    """
    s = get_session()
    print(s.sql("select current_user(), current_role(), current_warehouse()").collect())
    # sanity query (adjust table name if needed)
    try:
        rows = (
            s.table("MARTS.FCT_REVIEW_ENRICHED").select("SEAT_COMFORT", "FOOD_AND_BEVERAGES", "RECOMMENDED").limit(5).collect()
        )
        print(rows)
    except Exception as e:
        print("Connected, but sample table not found:", e)


if __name__ == "__main__":
    main()
