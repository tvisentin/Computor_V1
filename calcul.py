def handleDegree(degree, equa):
	if degree < 2:
		if degree == 0:
			r = equa[0]
		if degree == 1:
			r = (equa[0] / equa[1]) * -1
		toPrint = str(r)
		if (toPrint.find('.0') != -1):
			toPrint = toPrint[:toPrint.find('.0')]
		print 'The solution is:\n', toPrint
	else:
		r = solverSecondDegree(equa)


def solverSecondDegree(equa):
	delta = calculDelta(equa[2], equa[1], equa[0])
	if (delta < 0):
		print 'No solutions here'
	elif (delta == 0):
		print 'Discriminant is equal 0, the only solutions is:'
		print calculZero(equa[2], equa[1])
	else:
		print 'Discriminant is strictly positive, the two solutions are:'
		print calculSupPositive(delta, equa[2], equa[1])
		print calculSupNegative(delta, equa[2], equa[1])

def calculDelta(a, b, c):
	return ((b * b) - (4 * a * c))

def calculZero(a, b):
	return (b / (2 * a)) * -1

def calculSupPositive(delta, a, b):
	return 0

def calculSupNegative(delta, a, b):
	return 0