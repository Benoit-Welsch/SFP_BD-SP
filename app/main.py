from PyInquirer import prompt
from macro import exitGame, goToHome, screenRecord, cleanController
from imageProcessing import isShiny
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
        initController()
        startRun(pokemon)


def startRun(pokemon):
    goInBattle(['Turtwig', 'Chimchar', 'Piplup'].index(pokemon))
    if (not isShiny()):
        exitGame()
        startRun(pokemon)
    else:
        screenRecord()
        goToHome()
        cleanController()


if __name__ == "__main__":
    main()
