import random, os, pygame

pygame.init()

base_folder = os.path.dirname(__file__)
os.environ['SDL_VIDEO_CENTERED'] = '1'

Dictionary_Location = os.path.join(base_folder, "resources\\Dictionary.txt")
with open(Dictionary_Location, "r") as file:
    Dictionary = file.readlines()

word = ""
while not len(word) == 6:
    word = Dictionary[random.randint(0, len(Dictionary)-1)]
word = "arena"

Display = pygame.display.set_mode((370, 670))
clock = pygame.time.Clock()

WordleTitleFontPath = os.path.join(base_folder, "resources", "Adamina", "Adamina-Regular.ttf")
WordleTitleFont = pygame.font.Font(WordleTitleFontPath, 60)
WordleTitleFont.set_bold(True)
WordleTitle = WordleTitleFont.render("Wordle", True, (0, 0, 0))

GuessFontPath = os.path.join(base_folder, "resources", "Noto_Sans", "static", "NotoSans-Regular.ttf")
GuessFont = pygame.font.Font(GuessFontPath, 45)

Guess = []
for i in range(6):
    SubGuess = []
    for j in range(5):
        SubGuess.append("")
    Guess.append(SubGuess)

Font_X_Position = 0
Padding = 10
X, Y = 0, 0

pygame.display.set_caption("Wordle")
while True:
    Display.fill([255, 255, 255])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            try:
                #print(pygame.key.name(event.key))
                if event.key == pygame.K_RETURN and X == 5:
                    pygame.display.set_caption("Wordle | Seaching dictionary")
                    with open(Dictionary_Location, "r") as file:
                        Dictionary = file.readlines()

                    string = ""
                    for i in range(len(Guess[Y])):
                        string += Guess[Y][i]

                    string += "\n"

                    for j in range(len(Dictionary)):
                        if string.lower() == Dictionary[j].lower():
                            Y += 1
                            X = 0
                            break

                    pygame.display.set_caption("Wordle")
                elif event.key == pygame.K_BACKSPACE and X > 0:
                    X -= 1
                    Guess[Y][X] = ""
                elif chr(event.key).lower() >= "a" and chr(event.key).lower() <= "z" and X < 5:
                    Guess[Y][X] = chr(event.key).upper()
                    X += 1
            except Exception as Message:
                pass
    Ypos = 100
    for j in range(len(Guess)):
        Correct = 0
        for i in range(len(Guess[j])):
            if not Guess[j][i] == "":
                if j < Y:
                    if Guess[j][i].lower() in word.lower():
                        if Guess[j][i].lower() == word[i].lower():
                            col = (106, 170, 100)
                            Correct += 1
                        else:
                            col = (201, 180, 88)
                    else:
                        col = (120, 124, 126)
                else:
                    col = (120, 124, 126)
                Xpos = (400/5)*i
                Rect = pygame.Rect(Xpos, Ypos, 50, 50)
                pygame.draw.rect(Display, col, Rect)
                RenderedGuess = GuessFont.render(Guess[j][i], True, (255, 255, 255))
                x = RenderedGuess.get_width()
                Display.blit(RenderedGuess, ((Rect.centerx-(x/2)), Ypos-7))
            else:
                Xpos = (400/5)*i
                Rect = pygame.Rect(Xpos, Ypos, 50, 50)
                pygame.draw.rect(Display, (120, 124, 126), Rect, 2)
        if Correct == 5:
            Rect = pygame.Rect(0, 285, 370, 100)
            pygame.draw.rect(Display, (106, 170, 100), Rect)

            Rect = pygame.Rect(10, 295, 350, 80)
            pygame.draw.rect(Display, (255, 255, 255), Rect)

            RenderedGuess = GuessFont.render("Congratulations!", True, (0, 0, 0))
            x = RenderedGuess.get_width()
            Display.blit(RenderedGuess, ((Rect.centerx-(x/2)), 310))
            pygame.display.update()
            quit()

        Ypos += 55

    if Y > 5:
        Rect = pygame.Rect(0, 285, 370, 100)
        pygame.draw.rect(Display, (255, 0, 0), Rect)

        Rect = pygame.Rect(10, 295, 350, 80)
        pygame.draw.rect(Display, (255, 255, 255), Rect)

        RenderedGuess = GuessFont.render("Nope!", True, (0, 0, 0))
        x = RenderedGuess.get_width()
        Display.blit(RenderedGuess, ((Rect.centerx-(x/2)), 310))

    Display.blit(WordleTitle, ((370-WordleTitle.get_width())/2, 0))
    pygame.display.flip()
    clock.tick(30)
