import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.connection import get_session


def main():
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
