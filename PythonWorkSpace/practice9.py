score_file=open("score.txt","r",encoding="utf-8")
lines=score_file.readlines() #list형태로 저장
for line in lines:
    print(line,end="")
    
score_file.close()
score_file.close()