from datetime import datetime
import pandas as pd

def main():
    df = pd.DataFrame({"hello": ["world"], "time": [datetime.utcnow()]})
    print(df)

if __name__ == "__main__":
    main()
