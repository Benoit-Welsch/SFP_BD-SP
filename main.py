from time import sleep
import nxbt

nx = nxbt.Nxbt()

def debug(message):
    print(message)

def init():
    global controller_index
    controller_index = nx.create_controller(nxbt.PRO_CONTROLLER, reconnect_address=nx.get_switch_addresses())
    nx.wait_for_connection(controller_index)
    print("Connected")
    input("Press ENTER when you are on the game tiles !")
    print("3  ...")
    sleep(1)
    print("2  ...")
    sleep(1)
    print("1  ...")
    sleep(1)
    print("GO !!!")

def exit():
    nx.remove_controller(controller_index)
    print("Disconnected")

def spamDialog(loop):
    debug('Spamming')
    for _ in range(loop):
        nx.press_buttons(controller_index, [nxbt.Buttons.A])
        sleep(0.5)

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

    debug('RIGHT - Seclect pokeball')
    nx.press_buttons(controller_index, [nxbt.Buttons.DPAD_RIGHT])
    sleep(0.5)
    debug('RIGHT - Seclect pokeball')
    nx.press_buttons(controller_index, [nxbt.Buttons.DPAD_RIGHT])
    sleep(0.5)
    debug('RIGHT - Seclect pokemon')
    nx.press_buttons(controller_index, [nxbt.Buttons.A])
    sleep(1.5)
    debug('RIGHT - Menu selection')
    nx.press_buttons(controller_index, [nxbt.Buttons.DPAD_UP])
    sleep(0.5)
    debug('RIGHT - Confirm')
    nx.press_buttons(controller_index, [nxbt.Buttons.A])
    sleep(13)
    debug('RIGHT - Start detection')


init()
goInBattle()
exit()

