# url 입력
url = input("사이트의 url을 입력하세요.")
# 규칙1) http:// 부분 제외
line = url.replace("http://",'')
# 규칙2) .이후 부분 제외
place = line.find(".")
line = line[:place]
# 규칙3) 비밀번호 생성
pw = line[:3]+str(len(line))+str(line.count("e"))+"!"
print("{}의 비밀번호는 {}입니다.".format(url,pw))