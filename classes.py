from functions import noErrands

class time():
	def __init__(self):
		self.current = 540

	def get(self):
		timme = str(self.current//60)
		minut = str(self.current%60)
		if len(minut) is 1:
			minut = "0" + minut

		return str("Kl. " + str(timme) + ":" + minut)

class person():
	def __init__(self, custNo = 0):
		self.errands = noErrands()
		self.kundnr = custNo
