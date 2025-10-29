from datetime import datetime, UTC
import pandas as pd

def main():
    now = datetime.now(UTC)  # timezone-aware UTC datetime
    df = pd.DataFrame({"hello": ["world"], "time": [now]})
    print(df)

if __name__ == "__main__":
    main()
