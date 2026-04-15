'''
Boolean Indexing : 
불린 인덱싱은 조건 필터링과 추출을 동시에 할 수 있기 때문에
매우 자주 사용되는 인덱싱이다. (개인적 사고)

[구성]  배열[조건식] 
'''

import numpy as np
# 예) 
# 배열 내의 값이 5보다 작은 값들을 배열에서 추출하고자 한다면, 
# 1) boolean 인덱싱 사용하지 않는 경우:
print('--------------- not boolean indexing ------------------') 
# 1에서 9까지의 값을 가지는 1차원을 준비하기
ar1 = np.arange(1,10) # [1,2,3,4,5,6,7,8,9]
res = []   # 리스트지, 배열이 아님
for i in ar1:
    if i < 5:
        res.append(i) # 수가 5보다 작으므로 res에 추가(누적) 
print('type(res):', type(res))  
ar2 = np.array(res) # list를 ndarray로 변환  
print('type(ar2):', type(ar2)) 
print(ar2) 
print('------------------boolean indexing ------------------------') 
ar3 = ar1[ar1<5]  
print('type(ar3):',type(ar3))
print(ar3)
print('------------------ ar1.reshape(3,3) ------------------------') 
re_ar = ar1.reshape(3,3) 
print(re_ar<5) # 행렬로 나옴
# ar4 = re_ar[re_ar<5]
print(re_ar[re_ar<5]) # 조건 달면, 결과만 보겠다는 것
print('----------------- 새로운 리스트 생성 -------------------')
list1 = [8,1,5,3,2,7,9,6,4]  
print(type(list1)) 
ar5 = np.array(list1) # list를 ndarray로 변환
re_ar5 = ar5.reshape(3,3)  # 1차원 --> 2차원. 모양을 바꾸고 싶으면 array로 바꾼 후 reshape가능
print('re_ar5: ', re_ar5 < 5)  



