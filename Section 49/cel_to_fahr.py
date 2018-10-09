temperatures = [10, -20, 100]

def cel_to_fahr(celsius):
	fahr = celsius * 9/5 + 32
	return fahr

for temp in temperatures:
	fahr = cel_to_fahr(temp)
	print(fahr)
