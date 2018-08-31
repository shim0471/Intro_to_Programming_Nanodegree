#this is Code your Own Quiz Project file and it is 3rd version. Please check it.

import sys
""" import sys module in order to stop quiz when user's input incorrect too many."""

easy_level_text='''
---------------------------------------------------------------------------------------------------------------------------

< Star wars : the last jedi >

 plot:   The {___1___} fighters led by General Leia Organa evacuate their main base as a {___2___} fleet reaches them.
         Poe Dameron leads an effective but costly counterattack. The Resistance vessels jump into hyperspace to escape,
         but the First Order gives pursuit using a tracking device. During an attack, Leia's son, {___3___}, destroys
         the Resistance support fighters, but hesitates to fire at the lead Resistance ship after sensing his mother's
         presence on board.

         TIE fighters destroy the bridge of the ship, killing many Resistance leaders. {___4___} princess saves herself
         using the {___5___} but is incapacitated, leaving Vice Admiral Amilyn Holdo in command.

         Disapproving of her passive strategy, Poe, Finn, BB-8, and mechanic Rose Tico embark on a secret plan to
         disable the tracking device.

----------------------------------------------------------------------------------------------------------------------------'''
easy_answer=['resistance','first order','kylo ren','leia','force']


medium_level_text='''
---------------------------------------------------------------------------------------------------------------------------

< Star wars : Fact & Fiction part.01>

No.1  In "Star Wars IV: A New Hope," Han Solo boasts that the {___1___} did the Kessel Run in 12 parsecs. A parsec is a real
      term used in physics. What is a parsec? answer is {___2___}.

No.2  TIE fighters (TIE = {___3___}) use ion propulsion. This type of propulsion is also used by actual {___4___} spacecraft.
      {___4___}'s Dawn mission uses ion propulsion, which glows a blue color in its ion engines.

No.3  The ice planet Hoth is featured in " Star Wars V: {___5___}". Hoth is also the name of a real planet in our galaxy.
      There is a Hoth in our galaxy, though not the same Hoth from "Star Wars". An icy super-Earth discovered in 2006 reminded
      scientists so much of the frozen Rebel base, they unofficially nicknamed it Hoth.

----------------------------------------------------------------------------------------------------------------------------'''
medium_answer=['millennium falcon','a measure of distance','twin ion engines','nasa','the empire strikes back']


hard_level_text='''
----------------------------------------------------------------------------------------------------------------------------

< Star wars : Fact & Fiction part.02>

No.1  Which of the following Death Star technologies would be possible today? antswer is {___1___}.
      It is possible today to build a {___1___}, even one the size of the Death Star.
      NASA engineers say that {___2___} could be mined from an asteroid and the station built entirely in space.
      But it would require an Earth-wide effort with hundreds of thousands of people and trillions of dollars just to build it,
      let alone the costs of running it every day.

No.2  NASA is still looking for signs of extraterrestrial life. what chemicals another planet's atmosphere are scientists
      particularly interested in?
      Living organisms on Earth need {___3___}, and they produce {___4___} and {___5___}. so you'll find plenty all three
      in earth's atmosphere.
      each chemical could be found   separately in the atmosphere of an exoplanet hostile to life.
      but found together {___4___}, and {___5___} can be promising. so far we haven't yet found alien lite of and kind, either
      in our solar system or outside it.

-----------------------------------------------------------------------------------------------------------------------------'''
hard_answer=['the space station','metal','water','methane','oxygen']

blank=['{___1___}','{___2___}','{___3___}','{___4___}','{___5___}']


def check_answer(index,q_answer):
    """
    This function purpose is comparing user's input and correct answer.
    keyword arguments :
            iterate_num : using for while loop. (default 0)
            Incorrect_count : user's answer wrong then subtract 1 from 4. (default 4)
            max_opportunity : this number is chance to solve the blank. (default 5)
    Input :
            index : number from for statement of playing_quiz().
            q_answer : it is current level's answer.
            user_input : prompted by user.
    Behavior :
            this while loop executed in order to compare input and quiz answer.
            when user guesses incorrectly, they are prompted to try again.
    Output :
            return index. To replace correct answer and quiz blank.
    """
    iterate_num = 0
    Incorrect_count = 4 #if user's answer wrong then subtract 1 from 4.
    max_opportunity = 5 # max_opportunity is chance to solve the quiz.

    while iterate_num < max_opportunity:
        user_input = raw_input('Enter blank ' + str(index+1) + ' answer : ' ).lower()
        if user_input == q_answer[index]:
            print "Yes. Correct!!"
            break # Move to next questions.
        else:
            if Incorrect_count != 0:
                print "Incorrect. Let's try again; you have " + str(Incorrect_count) +" trys left!"
                Incorrect_count -= 1
            else:
                print "You've failed too many straight guesses!  Game over!"
                sys.exit()
        iterate_num += 1
    return index


def playing_quiz(quiz_text, q_answer, level):
    """
    This function repeat quiz's answer of a sequence in order from list.

    keyword arguments :
           index : number for loop runs for fixed amount. in this case answer list length is 5.
           after_index : this variable used replace function.
           blank : join user's correct input and text's blank.
    Input :
           quiz_text : display text with blank.
           q_answer : this type is list and include correnct quiz answers.
           level : this parameter is present user's level
    Behavior :
           executing the block each time up to complete every blank.
           and shows with correct answer in the previous blank.
    Output :
           return user's level.
    """
    print quiz_text + '\n'
    for index in range(0,len(q_answer)):
        after_index = check_answer(index,q_answer)
        quiz_text = quiz_text.replace(blank[after_index],q_answer[after_index])
        print quiz_text + '\n'

    return level



def after_playing_quiz(current_level):
    """
    Using this fuction in order to compare user's level.
    Input :
            current_level : saved return value by start_quiz().
    Behavior :
            loop quiz until hard level.
    Output :
           retrun value is None. if compared user's level is hard_level then terminate this program instantly.
    """
    while current_level != 'hard':
        if current_level == 'easy':
            print "Next level is medium........"+'\n'
            current_level = start_quiz("medium")
        elif current_level == 'medium':
            print "Next level is hard.........."+'\n'
            current_level=start_quiz('hard')
        else:
            return None


def start_quiz(level):
    """
    This function select a difficulty level from easy, medium, hard.

    keyword arguments :
            s_level : if user input wrong then try again with quiz level.
    Input :
            level from user selceted.
    Behavior :
            this fuction hand over parameters to playing_quiz() in order to fill the blank.
    Output :
            return value is current level. this value keep going the quiz until hard level.
    """
    if level=="easy":
        current_level = playing_quiz(easy_level_text, easy_answer, level)
        return current_level
    elif level == 'medium':
        current_level = playing_quiz(medium_level_text, medium_answer, level)
        return current_level
    elif level == 'hard':
        current_level = playing_quiz(hard_level_text, hard_answer, level)
        return current_level
    else:
        print "Please, Choise again."
        s_level = raw_input(': ')
        start_quiz(s_level)


def play_quiz():
    """
    This function start the quiz.
    Input :
           select_level : user is prompted to select a level.
    Behavior :
           display quiz text and continue quiz after fill the blank.
    Output :
           No return value. If user fill all blank then finish the quiz.
    """
    print '\n'+' '*12 + '''********************************

              Welcome Star wars blank Quiz

            ********************************'''+'\n'
    print "Please select a game difficulty by typing it in! \nPossible choices include easy, medium, and hard"

    selected_level = raw_input(': ').lower()
    current_level = start_quiz(selected_level)
    after_playing_quiz(current_level)

    print "Well done. Finish the Quiz. Good Bye."
    return None


play_quiz()
