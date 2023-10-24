n = int(input())
index = total = current = 0
while index != n:
	number = int(input())
	if number:
		current += 1
		total = max(current, total)
	else:
		current = 0
	index += 1
print(total)