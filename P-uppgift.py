#from queueADT import *
from functions import *
import classes
import time
import random

def enterCustomer():
	global beingServed
	global kundnr
	global customer
	global storeOpen
	global queue

	def newCustomer():
		if random.randrange(0,5) == 0:
			return True

	if newCustomer() and storeOpen:														# kollar varje minut om en nu kund kommer in
		if queue.isEmpty() and not beingServed:
			customer = classes.person(kundnr, -1)
			print(time , "kommer kund" , customer.kundnr , "in och blir genast betjänad.")
			kundnr += 1
			beingServed = True

		else:												# annars ställs personen i kön
			queue.put(classes.person(kundnr))
			kundnr += 1
			print(time , "kommer kund" , kundnr-1 , "in och ställer sig i kön som nr." , queue.length)


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
			else:
				print(time , "går kund", customer.kundnr)
				beingServed = False

def timeCheck():
	global time
	global storeOpen
	global queue

	if time.current == 1080:
		print("Dörren stängdes 18:00.")
		storeOpen = False

	if not queue.isEmpty():
		queue.queueTime += 1



time = classes.time() # kl 9:00
kundnr = 1
storeOpen = True
beingServed = False
queue = classes.queue()

while True:

	enterCustomer()

	updateCheck()

	timeCheck()

	if time.current >= 1080 and queue.isEmpty() and not beingServed:
		break

	time.current += 1

	#	print(time.current, storeOpen, queue.length, consumedTime, beingServed)

print("STATISTIK:" , kundnr , "kunder betjänades. Kundväntetid", queue.queueTime, "minuter =>", int(60*queue.queueTime/kundnr), "s per kund.")
