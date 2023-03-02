import pickle
# profile_file=open("profile.picke","wb")
# profile={"이름":"차현수","나이":24,"취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file) #profile에 있는 정보를 file에 저장하는 것
# profile_file.close()

profile_file=open("profile.picke","rb")
profile=pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()