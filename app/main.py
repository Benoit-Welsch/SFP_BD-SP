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
    }
]

runNumber = 0


def main():
    if (prompt(mainQuestions).get("main") == "Get shiny"):
        answers = prompt(shinyQuestions)
        pokemon = answers.get("start_choice")

        print("Pokemon :", pokemon)
        initController()
        startRun(pokemon)


def startRun(pokemon):
    goInBattle(['Turtwig', 'Chimchar', 'Piplup'].index(pokemon))
    if (not isShiny()):
        runNumber += 1
        exitGame()
        print("Run :", str(runNumber))
        startRun(pokemon)
    else:
        screenRecord()
        goToHome()
        cleanController()


if __name__ == "__main__":
    main()
