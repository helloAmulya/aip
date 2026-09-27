#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random, os

# states and their capitals

capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

# os.makedirs("capitalsQuiz", exist_ok=True)
os.makedirs("capitalsQuiz/quizzes", exist_ok=True)
os.makedirs("capitalsQuiz/ans_key", exist_ok=True)

# Generate 35 quiz files.
for quizNum in range(35):

    quizfile = open("capitalsQuiz/quizzes/capitalquiz%s.txt" % (quizNum + 1), "w")
    answerKeyfile = open("capitalsQuiz/ans_key/capitalAns%s.txt" % (quizNum + 1), "w")

    quizfile.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quizfile.write((" " * 20) + "State Capitals Quiz (Form %s)" % (quizNum + 1))
    quizfile.write("\n\n")

    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each.

    for questionNum in range(50):
        correctAns = capitals[states[questionNum]]
        wrongAns = list(capitals.values())
        del wrongAns[wrongAns.index(correctAns)]
        wrongAns = random.sample(wrongAns, 3)
        ansOptions = wrongAns + [correctAns]
        random.shuffle(ansOptions)

        quizfile.write(
            "%s. What is the capital of %s?\n" % (questionNum + 1, states[questionNum])
        )
        for i in range(4):
            quizfile.write(" %s. %s\n" % ("ABCD"[i], ansOptions[i]))
            quizfile.write("\n")

        answerKeyfile.write(
            "%s. %s\n" % (questionNum + 1, "ABCD"[ansOptions.index(correctAns)])
        )

    quizfile.close()
    answerKeyfile.close()
