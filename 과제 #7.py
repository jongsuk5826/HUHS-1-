import os
os.chdir('Python')
os.chdir('과제 #7')
for i in range(1,51) :
    with open(str(i)+'주차.txt','w',encoding='utf8') as f :
        f.write("- {0} 주차 주간보고 -".format(i))
        f.write("\n부서 :\n이름 :\n업무 요약 :")