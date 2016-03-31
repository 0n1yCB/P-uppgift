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

	def __str__(self):
		hour = str(self.current//60)
		minute = str(self.current%60)
		if len(hour) is 1:
			hour = "0" + hour
		if len(minute) is 1:
			minute = "0" + minute

		return str("Kl. " + str(hour) + ":" + minute)

class person():
	def __init__(self, custNo = 0):
		self.errands = noErrands()
		self.kundnr = custNo
