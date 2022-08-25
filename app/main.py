from PyInquirer import prompt
from imageProcessing import captureFrame, saveFrame
from macro import goInBattle, initController

mainQuestions = [
    {
        'type': 'list',
        'name': 'main',
        'message': 'Choose the starter you want to get',
        'choices': ['Get shiny', ],
    },
]

shinyQuestions = [
    {
        'type': 'list',
        'name': 'start_choice',
        'message': 'Choose the starter you want to get',
        'choices': ['Turtwig', 'Chimchar', 'Piplup'],
    },
    {
        'type': 'list',
        'name': 'encountered_action',
        'message': 'Choose what to do when encountered',
        'choices': ['Fight and save', 'Notify me', 'Do nothing'],
    },
]


def main():
    if (prompt(mainQuestions).get("main") == "Get shiny"):
        answers = prompt(shinyQuestions)
        pokemon = answers.get("start_choice")
        action = answers.get("encountered_action")

        print("Pokemon :", pokemon)
        print("Action :", action)

        if (pokemon == 'Piplup'):
            initController()
            startRun(pokemon)
        else:
            print("Not supported")


def startRun(pokemon):
    goInBattle(['Turtwig', 'Chimchar', 'Piplup'].index(pokemon))
    # exitGame()
    # startRun(pokemon)


if __name__ == "__main__":
    _, frame = captureFrame()
    saveFrame(frame, "./.temp/frame" + str(2) + ".png")
    # main()
