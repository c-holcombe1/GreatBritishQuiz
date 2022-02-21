print('Welcome to QI')
answer=input('Are you ready to play the Great British Quiz? (yes/no) :')
score=0
total_questions=3

if answer.lower()=='yes':
    answer=input('Question 1: For its size, where has more tornadoes than any other country in the world.?')
    if answer.lower()=='britain':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')


    answer=input('Question 2: True or False,the average Briton spends a year of their working life off sick? ')
    if answer.lower()=='true':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 3: When Winston Churchill visited the US during Prohibition, he got a doctor’s prescription for an unlimited supply of what?')
    if answer.lower()=='alcohol':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

print('Thankyou for Playing this small British quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
