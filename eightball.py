import random
from termcolor import colored
from wizzy import print_slow, text_speed

def answerQuestion():
    responses = {"why": "Because.",
                 "how": "Very Carefully.",
                 "where": "In your butthole.",
                 "what": "I don't know",
                 "who": "well, everyone!",
                 "when": "Tomorrow.",
                 "yesNo": "It is decidedly so"}

    #Loop to answer questions until 'exit' is entered
    while True:
     answered = True
     question = input("Ask the wizard one of your burning questions! (or type 'exit' to quit): ") 
     if question.lower() == 'exit':
      print_slow("Exiting.")
      break
     if question.split()[0] == 'speed':
      text_speed(question)
      break
     else:
      for word in question.split():
        #print(f"Checking word: {word}") useful for debugging if needed
        #figure out what kind of question is being asked, to provide an appropriate response
        if word.lower() in responses:
          print_slow(responses[word])
          answered = True
          break
        else:
          answered = False
        #the answered variable comes into play here, and logs any questions that go unanswered.
      if not answered:
       print_slow("That's a new one. I'll have to perform more research before I can provide an answer.")
       #logging.info(f"Unanswered question: '{question}'")
