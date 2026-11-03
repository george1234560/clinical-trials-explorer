import pandas as pd

def fix_date(date):
    if not pd.isna(date):

        if len(date) == 7:
            date =date + "-15"

    return date

def fix_data(df):
    df["enrollment"] = df["enrollment"].astype("Int64")
    df["startdate"] = df["startdate"].apply(fix_date)
    df["completion_date"] = df["completion_date"].apply(fix_date)
    df["startdate"] =pd.to_datetime(df["startdate"])
    df["completion_date"] =pd.to_datetime(df["completion_date"])

    return df