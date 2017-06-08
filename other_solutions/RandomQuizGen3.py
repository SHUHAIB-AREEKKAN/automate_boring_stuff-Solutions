#! /usr/bin/python3
#random order, along with the answer key

import random

#The quiz data. Keys are states and calues are their capitals.

capitals= {'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix','Arkansas':'Little Rock',
           'California':'Sacramento','Colorado':'Denver','Connecticut':'Hartford','Delaware':'Dover',
           'Florida':'Tallahassee','Georgia':'Atlanta','Hawaii':'Honolulu','Idaho':'Boise','Illinois':'Springfield',
           'Indiana':'Indianapolios','Iowa':'Des Moines','Kansas':'Topeka','Kentucky':'Frankfort',
           'Louisiana':'Baton Rouge','Maine':'Augusta','Maryland':'Annapolis','Massachusetts':'Boston',
           'Michigan':'Lansing','Minnesota':'St. Paul','Mississippi':'Jackson','Missouri':'Jefferson City',
           'Montana':'Helena','Nebraska':'Lincoln','Nevada':'Carson City','New Hampshire':'Concord',
           'New Jersey':'Trenton','New Mexico':'Santa Fe','New Yorl':'Albany','North Carolina':'Raleigh',
           'North Dakota':'Bismark','Ohio':'Columbus','Oklahoma':'Oklahoma City','Oregon':'Salem',
           'Pennsylvania':'Harrisburg','Rhode Island':'Providence','South Carolina':'Columbia',
           'South Dakota':'Pierre','Tennessee':'Nashville','Texas':'Austin','Utah':'Salt Lake City',
           'Vermont':'Montpelier','Virginia':'Richmond','Washington':'Olympia','West Virginia':'Charleston',
           'Wisconsin':'Madison','Wyoming':'Cheyenne'}

for quizNum in range(35):
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalquiz_answers%s.txt' % (quizNum +1), 'w')

    quizFile.write('Name:\n\nDate:\n\nHour:\n\n')
    quizFile.write((' ' *20)+ 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):

        correctAnswer= capitals[states[questionNum]]
        wrongAnswers= list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
    #This is where I think I have the problem, It will not finish the test.
        quizFile.write('%s. What is the capital of %s\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')

        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
quizFile.close()
answerKeyFile.close()
