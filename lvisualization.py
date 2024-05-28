import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('homelessness.csv')
# print(df)
# print(df.head)
# family_members = df[(df["family_members"]) > 2500 & (df["state_pop"] > 1354000)]
df['not_homeless_people'] = df["state_pop"] - (df["individuals"] + df["family_members"])
highest_not_homeless = df["not_homeless_people"].max()
print(df[df["not_homeless_people"] == highest_not_homeless])
# print(highest_not_homeless.iloc[:,[1,3]])
# print(df[["region","state","state_pop","not_homeless_people"]])
# sett_index = family_members.set_index("Unnamed: 0")
# drop_index = sett_index.set_index(drop = True)
# subset = family_members[family_members["region"].isin(["Pacific","New England"])]
# print(subset[['state','region','family_members','state_pop']])