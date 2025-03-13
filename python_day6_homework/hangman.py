import random

class HangmanGame:
    def __init__(self):
        self.words = ["apple", "banana", "orange", "grape", "lemon"]
        self.hangman_pics = [ 
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
    ---"""]
        self.quiz = self.words[random.randint(0, 4)]  
        self.hidden = "_" * len(self.quiz)  
        self.count = 0 

    def display(self):
        print(self.hangman_pics[self.count])
        print(self.hidden.replace("_", " _ ")) 
            
    def user_guess(self):
        guess = input("Enter 1 character only: ").strip()
        while len(guess) != 1:  
            guess = input("Enter 1 character ONLY 🙎🏻‍♂️: ").strip()
        return guess

    def play(self):

        while True:
            if self.count != 7:
                self.display()

            # 종료 조건: 게임 시도 횟수 10 초과 또는 맞혔을 때 hidden == quiz 
            if self.count >= 7:
                print("💀 Game Over 💀")
                break 

            if self.hidden == self.quiz:
                print("🙌🏻 Congratulations! You made it! 🙌🏻")  # 맞혔을 때
                break

            # 사용자 입력 받기
            guess = self.user_guess()

            # 맞혔을 때 🙆🏻‍♂️:
            if guess in self.quiz:
                print("😳 Cool! You were right :> Cheer up!")

                # quiz에서 해당 문자가 있는 인덱스를 찾아 hidden의 _를 guess 문자로 바꿈 
                indices = [index for index, char in enumerate(self.quiz) if guess == char]  # [1, 2]
                for index in indices:
                    self.hidden = self.hidden[:index] + guess + self.hidden[index + 1:]

            # 틀렸을 때 🙅🏻‍♂️:
            if guess not in self.quiz:
                self.count += 1
                print(f'Sorry, but you were wrong! 🙅🏻‍♂️ Remaining attempts: {7 - self.count}')
                
if __name__ == "__main__": 
    game = HangmanGame()  # 게임 객체 생성
    game.play()  # 게임 시작
