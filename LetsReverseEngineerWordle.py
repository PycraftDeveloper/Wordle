#type: ignore

# 1. - Setup
import random, os

base_folder = os.path.dirname(__file__)
os.environ['SDL_VIDEO_CENTERED'] = '1'

Dictionary_Location = os.path.join(base_folder, "resources\\Dictionary.txt")
with open(Dictionary_Location, "r") as file:
    Dictionary = file.readlines()

# 2. - Mathematically perfect starter word
# 2.a - Count number of occurances of each letter in dictionary
AllData = ""
for word in Dictionary:
    AllData += word.strip()

Letters = "qwertyuiopasdfghjklzxcvbnm"
Breakdown = {}
for letter in Letters:
    Breakdown[letter] = AllData.count(letter)

# 2.b - Filter the dictionary to remove all words with duplicate letters
FilteredDictionary = []
for word in Dictionary:
    for letter in word:
        if word.count(letter) > 1:
            break
    else:
        FilteredDictionary.append(word.strip())

# 2.c - Give each word a 'score' and find highest
OrderedByMostLikely = []
for word in FilteredDictionary:
    word = word
    value = 0
    for letter in word:
        value += Breakdown[letter]
    OrderedByMostLikely.append((value, word))

OrderedByMostLikely.sort(reverse=True)

# 2.d - Find the words with the highest score
highest_score = OrderedByMostLikely[0][0]
HighScoreWords = []
for item in OrderedByMostLikely:
    if item[0] == highest_score:
        HighScoreWords.append(item[1])
    else:
        break

# 2.e - Display Findings
print("The best words to start with are:", ", ".join(HighScoreWords))
SelectedWord = random.choice(HighScoreWords)
print(f"Go with: {SelectedWord}")

# 3 - Play the game and refine
AbsentLetters = [] # Not in word
PresentLetters = []
CorrectLetters = ["", "", "", "", ""]
TriedWords = [SelectedWord]
Guessed = False
FirstRun = True

while not Guessed:
    response = FirstRun or input("Was that guess correct? (y/n): ")
    FirstRun = False
    if response == "y":
        Guessed = True
    else:
        response = input("What letters are not in the word: ")
        for letter in response:
            if letter not in AbsentLetters:
                AbsentLetters.append(letter.lower())

        # 4 - Filter dictionary based on what we know (refine)
        PossibleWords = []
        for word in Dictionary:
            for letter in word:
                if letter in AbsentLetters:
                    break
            else:
                if word.strip() not in TriedWords:
                    PossibleWords.append(word.strip())

        response = input("What letters are present: ")
        for letter in response:
            if letter not in PresentLetters:
                PresentLetters.append(letter.lower())

        for word in PossibleWords[:]: # Copy for save removal during iteration
            for letter in PresentLetters:
                if letter not in word:
                    PossibleWords.remove(word)
                    break

        response = input("What letters are in the correct position (use ? for unknown): ")
        for i in range(len(response)):
            if response[i] != "?":
                CorrectLetters[i] = response[i].lower()
                if response[i] not in PresentLetters:
                    PresentLetters.append(response[i].lower())

        for word in PossibleWords[:]:
            for i in range(len(CorrectLetters)):
                if CorrectLetters[i] != "" and CorrectLetters[i] != word[i]:
                    PossibleWords.remove(word)
                    break

        # 5. Find next best word
        for word in PossibleWords[:]:
            for letter in word:
                if word.count(letter) > 1:
                    PossibleWords.remove(word)
                    break

        OrderedByMostLikely = []
        for word in PossibleWords:
            word = word
            value = 0
            for letter in word:
                value += Breakdown[letter]
            OrderedByMostLikely.append((value, word))

        OrderedByMostLikely.sort(reverse=True)

        if len(OrderedByMostLikely) == 0: # Consider Duplicate Letters
            PossibleWords = []
            for word in Dictionary:
                for letter in word:
                    if letter in AbsentLetters:
                        break
                else:
                    if word.strip() not in TriedWords:
                        PossibleWords.append(word.strip())

            for word in PossibleWords[:]: # Copy for save removal during iteration
                for letter in PresentLetters:
                    if letter not in word:
                        PossibleWords.remove(word)
                        break

            for word in PossibleWords[:]:
                for i in range(len(CorrectLetters)):
                    if CorrectLetters[i] != "" and CorrectLetters[i] != word[i]:
                        PossibleWords.remove(word)
                        break

            OrderedByMostLikely = []
            for word in PossibleWords:
                word = word
                value = 0
                for letter in word:
                    value += Breakdown[letter]
                OrderedByMostLikely.append((value, word))

            OrderedByMostLikely.sort(reverse=True)

            highest_score = OrderedByMostLikely[0][0]
            HighScoreWords = []
            for item in OrderedByMostLikely:
                if item[0] == highest_score:
                    HighScoreWords.append(item[1])
                else:
                    break
        else:
            highest_score = OrderedByMostLikely[0][0]
            HighScoreWords = []
            for item in OrderedByMostLikely:
                if item[0] == highest_score:
                    HighScoreWords.append(item[1])
                else:
                    break

        if len(HighScoreWords) == 0:
            print("I have no possible words, sorry!")
            break

        print(f"The next best word is: {HighScoreWords[0]}")
        TriedWords.append(HighScoreWords[0])
