import pandas as pd 

def get_phone_numbers(PATH):
    df = pd.read_csv(PATH)
    customers = df["Phone"].to_list()
    return customers