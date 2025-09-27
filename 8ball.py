import random
from termcolor import colored

responses = [
"The stones have foretold... Yes.",
"Hmmm. Well. I don't think so..",
"BAH! Of course not!",
"Maybe.... Yes. I think so..",
"Perhaps.",
"Hmmm. Let's see here...\nThe wizard is consulting his manuscripts\nAH! Evidently, no."
]

exitMessages = [
"Oh, you're done? A pity.",
"And I was just starting to like you...",
"Good. I can go back to my reading."
]

#Ask for an input question until the user inputs 'exit', at which point print a random exitMessage and close
while True:
	question = input("Ask the wizard one of your burning questions! (or type 'exit' to quit): ")
	if question.lower() == 'exit':
		print(colored(random.choice(exitMessages),'green'))
		break
	else:
		print(colored(random.choice(responses),'green'))
