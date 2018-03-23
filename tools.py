def calculate_r0(x_label, y_label):
	I = 0
	for i,each in enumerate(x_label):
		if each>0:
			I = i
			break

	max_1 = max(y_label[0:I])
	max_2 = max(y_label[I:-1])

	half_max_1 = max_1/2
	half_max_2 = max_2/2

	for i,each in enumerate(y_label[0:I]):
		if each == max_1:
			max_1_x = x_label[i]

	for i,each in enumerate(y_label[I:-1]):
		if each == max_2:
			max_2_x = x_label[I+i]

	r0 = (max_2_x-max_1_x)/2

	return r0

def calculate_DSS(x_label, y_label):
	max_1_y=0
	max_2_y=0
	max_1_x=0
	max_2_x=0
	num1=0
	num2=0
	I = 0
	DSS1=0
	DSS2=0
	for i,each in enumerate(x_label):
		if each>0:
			I = i
			break

	max_1_y = max(y_label[0:I])
	max_2_y = max(y_label[I:-1])
	half_max_1_y = max_1_y/2
	half_max_2_y = max_2_y/2

	for i,each in enumerate(y_label[0:I]):
		if each == max_1_y:
			max_1_x = x_label[i]
			num1=i

	for i,each in enumerate(y_label[I:-1]):
		if each == max_2_y:
			max_2_x = x_label[I+i]
			num2=i+I

	for i in range(num1,I):
		if y_label[i] < half_max_1_y:
			DSS1 = x_label[i]

	for i in range(I,num2):
		if y_label[i] > half_max_2_y:
			DSS2 = x_label[i]

	DSS = DSS2 - DSS1
	return DSS