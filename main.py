import random
import hangman_art
import hangman_words


def main():
    wrong = 0
    win = False
    current_stage = 6

    word_list = hangman_words.word_list
    stages = hangman_art.stages

    chosen_word = random.choice(word_list)

    blanks = list(chosen_word)
    word_length = len(chosen_word)

    for x in range(0, word_length):
        blanks[x] = "_ "
    print(hangman_art.logo)
    print(stages[6])
    print(blanks)

    while wrong < 6 and win is False:

        guess = input("Please choose a letter\n").lower()

        for x in range(0, word_length):
            if guess == chosen_word[x]:
                blanks[x] = guess

        if guess not in chosen_word:
            wrong += 1
            current_stage -= 1
            print(stages[current_stage])
            print(guess, "was incorrect.")
        else:
            print(guess, "was correct.")

        if wrong >= 6:
            print("You lose!")

        if "_ " not in blanks:
            win = True
        if wrong < 6:
            print(blanks)
        if win:
            print("You win!")


if __name__ == '__main__':
    main()
