from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    return True if answer == question["answer"] else False      #remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    count=0
    life=0
    total=0
    while(count<15):

        print(f'\tQuestion {count+1}: {QUESTIONS[count]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[count]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[count]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[count]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[count]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')

        # check for the input validations
        if ans.lower()=='quit':
            print(total)
            break;
        if ans=='lifeline' and life==0:
             op="option"+str(QUESTIONS[count]["answer"])
             flag=0
             print("The new options are: \n")
             for i in ['option1','option2','option3','option4']:
                 if op==i:
                     print(f'\t\t\t{op}: {QUESTIONS[count][op]}')
                     continue
                 elif flag==0:
                     print(f'\t\t\t{i}: {QUESTIONS[count][i]}')
                     flag=1
             life=1
             ans = input('Your choice ( 1-4 ) : ')


        if isAnswerCorrect(QUESTIONS[count], int(ans) ):
            print('\nCorrect !')
            print(f'You have won {QUESTIONS[count]["money"]} rupees !!!')
            total=QUESTIONS[count]["money"]+total
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            

        else:
            # end the game now.
            # also print the correct answer
            print('\nIncorrect !')
            op="option"+str(QUESTIONS[count]["answer"])
            print(f'The correct answer is {QUESTIONS[count][op]}')
            if(count<6):
                print('\n0 rupees won')
            elif(6<=count<10):
                print('\n 10,000 rupees won')
            elif(10<=count):
                print('\n 3,20,000 rupees won ')
            break
        # print the total money won in the end.
        count+=1

kbc()
