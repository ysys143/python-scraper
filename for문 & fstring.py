변수 = "2020-09-10"
페이지번호 = 3
q = f"Date={변수}&currentPageNo={페이지번호}"

for 페이지번호 in range(1,10) :
    쿼리 = f"Date={변수}&currentPageNo={페이지번호}"
    print(쿼리)


