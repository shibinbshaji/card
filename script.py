import sys
card_no = list(sys.argv[1])
######################################################
def double_it(dig):
	if dig < 5:
		dig = dig*2
	else:
		if dig == 5:
			dig = 1
		elif dig == 6:
			dig = 3
		elif dig == 7:
			dig = 5
		elif dig == 9:
			dig = 9
	return dig
######################################################
def check_card(numb):
	num = numb.copy()
	num[0] = double_it(num[0])
	num[2] = double_it(num[2])
	num[4] = double_it(num[4])
	num[6] = double_it(num[6])
	num[8] = double_it(num[8])
	num[10] = double_it(num[10])
	num[12] = double_it(num[12])
	num[14] = double_it(num[14])
	sum = 0
	for i in num:
		sum = sum + i
	if sum%10 == 0:
		##print("Valid Card Number")
		return 1
#######################################################
for i in range(0,16):
        card_no[i] = int(card_no[i])
num = card_no.copy()
check_card(num)
#########################temp code#################3
temp = []
for i in range(0,12):
	temp.append(card_no[i])
temp2 = temp.copy()
print(temp2)
for i in range(0,10):
	for j in range(0,10):
		for k in range(0,10):
			for l in range(0,10):
				temp2 = temp.copy()
				temp2.append(i)
				temp2.append(j)
				temp2.append(k)
				temp2.append(l)
				if (check_card(temp2)):
					print(temp2)
