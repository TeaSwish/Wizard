import random
import logging
import sys
import time

logging.basicConfig(filename='wiz.log',level=logging.DEBUG)


def main():
    global questionsAnswered
    questionsAnswered = 0
    textSpeed("speed medium")  # default text speed
    # intro()


def textSpeed(question):
    global delay
    speed = question.lower()
    match speed:
        case "speed slow":
            delay = 0.05
            slowPrint("Text speed set to slow.")
        case "speed medium":
            delay = 0.03
            slowPrint("Text speed set to medium.")
        case "speed fast":
            delay = 0.01
            slowPrint("Text speed set to fast.")
        case _:
            delay = 0.03  # default to medium
            slowPrint("Unrecognized speed, options are slow, medium(current speed), fast.")
    


def slowPrint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # for newline after the message is printed


def intro():
    slowPrint(
        "Welcome, to The Unreasonable Wizard!\nThere are three text speeds. This is medium speed. If at any time you would like to change the speed, please type 'speed' followed by 'slow', 'medium', or 'fast'."
    )
    time.sleep(1)
    print(
        r"""                    ____
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
  """
    )

    slowPrint(
        "After many years of searching far and wide, you have finally made it to the the Tower of the Unreasonable Wizard."
    )
    slowPrint(
        "Across the lands it is known that the wizard has the means to answer any question, but has a deep hatred of so called 'questions of reason'."
    )


def respondToQuestions():
    global questionsAnswered
    question = input(
        "Ask the wizard one of your burning questions! (or type 'exit' to quit): "
    )
    #This is for debug purposes, to be removed later, like a devkit.
    if question.split()[0] == 'debug':
        if question.split()[1] == 'answer#':
            questionsAnswered = int(question.split()[2])
    answer = getAnswer(question)
    if answer == "Exiting.":
        slowPrint("Exiting...")
        return
    elif answer == "speed":
        respondToQuestions()
        return
    response = getAction(answer, question)
    slowPrint(response)
    respondToQuestions()


