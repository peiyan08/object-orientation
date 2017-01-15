"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

2. What is a class?

3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.


"""


# Parts 2 through 5:
# Create your classes and class methods
class Student(object):
    """Create student instances with first name, last name and address"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Create Question instances with question and correct_answer.

       It also has a ask_and_evaluate method that check if the user's
       answer is the same as the correct answer."""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer


    def ask_and_evaluate(self, question, correct_answer):
        user_answer = raw_input("%s: " % question)
        if user_answer == correct_answer:
            return True
        else:
            return False


class Exam(Question):
    """Create Exam instance with a exam name.

       It has method add_question that create list of Question instances.
       It also has a administer method which keep tracking of how well the
       user did."""

    def __init__(self, name):
        self.name = name
        self.questions = []


    def add_question(self, question, correct_answer):
        self.questions.append(Question(question, correct_answer))


    def administer(self):
        self.score = 0
        for question in self.questions:
            if super(Exam, self).ask_and_evaluate(question.question,question.correct_answer):
                self.score += 1
        percentage_score = float(self.score)/len(self.questions)
        print "Your accuracy is %.2f." % percentage_score
        return percentage_score

class Quiz(Exam):
    """Create Quiz instance that inherient from Exam Class

    It has its own version of the administer method, which evaluates
    if the user has passed/failed the quiz."""

    def administer(self):
        self.quiz_score = 0
        for question in self.questions:
            if super(Exam, self).ask_and_evaluate(question.question,question.correct_answer):
                self.quiz_score += 1
        percentage_score = float(self.quiz_score)/len(self.questions)
        if percentage_score >= 0.5:
            print "Congrats! You have passed the quiz!"
            return True
        else:
            print "Failed! You have failed the quiz, please try harder next time!"
            return False


"""Test One"""
print "Now you are taking an Exam"
exam = Exam("final_exam")
exam.add_question("What is the method for adding an element to a set?", ".add()")
exam.add_question("What is the method for adding an additional element into the list?", ".append()")
exam.add_question("What is the method for adding a list of elements to a list?", ".extend()")

student = Student("Amy","White", "1304 Post St. San Francisco CA 94113")
def take_test(exam, student):
    score = exam.administer()
    Student.score = score
    

take_test(exam, student)

"""Test Two"""
print "Now you are taking the second exam."
def example():
    new_exam = Exam("second_final")
    new_exam.add_question("What is the method for sorting a list in place?", ".sort()")
    new_exam.add_question("What is the method for sorting a list not in place?", "sorted()")
    new_exam.add_question("What is the method for poping an element from a list?", ".pop()")
    new_student = Student("peiyan", "zhao", "668 Sutter St. San Francisco, CA, 94102")
    take_test(new_exam, new_student)

example()

"""Test Three -- Quiz"""
print "Now you are taking a quiz."
q1 = Quiz("first quiz")
q1.add_question("How to get the length of a list?", "len()")
q1.add_question("How to get all the keys from a dictionary?", ".keys()")
q1.add_question("How to check if the key existed in the dictionary?", ".get()")

def starting_quiz(q1):
    q1.administer()

starting_quiz(q1)

