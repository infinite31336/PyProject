import re

id=input('請輸入身分證字號:')
id=id.upper()   #轉成大寫
aabb={'A':'10','B':'11','C':'12','D':'13','E':'14','F':'15','G':'16',
'H':'17','I':'34','J':'18','K':'19','L':'20','M':'21','N':'22','O':'35',
'P':'23','Q':'24','R':'25','S':'26','T':'27','U':'28','V':'29','W':'32',
'X':'30','Y':'31','Z':'33'}   #英文字母數值對應表
N=len(id)
correct_id=(N==10)
if correct_id:
    first=aabb.get(id[0])#取得英文字母
    a=int(first[0])#十位數
    b=int(first[1])#個位數
    i=1#設定起始值
    count=0
    for n in range(8,0,-1):#身分證後九位數從後面開始數
        count=int(id[i])*n+count#加權值
        i+=1
    count=a+b*9+int(id[i])+count#總和
    if count%10==0:
        print("身分證正確")
    else:
        print("身分證錯誤")
else:
    print("身分證格式有誤")