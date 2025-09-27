import random
import logging

logging.basicConfig(filename='wiz.log',level=logging.DEBUG)

#Loop to answer questions until 'exit' is entered
while True:
	answered = False
	question = input("Ask the wizard one of your burning questions! (or type 'exit' to quit): ")
	if question.lower() == 'exit':
		print("Exiting.")
		break
	else:
		for word in question.split():
			#print(f"Checking word: {word}") useful for debugging if needed
			#figure out what kind of question is being asked, to provide an appropriate response
			if word.lower() == 'why':
				print("Because.")
				answered = True
				break
			elif word.lower() == 'how':
				print("Very Carefully.")
				answered = True
				break
			elif word.lower() == 'where':
				print("In your butthole.")
				answered = True
				break
			elif word.lower() == 'what':
				print("I don't know, man.")
				answered = True
				break
			elif word.lower() == 'who':
				print("well, everyone!")
				answered = True
				break
			elif word.lower() == 'when':
				print("Tomorrow.")
				answered = True
				break
			elif word.lower() in ('will','do','does','is','are','has','have'):
				print("It is decidedly so.")
				answered = True
				break
		#the answered variable comes into play here, and logs any questions that go unanswered.
		if not answered:
			print("That's a new one. I'll have to perform more research before I can provide an answer.")
			logging.info(f"Unanswered question: '{question}'")
