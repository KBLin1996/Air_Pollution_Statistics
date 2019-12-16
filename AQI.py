import os
import pandas as pd


def process(data, country_path):

    value = 0
    avg = 0

    for csv in data:
        csv_path = os.path.join(country_path, csv)
        df = pd.read_csv(csv_path)
        
        for i in range(1, 13):
            value = df.iloc[1][i] + value

    #print(len(data))
    avg = value / (len(data) * 12)

    return avg

def display_AQI(country, avg):
    
    if avg >= 0 and avg < 15.5:
        print("Country: ", country, "    Result:  Green")

    elif avg >= 15.5 and avg < 35.5:
        print("Country: ", country, "    Result:  Yellow")

    elif avg >= 35.5 and avg < 54.5:
        print("Country: ", country, "    Result:  Orange")
    
    elif avg >= 54.5 and avg < 150.5:
        print("Country: ", country, "    Result:  Red")
    
    elif avg >= 150.5 and avg < 250.4:
        print("Country: ", country, "    Result:  Purple")


if __name__ == '__main__':

    main_directory = "./All_AirPollution"

    years = os.listdir(main_directory)

    for year in years:

        year_path = os.path.join(main_directory, year)
        print(year, ":")
        countries = os.listdir(year_path)

        for country in countries:

            country_path = os.path.join(year_path, country)
            all_csv = os.listdir(country_path)
            average = process(all_csv, country_path)
            #print("Country: ", country, ", Average", average)

            display_AQI(country, average)