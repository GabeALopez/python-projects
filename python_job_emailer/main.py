from api.api_client import APIClient
import pandas as pd

def process_data(key, value_data):
    match key:
            case 'devitjobs':
                print("")
            case _:
                print("Nothing")

def main():
    api_dict = {}

    df = pd.read_csv('config/api_info.csv')

    for row in df.itertuples(index=False):
        api_dict[row.website] = APIClient(row.url, row.api_key, row.header)

    for key, value in api_dict.items():
        value_data = value.get_data()
        process_data(key, value_data)

        

        

    print("")

if __name__ == "__main__":
    main()