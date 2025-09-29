import random
import logging

logging.basicConfig(filename='wiz.log',level=logging.DEBUG)


def main():
	intro()
	question = input("Ask the wizard one of your burning questions! (or type 'exit' to quit): ") 
	answerQuestion(question)

def intro():
	print("After many years of searching far and wide, you have finally made it tho the Tower of the Unreasonable Wizard.")
	print("Across the lands it is known that the wizard has the means to answer any question, but has a deep hatred of so called 'questions of reason'.") 
#Loop to answer questions until 'exit' is entered
def answerQuestion(question):
    while True:
     answered = True
     if question.lower() == 'exit':
      print("Exiting.")
      break
     else:
      for word in question.split():
			#print(f"Checking word: {word}") useful for debugging if needed
			#figure out what kind of question is being asked, to provide an appropriate response
       if word.lower() == 'why':
        print("Because.")
        break
       elif word.lower() == 'how':
        print("Very Carefully.")
        break
       elif word.lower() == 'where':
        print("In your butthole.")
        break
       elif word.lower() == 'what':
        print("I don't know, man.")
        break
       elif word.lower() == 'who':
        print("well, everyone!")
        break
       elif word.lower() == 'when':
        print("Tomorrow.")
        break
       elif word.lower() in ('will','do','does','is','are','has','have'):
        print("It is decidedly so")
        break
       else:
        answered = False
		#the answered variable comes into play here, and logs any questions that go unanswered.
      if not answered:
       print("That's a new one. I'll have to perform more research before I can provide an answer.")
       logging.info(f"Unanswered question: '{question}'")

