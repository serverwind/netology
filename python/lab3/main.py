arr = ['python', 'c++', 'c', 'scala', 'java']

def count_letter(arr, letter):
	amount = 0
	for word in arr:
		if letter in word:
			amount +=1
	print(amount)
	return amount

count_letter(arr, 'a')