from PyInquirer import prompt
from config import loadConfig
from macro import exitGame, goToHome, screenRecord, cleanController
from imageProcessing import isShiny
from macro import goInBattle, initController
import notification

mainQuestions = [
    {
        'type': 'list',
        'name': 'main',
        'message': 'What do you want to do',
        'choices': ['Get shiny'],
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
        'name': 'action_choice',
        'message': 'Action to perform on detection',
        'choices': ['Sleep', 'Sleep + Notification'],
    }
]

notificationQuestions = [
    {
        'type': 'list',
        'name': 'type_notification',
        'message': 'Action to perform on detection',
        'choices': ['Discord'],
    }
]


def main():
    loadConfig()
    q1 = prompt(mainQuestions)

    if (q1.get("main") == "Get shiny"):
        notify = False

        answers = prompt(shinyQuestions)
        pokemon = answers.get("start_choice")
        action = answers.get("action_choice")

        if (action == "Sleep + Notification"):
            notify = True
            notificationType = prompt(notificationQuestions)

        print("Pokemon :", pokemon)
        print("Action : ", action)
        initController()
        startRun(pokemon)
        if (notify):
            if (notificationType.get("type_notification") == "Discord"):
                notification.discord()


def startRun(pokemon):
    shiny = False
    runNumber = 0
    while (not shiny):
        runNumber += 1
        print("Run :", str(runNumber))
        goInBattle(['Turtwig', 'Chimchar', 'Piplup'].index(pokemon))
        shiny = isShiny()
        if(not shiny):
            exitGame()
       
    screenRecord()
    goToHome()
    cleanController()


if __name__ == "__main__":
    main()
