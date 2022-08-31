from datetime import datetime
from PyInquirer import prompt
from VideoCamera import VideoGet
from config import loadConfig
from helper import debug
from macro import exitGame, goToHome, screenRecord, cleanController
from imageProcessing import createTileView, isShiny, loadModel
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
    config = loadConfig()
    cam = VideoGet(config['cam']['path'])
    cam.start()

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

        loadModel()
        initController()
        startRun(cam, pokemon)

        if (notify):
            if (notificationType.get("type_notification") == "Discord"):
                notification.discord()


def startRun(cam: VideoGet, pokemon):
    shiny = False
    runNumber = 0
    while (not shiny):
        runNumber += 1
        print("Run :", str(runNumber))
        goInBattle(['Turtwig', 'Chimchar', 'Piplup'].index(pokemon))

        frames = cam.captureFrame(60)

        date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        debug('TILES - Creation of unified view')
        createTileView(frames, 6).save("./.temp/frames_" + date_time + ".png")

        debug('KERAS - Start detection')
        shiny, _ = isShiny(frames)

        if (not shiny):
            exitGame()

    screenRecord()
    goToHome()
    cleanController()


if __name__ == "__main__":
    main()
