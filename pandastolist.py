import pandas as pd
df = pd.read_csv("C:/Users/user/Desktop/abhi/nse.csv")
isin_list = df["ISIN"].tolist()
print(isin_list)