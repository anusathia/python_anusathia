import random
word_list=["apple","beautiful","potato"]
chosen_word=random.choice(word_list)
print(chosen_word)
lives=6
display=[]
for i in range(len(chosen_word)):#0 1 2 3 4  5 #apple
    display+='_'
print(display)
game_over=False
while not game_over: #True#we use while loop because we dont know how many times this will run 
    guessed_letter=input("Guess a letter:").lower()  #p  _pp_ _
    for position in range(len(chosen_word)): #01234
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You lose!!")
    if '_' not in display:
        game_over=True
        print("you win")
     
