from api.api_client import APIClient
import pandas as pd

def main():
    api_dict = {}

    df = pd.read_csv('config/api_info.csv')

    for row in df.itertuples(index=False):
        api_dict[row.website] = APIClient(row.url, row.api_key, row.header)

    print(api_dict)

    

    




if __name__ == "__main__":
    main()