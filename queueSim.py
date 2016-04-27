
import classes
import random
from time import sleep
from math import ceil

def enterCustomer(beingServed, kundnr, customer, storeOpen, queue, enterProbability, systemTime):

	def probGen(probability):
		return random.randrange(0,100) <= probability

	if probGen(enterProbability) and storeOpen:														# kollar varje minut om en nu kund kommer in
		newCustomer = classes.person(kundnr, systemTime.current)		# Skapa ny kund med ett kundnr och ange tiden som den kom in

		if newCustomer.isRobber:
			print(systemTime, "Butiken rånas! Kön töms.", ceil(queue.length*random.random()), "personer skjuts ned.")
			queue.empty()
			if probGen(random.random()*100):						# Slumpa sannolikhet att fru Franco vinner
				enterProbability = 51
				print("Fru Franco besegrade rånaren! Hype!")
			else:
				print("Mörp. Fru Franco blev besegrad. RIP.")
				enterProbability = 4
			sleep(5)

		if queue.isEmpty() and not beingServed:
			customer = newCustomer
			customer.consumedTime = -1
			print(systemTime , "kommer kund" , customer.kundnr , "in och blir genast betjänad.")
			beingServed = True

		else:												# annars ställs personen i kön
			queue.put(newCustomer)
			print(systemTime , "kommer kund" , kundnr , "in och ställer sig i kön som nr." , queue.length)

		kundnr += 1

	return beingServed, kundnr, customer, storeOpen, queue, enterProbability

#########################################################################################
#########################################################################################
#########################################################################################

def updateCheck(beingServed, customer, storeOpen, queue, systemTime):

	if beingServed is True:									# om en kund betjänas så ökas tiden det har tagit för ärendena
		customer.consumedTime += 1
		if customer.canLeave():				# om den konsumerade tiden nått 2 * ärenden minuter lämnar kunden disken och en kund hämtas från kön.
			if not queue.isEmpty():
				print(systemTime , "går kund" , customer.kundnr , "och kund" , customer.kundnr+1 , "blir betjänad.")
				customer = None
				customer = queue.get()
				queueTime = systemTime.current - customer.enterQueue			# Beräkna tiden som kunden stått i kön och addera till den totala summan
				queue.queueTime += queueTime

			else:
				print(systemTime , "går kund", customer.kundnr)
				beingServed = False

	return beingServed, customer, storeOpen, queue

#########################################################################################
#########################################################################################
#########################################################################################

def timeCheck(systemTime, storeOpen, enterProbability):

	if systemTime.current == 1080:					# Om klockan är 18:00 stängs dörren och inga fler kunder får komma in.
		print("Dörren stängdes 18:00.")
		storeOpen = False

	if enterProbability > 20:						# Om sannolikheten att en kund ska komma in inte är 20 kommer den att ökas/minskas.
		enterProbability -= 1
	elif enterProbability < 20:
		enterProbability += 1

	return storeOpen, enterProbability

#########################################################################################
#########################################################################################
#########################################################################################

def queueSim():

	systemTime = classes.time() # kl 9:00
	kundnr = 1					# Första kundern är nummer 1
	storeOpen = True
	beingServed = False
	queue = classes.queue()
	enterProbability = 20
	customer = None

	while True: # Loopa tills klockan är 18:00 och alla kunder har blivit betjänade.

		beingServed, kundnr, customer, storeOpen, queue, enterProbability = enterCustomer(beingServed, kundnr, customer, storeOpen, queue, enterProbability, systemTime)

		beingServed, customer, storeOpen, queue = updateCheck(beingServed, customer, storeOpen, queue, systemTime)

		storeOpen, enterProbability = timeCheck(systemTime, storeOpen, enterProbability)

		if systemTime.current >= 1080 and queue.isEmpty() and not beingServed:
			break

		systemTime.current += 1


	print("STATISTIK:" , kundnr , "kunder betjänades. Kundväntetid", queue.queueTime, "minuter =>", int(60*queue.queueTime/kundnr), "s per kund.")

queueSim()