def getAction(answer, question):
    global questionsAnswered
    actions = [
f'''The wizard produces from his sleeve a small vial of pink liquid.
He downs it in one gulp, and vanishes in a puff of smoke...
The front door swings open behind you, the wizard saunters in and proudly proclaims:
"{answer}"'''
,
'''"Excuse me while I consult the stars."
The wizard ascends the spiral staircase that wraps along the inner wall of the tower.
You hear some clattering noises from upstairs, then a muffled "OF COURSE!"
The wizard makes his way back downstairs.
"It is daytime."'''
,
'''The wizard takes from his pocket a large coin.
"I'll let the fates answer this one."
He flips the coin into the air...
It tumbles down...
The coin lands perfectly on the thin edge.
"Hmm. I guess the fates are at lunch."'''
,
'''"I think my fiancee's cousin's plumber's old college roommate would know this one."
"What was his name again...? Hmm... Donny? Danny? Dolan? Duncan?..."
"I can't quite recall. I'm sure he'll pop into my head later."'''
,
f'''The wizard goes to a nearby chest, and from it retrieves a single egg.
He cracks the egg over his counter, and peers intently at the contents.
...
It seems to be an entirely ordinary egg.
...
"Well, this is CLEARLY the wrong egg."
He retrieves another egg from the chest, cracks it open, and...
A note drops onto the counter. He reads it aloud:
"{answer}"
He pulls a pocketwatch from his robe. He clicks a button on top.
You hear a soft ticking as both eggs reassemble themselves and hover back into the chest.'''
,
f'''The wizard tosses a handful of multicolored rocks onto the counter.
The rocks clatter and roll around for a moment, then settle.
They arrange themselves into a neat circle.
The wizard stares deeply into the circle.
...
...
...
...He continues staring into the circle...
...
...
...
...Has he fallen asleep?...
...
...
...
...No, wait! He blinks!
He looks up at you and says:
"{answer}"'''
,
f'''The wizard walks over and opens a nearby window.
You hear a loud *THUD* from a different window.
"Ah, wrong window."
The wizard once again retrieves his pocketwatch. He clicks the button on top.
You hear a soft ticking as the first window reseals itself, and the wizard opens the correct window.
A small owl flies in and drops a scroll onto the counter.
The wizard reads the scroll:
"{answer}"'''
,
f'''The wizard pulls from his robe a crystal ball.
He places the crystal ball on the counter, and peers into it.
The crystal ball swirls with misty colors...
Scenes begin to unfold within the crystal ball...
Memories?
A vision of the future?
The wizard in bed with your mother?
The ball becomes cloudy once more.
"I see... I see..."
"{answer}"'''
,
f'''The wizard pulls a hammer off of the wall.
He raises the hammer high above his head, and brings it down with a mighty crash onto the crystal ball.
The crystal ball shatters into a thousand pieces.
Right where the ball sat, lays a small note.
The wizard picks up the note and reads it aloud:
"{answer}"'''
,
f'''Just as the wizard goes to speak, a bolt of lightning crashes through the still open window!
The wizard is thrown back against the wall, and slumps to the floor, unconscious.
You hear footsteps coming down the spiral staircase.
A hooded figure enters the room, and approaches the slumped wizard.
He checks the wizard's pulse, then looks back at you and shakes his head.
He apporaches the counter, and you can finally get a clear look at him.
It's... the wizard!?
"Boy, am I glad I'm not that guy!" He points with one thumb over his shoulder.
"Anywhoo... the answer to your question is..."
The slumped wizard melts into the ground, and disappears completely
"{answer}"'''
,
f'''"Well, certainly you know the answer to that one yourself!"
The wizard glares at you for a moment.
Suddenly, you realize that you DO know the answer to this one.
But you could swear that you didn't know it before coming here...
"{answer}"'''
,
f'''The wizard pulls a large book from a nearby shelf.
He blows the dust off the cover, and opens it to a random page.
He scans the page for a moment, then looks up at you.
"Hmm. According to this, the answer is..."
"{answer}"'''
,
f'''"Ah, yes! I remember now!"
The wizard claps his hands together.
He paces back and forth for a moment, then stops and looks at you.
"The answer is..."
"{answer}"'''
,
f'''The wizard pulls a small rectangular device from his robe.
"Hey Siri, {question}"
The device beeps, then speaks:
"{answer}"'''
,
'''"42."'''
,
'''The wizard pulls something wrapped in fabric out of a drawer.
He sets the object on the counter between you, and unwraps it.
You recognize it as a tarot deck.
The wizard shuffles the deck, then deals one card face up...
The Tower...
"oooh, That's not good.'''
,
f'''The wizard pulls a small black ball from his robe.
He looks at it intently, then mumbles something under his breath.
He gives the ball a shake, then stares into it.
He looks up at you.
"{answer}"'''
,
f'''"DESMOND!" The wizard shouts at the top of his lungs.
The wizard quickly scrawls a note on a piece of parchment.
He seals it with wax, and writes in big bold letters "TO DESMOND" on the outside.
The wizard then tosses the note into a nearby fireplace.
After a moment, a small raven flies in through the open window, carrying a similar note.
The wizard takes the note from the raven, and reads it aloud:
""{answer}", Love Desmond."
"Lovely guy, despite the name."'''
,
'''[CENSORED FOR YOUR PROTECTION]'''
,
f'''"{answer}"
...
...
...
...
...
...
...
...
...
...
...
...
...
...
"What, why are you staring at me?"
"Is that not magical enough for you?"
"Are you expecting me to do some elaborate ritual or something?"
"I already knew this one, so that's that."'''
]
    if questionsAnswered >= len(actions):
        questionsAnswered = 0
    action = actions[questionsAnswered]
    questionsAnswered += 1
    return action


def getAnswer(question):
    answer = None

    yesNo = ["will", "do", "does", "is", "are", "has", "have", "was", "were"]

    responses = {
        "why": ["It is what it is", "Because."],
        "how": ["It is what it is", "Very carefully."],
        "where": ["It is what it is", "In your butthole."],
        "what": ["It is what it is", "I don't know"],
        "who": ["It is what it is", "well, everyone!"],
        "when": ["It is what it is", "Tomorrow."],
        "yesno": [
            "It is decidedly so",
            "Maybe",
            "Possibly.",
            "I wouldn't count on it.",
            "There's a good chance.",
            "It's unlikely.",
            "It is what it is",
        ],
    }

    if question.lower() == "exit":
        return "Exiting."
    if question.split()[0] == "speed":
        textSpeed(question)
        return "speed"
    else:
        for word in question.split():
            # figure out what kind of question is being asked, to provide an appropriate response
            if word.lower() in yesNo:
                word = "yesNo"
            if word.lower() in responses:
                answer = responses[word.lower()][
                    random.randint(0, len(responses[word.lower()]) - 1)
                ]
        if answer is None:
            logging.info(f"Unanswered question: '{question}'")
            return "That's a new one. I'll have to perform more research before I can provide an answer."
        return answer

main()
respondToQuestions()

