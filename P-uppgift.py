#from queueADT import *
#from functions import *
import classes
import time
import random
from time import sleep

def enterCustomer(beingServed, kundnr, customer, storeOpen, queue, PRkick):

	def probGen(maxno):
		return random.randrange(0,maxno) == 0

	if probGen(100//PRkick) and storeOpen:														# kollar varje minut om en nu kund kommer in
		newCustomer = classes.person(kundnr, time.current)
		if newCustomer.isRobber:
			print(time, "Butiken rånas! Kön töms.")
			queue.empty()
			if probGen(random.randrange(1,5)):
				PRkick = 51
				print("Fru Franco besegrade rånaren! Hype!")
			else:
				print("Mörp. Fru Franco blev besegrad. rip.")
				PRkick = 4
			sleep(5)

		if queue.isEmpty() and not beingServed:
			customer = newCustomer
			customer.consumedTime = -1
#			print(time , "kommer kund" , customer.kundnr , "in och blir genast betjänad.")
			beingServed = True

		else:												# annars ställs personen i kön
			queue.put(newCustomer)
#			print(time , "kommer kund" , kundnr , "in och ställer sig i kön som nr." , queue.length)


		kundnr += 1

	return beingServed, kundnr, customer, storeOpen, queue, PRkick

def updateCheck():
	global beingServed
	global time
	global customer
	global queue
	global queueTime

	if beingServed == True:									# om en kund betjänas så ökas tiden det har tagit för ärendena
		customer.consumedTime += 1
		if customer.canLeave():				# om den konsumerade tiden nått 2 * ärenden minuter lämnar kunden disken och en kund hämtas från kön.
			if not queue.isEmpty():
				print(time , "går kund" , customer.kundnr , "och kund" , customer.kundnr+1 , "blir betjänad.")
				customer = None
				customer = queue.get()
				queueTime = time.current - customer.enterQueue
				#print(queueTime)
				queue.queueTime += queueTime

			else:
				print(time , "går kund", customer.kundnr)
				beingServed = False

def timeCheck():
	global time
	global storeOpen
	global queue
	global PRkick

	if time.current == 1080:
		print("Dörren stängdes 18:00.")
		storeOpen = False

	if PRkick > 20:
		PRkick -= 1
	elif PRkick < 20:
		PRkick += 1

time = classes.time() # kl 9:00
kundnr = 1
storeOpen = True
beingServed = False
queue = classes.queue()
PRkick = 20

while True:

	enterCustomer()

	updateCheck()

	timeCheck()

	if time.current >= 1080 and queue.isEmpty() and not beingServed:
		break

	time.current += 1

	#	print(time.current, storeOpen, queue.length, consumedTime, beingServed)

print("STATISTIK:" , kundnr , "kunder betjänades. Kundväntetid", queue.queueTime, "minuter =>", int(60*queue.queueTime/kundnr), "s per kund.")
