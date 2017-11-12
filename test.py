def newPrediction(a,b,c,d,e):

	a2 =-1
	b2=-1
	c2=-1
	d2=-1
	e2=-1

	if (a > 50):
		a2 = 1
	else:
		a2 = 0
	if (b > 50):
		b2 = 1
	else:
		b2 = 0
	if (c > 50):
		c2 = 1
	else:
		c2 = 0
	if (d > 50):
		d2 = 1
	else:
		d2 = 0
	if (e > 50):
		e2 = 1
	else:
		e2 = 0

	test = True;

	if(test == True):
		if(a>b):
			return 0
		else: return 1
	else: return 2
