#type: ignore

import random, os, pmma

base_folder = os.path.dirname(__file__)

Dictionary_Location = os.path.join(base_folder, "resources\\Dictionary.txt")
with open(Dictionary_Location, "r") as file:
    Dictionary = file.readlines()

word = ""
while not len(word) == 6:
    word = Dictionary[random.randint(0, len(Dictionary)-1)]

Display = pmma.Display()
Display.create([370, 670], caption="Wordle")
Display.window_fill_color.set_color_name(pmma.Constants.Colors.WHITE)

WordleTitleFontPath = os.path.join(base_folder, "resources", "Adamina", "Adamina-Regular.ttf")
WordleTitle = pmma.TextRenderer()
WordleTitle.set_font(WordleTitleFontPath)
WordleTitle.set_text("Wordle")
WordleTitle.set_size(60)
WordleTitle.foreground_color.set_color_name(pmma.Constants.Colors.BLACK)
WordleTitle.position.set_coord(80, 60)

GuessFontPath = os.path.join(base_folder, "resources", "Noto_Sans", "static", "NotoSans-Regular.ttf")

ResultFont = pmma.TextRenderer()
ResultFont.set_font(WordleTitleFontPath)
ResultFont.set_size(45)
ResultFont.foreground_color.set_color_name(pmma.Constants.Colors.BLACK)

Guess = []
LetterFont = []
for i in range(6):
    SubGuess = []
    SubLetters = []
    for j in range(5):
        SubGuess.append("")

        Letter = pmma.TextRenderer()
        Letter.set_font(GuessFontPath)
        Letter.set_size(45)
        Letter.foreground_color.set_color_name(pmma.Constants.Colors.RED)
        SubLetters.append(Letter)

    LetterFont.append(SubLetters)
    Guess.append(SubGuess)

Font_X_Position = 0
Padding = 10
X, Y = 0, 0

EnterKeyPressed = pmma.KeyEvents.Enter()
BackspaceKeyPressed = pmma.KeyEvents.Backspace()
TextEvent = pmma.WindowEvents.TextInput()

WordleSquare = pmma.Shapes2D.Rectangle()
WordleSquare.set_size([50, 50])

while pmma.General.is_application_running():
    Display.clear()

    try:
        if EnterKeyPressed.get_pressed_toggle() and X == 5:
            Display.set_caption("Wordle | Seaching dictionary")
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

            Display.set_caption("Wordle")
        elif BackspaceKeyPressed.get_pressed_toggle() and X > 0:
            X -= 1
            Guess[Y][X] = ""
        elif TextEvent.get_text() != "" and X < 5:
            Guess[Y][X] = TextEvent.get_text().upper()
            X += 1
            TextEvent.clear_text()
    except Exception as Message:
        print(Message)
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

                WordleSquare.shape_center.set_coord(Xpos + 25, Ypos)
                WordleSquare.shape_color.set_RGB_array(col)
                WordleSquare.set_width(0)
                WordleSquare.render()

                LetterFont[j][i].set_text(Guess[j][i])
                LetterFont[j][i].position.set_coord(Xpos, Ypos-7)
                LetterFont[j][i].render()
            else:
                Xpos = (400/5)*i

                WordleSquare.shape_center.set_coord(Xpos + 25, Ypos)
                WordleSquare.shape_color.set_RGB(120, 124, 126)
                WordleSquare.set_width(2)
                WordleSquare.render()

        if Correct == 5:
            OutlineRect = pmma.Shapes2D.Rectangle()
            OutlineRect.set_size([370, 100])
            OutlineRect.shape_center.set_coord(0, 285)
            OutlineRect.shape_color.set_RGB(106, 170, 100)
            OutlineRect.render()

            FillRect = pmma.Shapes2D.Rectangle()
            FillRect.set_size([350, 80])
            FillRect.shape_center.set_coord(10, 295)
            FillRect.shape_color.set_color_name(pmma.Constants.Colors.WHITE)
            FillRect.render()

            ResultFont.set_text("Congratulations!")
            ResultFont.position.set_coord(10, 310)
            ResultFont.render()

        Ypos += 55

    if Y > 5:
        OutlineRect = pmma.Shapes2D.Rectangle()
        OutlineRect.set_size([370, 100])
        OutlineRect.shape_center.set_coord(0, 285)
        OutlineRect.shape_color.set_color_name(pmma.Constants.Colors.RED)
        OutlineRect.render()

        FillRect = pmma.Shapes2D.Rectangle()
        FillRect.set_size([350, 80])
        FillRect.shape_center.set_coord(10, 295)
        FillRect.shape_color.set_color_name(pmma.Constants.Colors.WHITE)
        FillRect.render()

        ResultFont.set_text("Nope!")
        ResultFont.position.set_coord(10, 310)
        ResultFont.render()

    WordleTitle.render()

    Display.refresh()