import requests

baseURL = "https://www.open.go.kr/othicInfo/infoList/infoList.ajax"
query = "kwd=%EC%84%A0%EB%B6%88%EC%8B%9D%ED%95%A0%EB%B6%80%EA%B1%B0%EB%9E%98&insttSeCd=&eduYn=N&startDate=20100812&endDate=20200910&insttCdNm=&insttCd=&searchMainYn=&viewPage=1&rowPage=1000&sort=s"
url = f"{baseURL}?{query}"


response = requests.post(url)
response.text[:10]



import json

response_data = json.loads(response.text)
response_data[:10]

rtnList = response_data["result"]["rtnList"]
rtnList[:10]


import pandas as pd
df = pd.DataFrame(rtnList)
df["tma_kwd"] = df["tma_kwd"].str.replace("\n", "  ")
df[:10]
df.info()


df.to_csv("선불식할부거래.csv", encoding = "cp949", index=False)
pd.read_csv("선불식할부거래.csv", encoding="cp949")
