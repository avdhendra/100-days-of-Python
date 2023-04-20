from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    pair = Question(q_text, q_answer)
    question_bank.append(pair)
    # We created a list of questions (question_bank) where
    # we're adding each question/answer pair to.

game_quiz = QuizBrain(question_bank)
while game_quiz.still_has_questions():
    game_quiz.next_question()
print('You reached the end of the Quiz!')
print(f'Your total score was {game_quiz.score}/{len(question_bank)}')