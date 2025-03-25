import csv
import sqlite3
import pandas as pd


df=pd.read_csv('k:/git_repo/MainRepo/Projects/Lego project/sets.csv')

df.columns = df.columns.str.strip()
conn = sqlite3.connect('k:/git_repo/MainRepo/Projects/Lego project/legoDB.db')
df.to_sql('sets', conn, if_exists='replace')
conn.close()