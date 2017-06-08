def build_periodic_table(filename="periodic_table.txt"):
    input_file = open(filename, 'r')
    table = dict()
    for element in input_file:
        tokens = element.split()
        table[tokens[2]] = (tokens[1], int(tokens[0]), float(tokens[3]))
    return table

def getInput():
	while True:
		print("1) Search by symbol/name\n2) Search by atomic mass")
		print("3) Molecular Mass Calculation\n4) Quit")
		inputNumber = input("\nPlease enter your choice: ")
		try:
			inputValue = int(inputNumber)
			if inputValue < 1 or inputValue > 4:
				print("Number entered is not a valid choice\n")
				continue
			break
		except ValueError:
			print("Input is not an integer\n")
	return inputValue

def pySwitch(choice):
	periodicTable = build_periodic_table()
	if choice == 1:
		inputStr = input("\nPlease enter a search string: ")
		resultList = searchByName(inputStr, periodicTable)
		if resultList:
			print("\t#\tElement name\t\tSym\tMass")
			print("=" * 80)
			for x in resultList:
				print("\t", x[0], "\t", x[1], "\t\t", x[2], "\t", x[3])
			print("=" * 80)
	elif choice == 2:
		inputMin = input("\nPlease enter a min mass: ")
		inputMax = input("\nPlease enter a max mass: ")
		resultList = searchByMass(inputMin, inputMax, periodicTable)
		if resultList:
			print("\t#\tElement name\t\tSym\tMass")
			print("=" * 80)
			for x in resultList:
				print("\t", x[0], "\t", x[1], "\t\t", x[2], "\t", x[3])
			print("=" * 80)
	elif choice == 3:
		print("The molecular mass is ", calculateMoleMass(periodicTable), "\n")
	elif choice == 4:
		exit()

def searchByName(inputStr, periodicTable):
	results = []
	inputStr = inputStr.lower();
	for key,val in periodicTable.items():
		tmp1 = key.lower()
		tmp2 = val[0].lower()
		if tmp1.find(inputStr) != -1:
			value = periodicTable.get(key)
			tpl = (value[1], value[0], key, value[2])
			results.append(tpl)
		elif tmp2.find(inputStr) != -1:	
			value = periodicTable.get(key)
			tpl = (value[1], value[0], key, value[2])
			results.append(tpl)
	return results

def searchByMass(minMass, maxMass, periodicTable):
	results = []
	for key,val in periodicTable.items():
		value = periodicTable.get(key)
		if float(minMass) <= value[2] and value[2] <= float(maxMass):
			tpl = (value[1], value[0], key, value[2])
			results.append(tpl)
	return results

def calculateMoleMass(periodicTable):
	moleList = []
	result = []
	while True:
		inputStr = input("\nPlease enter an atomic symbol: ")
		if inputElement == '.':
			break
		inputAtoms = input("\nPlease enter number of atoms in molecule: ")
		inputStr = inputStr.lower();
		for key,val in periodicTable.items():
			tmp1 = key.lower()
			tmp2 = val[0].lower()
			if tmp1.find(inputStr) != -1:
				tpl = tmp2 + inputAtoms
				moleList = moleList.append(tpl)
			else:
				print("Molecular formula contains an unkown element")
				break
	if moleList:
		for x in moleList:
			result = result + (x[1] * x[0])
	return result

while True:
	pySwitch(getInput())