import random

answer = random.randint(1, 100)
counter = 0
while True:
	counter += 1
	number = int(input('請輸入: '))
	if number < answer:
		print('比%d大一點' % number)
	elif number > answer:
		print('比%d小一點' % number)
	else:
		print('恭喜你猜對了!')
		break
print('總共猜了%d次' % counter)
if counter > 7:
    print('再接再厲')
elif counter >3:
    print('做得不錯')
else:
    print('太棒了')