#내가 한 방법
# def std_weight(height,gender):
#     height=float(height/100)
#     if gender=="남자":
#         weight=round((height * height * 22),2)
#         print("키{0}m 남자의 표준 체중은 {1}입니다".format(height,weight))
#     elif gender=="여자":
#         weight=float(round((height * height * 21),2))
#         print("키{0}m 여자의 표준 체중은 {1}입니다".format(height,weight))

# std_weight(175,"남자")
# std_weight(160,"여자")
#################################################################################
#return 사용해서
def std_weight(height,gender):
    height=height/100
    if gender=="남자":
        weight=height*height*22
        return weight
    elif gender=="여자":
        weight=height*height*21
        return weight
    
height=175
gender=("남자")
weight=round(std_weight(height,gender),2)
#std_weight(175,"남자")
print("키{0}m {1}의 표준 체중은 {2}kg입니다".format(height,gender,weight))
