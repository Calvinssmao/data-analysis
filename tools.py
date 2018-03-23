def calculate_gap(x_label, y_label):
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

	gap = max_2_x-max_1_x

	return gap