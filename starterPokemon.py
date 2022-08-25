def debug(message):
    print(message)


def goInBattle():
    debug('A - Select Game')
    nx.press_buttons(controller_index, [nxbt.Buttons.A])
    sleep(1.5)
    debug('A - Select Profile')
    nx.press_buttons(controller_index, [nxbt.Buttons.A])
    sleep(23)
    debug('A - Skip cinematic')
    nx.press_buttons(controller_index, [nxbt.Buttons.A])
    sleep(4)
    debug('A - Start save')
    nx.press_buttons(controller_index, [nxbt.Buttons.A])
    sleep(13)
    debug('UP - Move to starter zone')
    nx.press_buttons(controller_index, [nxbt.Buttons.DPAD_UP])
    sleep(1.5)
    debug('A - Skip dialog')
    nx.press_buttons(controller_index, [nxbt.Buttons.A])
    sleep(4)
    debug('A - Skip dialog UNTIL pokemon selection')
    spamDialog(71)

    sleep(2)
    debug('B - Make sure that we are in pokeball selection and not in a menu')
    nx.press_buttons(controller_index, [nxbt.Buttons.B])
    sleep(2)

    debug('RIGHT - Select pokeball')
    nx.press_buttons(controller_index, [nxbt.Buttons.DPAD_RIGHT])
    sleep(0.5)
    debug('RIGHT - Select pokeball')
    nx.press_buttons(controller_index, [nxbt.Buttons.DPAD_RIGHT])
    sleep(0.5)
    debug('RIGHT - Select pokemon')
    nx.press_buttons(controller_index, [nxbt.Buttons.A])
    sleep(1.5)
    debug('RIGHT - Menu selection')
    nx.press_buttons(controller_index, [nxbt.Buttons.DPAD_UP])
    sleep(0.5)
    debug('RIGHT - Confirm')
    nx.press_buttons(controller_index, [nxbt.Buttons.A])
    sleep(13)
    debug('RIGHT - Start detection')
    sleep(8)


def piplupRun():
    goInBattle()
    brightnessNormal = config.get("PIPLUP", "Normal")
    brightnessShiny = config.get("PIPLUP", "Shiny")

    normal = cv2.imread("/home/lv0/shiny/images/Piplup_Normal_Gray.png")
    height = int(normal.shape[0]/2)-10
    width = int(normal.shape[1]/2)-5

    isShiny = compareImageToValue(normal, brightnessShiny, height, width)
    isNormal = compareImageToValue(normal, brightnessNormal, height, width)

    print("Shiny :", isShiny)
    print("Normal :", isNormal)
    print("Other :", not (isNormal or isShiny))
    if (isNormal):
        exitGame()
        piplupRun()
