#step 1
word_list=["ardvark","baboon","camel"]
''''
#TODO1 --> Randomly choose a word from the word_list and assign it to a variable

#TODO2--> Ask the user to guess a letter and assign their answer to a variable called guess make guess lowercase


#TODO3--> Check if the letter the user guessed is one of the letter in the chosen_word

'''

#TODO1
import random

choosen_word=random.choice(word_list)
display=[]
lives=6
for _ in range(len(choosen_word)):
    display+='_'
#TODO2:
print(display)
end_of_game=False
while not end_of_game:
    guess=input("Guess a Letter: ").lower()

#TODO3
    for position in range(len(choosen_word)):
      letter=choosen_word[position]
      #print(f"Current position:{position}\n Current letter:{letter}\n Guess Letter:{guess}")
      if letter==guess:
        display[position]=letter
     


    if guess not in choosen_word:
       lives=-1
       if lives==0:
          end_of_game=True
          print("You Loose")
          
    
    print(f"{' '.join(display)}")

    if "_" not in display:
       end_of_game=True
       print("You Win")
    

    