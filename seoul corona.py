import pandas as pd

url = "https://www.seoul.go.kr/coronaV/coronaStatus.do"

table = pd.read_html(url)
# table

len(table)
table[0]
table[1]
table[2]
table[3]

table[3].to_csv("서울코로나.csv", encoding="cp94", index=False)
pd.read_csv("서울코로나.csv", encoding="cp94")
