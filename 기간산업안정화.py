import requests

"""
keyword = "%EA%B8%B0%EA%B0%84%EC%82%B0%EC%97%85%EC%95%88%EC%A0%95"
startDate = "20100810"
endDate = "20200910"
viewPage = "1"
rowPage = "10000"

baseURL = "https://www.open.go.kr/othicInfo/infoList/infoList.ajax?"
query1 = f"kkwd={keyword}&insttSeCd=&eduYn=N&" 
query2 = f"startDate={startDate}&endDate={endDate}&" 
query3 = f"insttCdNm=&insttCd=&searchMainYn=&viewPage={viewPage}&rowPage={rowPage}&sort=s"

url = baseURL+query1+query2+query3

"""
baseURL = "https://www.open.go.kr/othicInfo/infoList/infoList.ajax?"
query = "kwd=%EA%B8%B0%EA%B0%84%EC%82%B0%EC%97%85%EC%95%88%EC%A0%95&insttSeCd=&eduYn=N&startDate=20090912&endDate=20200911&insttCdNm=&insttCd=&searchMainYn=&sort=s&viewPage=1&rowPage=10000&totalPage=20&url=%2FothicInfo%2FinfoList%2FinfoList.ajax&callBackFn=searchFn_callBack"

url = baseURL+query

response = requests.post(url)
response.text


import json

response_data = json.loads(response.text)
response_data

rtnList = response_data["result"]["rtnList"]
rtnList[:10]


import pandas as pd
df = pd.DataFrame(rtnList)
df["tma_kwd"] = df["tma_kwd"].str.replace("\n", "  ")
df[:10]
df.info()


df.to_csv("기간산업안정화.csv", encoding = "cp949", index=False)
pd.read_csv("기간산업안정화.csv", encoding="cp949")
