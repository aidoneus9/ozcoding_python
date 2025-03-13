# hangman.py 파일 참고해서 약간 고쳐야 함.

import random

words = ["apple", "banana", "orange", "grape", "lemon"] 

hangman_pics = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\
     |   /
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\
     |   / \
     |
    ---""",
]

quiz = words[random.randint(0,4)] # -> "apple"
hidden = "_" * len(quiz) # <- 🚨 길이가 3인...리스트에 안 넣으면 해결 안 됨.  Show / 각 기능 함수로 바꾸기 
print(hidden.replace("_", " _ " ))

count = 0

while True:
    
    # while 종료 조건: 게임 시도 횟수 10 초과 또는 맞혔을 때 hidden == quiz 
    if count >= 7:
        print("💀 Game Over 💀")
        break 

    if hidden == quiz:
        print("🙌🏻 Congratulations! You made it! 🙌🏻") ## 일단 한 번만 풀 수 있음 
        break

    # 사용자의 시도

    def user_guess():
        guess = input("Enter 1 character only: ").strip()
        while(len(guess) != 1):
            guess = input("Enter 1 character ONLY 🙎🏻‍♂️: ").strip()
        return guess
    
    guess = user_guess()
            
    # 🚨 맞혔을 때:
    if guess in quiz:  
        print("😳 Cool! You were right :> Cheer up!")

        # quiz에서 해당 문자가 있는 인덱스를 찾아 hidden의 _를 guess 문자로 바꿈 
        indices = [index for index, char in enumerate(quiz) if guess == char] # [1, 2]
        for index in indices:
            hidden = hidden[:index] + guess + hidden[index + 1:]

        print(hidden.replace("_", " _ ")) 

    # 틀렸을 때:     
    if guess not in quiz: 
        count += 1
        print(f'Sorry, but you were wrong! 🙅🏻‍♂️ Remaining attempts: {7 - count}')
        print(hangman_pics[count - 1]) 🖼️     
        


    


    


         

