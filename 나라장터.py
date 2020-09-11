import pandas as pd

url = "http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?" 
query = "area=&bidNm=&bidSearchType=1&fromBidDt=2020%2F08%2F11&fromOpenBidDt=&instNm=&"
query = query + "radOrgan=1&regYn=Y&searchDtType=1&searchType=1&taskClCds=&"
query = query + "toBidDt=2020%2F09%2F10&toOpenBidDt=&currentPageNo=2&maxPageViewNoByWshan=2&"

#f-string 문법
변수 = "2020-09-10"
페이지번호 = 3
q = f"Date={변수}&currentPageNo={페이지번호}"
q

table = pd.read_html(url)
len(table)

table[0]
table[0].to_csv("나라장터.csv", encoding="cp949", index=False)
pd.read_csv("나라장터.csv", encoding="cp949")
