import random
import logging
import sys
import time

logging.basicConfig(filename='wiz.log',level=logging.DEBUG)

def main():
  text_speed('speed medium') #default text speed
  intro()

def text_speed(question):
    global delay
    if question.lower() == 'speed slow':
        delay = 0.05
    elif question.lower() == 'speed medium':
        delay = 0.03
    elif question.lower() == 'speed fast':
        delay = 0.01
    else:
        delay = 0.05  # default to medium if unrecognized
    print_slow(f"Text speed set to {question.split()[1]}.")

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print() # for newline after the message is printed

def intro():
  print_slow("Welcome, to The Unreasonable Wizard!\nThere are three text speeds. This is medium speed. If at any time you would like to change the speed, please type 'speed' followed by 'slow', 'medium', or 'fast'.")
  time.sleep(1)
  print(r"""                    ____
                  .'* *.'
               __/_*_*(_
              / _______ \
             _\_)/___\(_/_
            / _((\- -/))_ \
            \ \())(-)(()/ /
             ' \(((()))/ '
            / ' \)).))/ ' \
           / _ \ - | - /_  \
          (   ( .;''';. .'  )
          _\"__ /    )\ __"/_
            \/  \   ' /  \/
             .'  '...' ' )
              / /  |  \ \
             / .   .   . \
            /   .     .   \
           /   /   |   \   \
         .'   /    b    '.  '.
     _.-'    /     Bb     '-. '-._
 _.-'       |      BBb       '-.  '-.
(________mrf\____.dBBBb.________)____)
  """)
  
  print_slow("After many years of searching far and wide, you have finally made it to the the Tower of the Unreasonable Wizard.")
  print_slow("Across the lands it is known that the wizard has the means to answer any question, but has a deep hatred of so called 'questions of reason'.") 

def answerQuestion():
    yesNo = ['will','do','does','is','are','has','have']

    responses = {"why": "Because.",
                 "how": "Very Carefully.",
                 "where": "In your butthole.",
                 "what": "I don't know",
                 "who": "well, everyone!",
                 "when": "Tomorrow.",
                 "yesno": ["It is decidedly so", "Maybe", "Possibly.", "I wouldn't count on it.", "There's a good chance.", "It's unlikely."],}

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
        #figure out what kind of question is being asked, to provide an appropriate response
        if word.lower() in yesNo:
          word = 'yesNo'
        if word.lower() in responses:
          print_slow(responses[word.lower()][random.randint(0, len(responses[word.lower()])-1)])
          answered = True
          break
        else:
          answered = False
        #the answered variable comes into play here, and logs any questions that go unanswered.
      if not answered:
       print_slow("That's a new one. I'll have to perform more research before I can provide an answer.")
       logging.info(f"Unanswered question: '{question}'")

main()
answerQuestion()