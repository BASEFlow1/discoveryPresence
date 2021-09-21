import argparse
from os import set_inheritable
from pypresence import Presence
from colorama import Fore
import time
import psutil
from flair import FreelancerState

def proccessActive(str):
    if str in (p.name() for p in psutil.process_iter()):
        return True
    else:
        return False

def print_event(*args):
    """Print an event to terminal with emphasis (using ANSI colour codes). How this displays exactly varies between
    terminals."""
    print('\033[1m' + ' '.join(map(str, args)) + '\033[0m')


rpc = Presence("888528830040526889")
rpc.connect()

parser = argparse.ArgumentParser(prog='flair', description='flair, a novel client-side hook for Freelancer')
parser.add_argument('freelancer_dir', help='Path to a working Freelancer install directory')

arguments = parser.parse_args()

isDocked = False

game_state = FreelancerState(arguments.freelancer_dir)
game_state.begin_polling(print_state=False)

currentSystem = game_state.system if game_state.system != None else "None"
currentChar = game_state.name if game_state.name != None else "None"
currentBase = game_state.base if game_state.base != None else "None"
isDocked = game_state.docked if game_state.docked != None else "None"
i = 0

startTime = time.time()

def yoMama(startTime):
    if proccessActive("Freelancer.exe"):
        if not isDocked:
            if str(currentChar[:5]) == "46th|":
                rpc.update(large_image="rpcImage", state = f"Playing as {currentChar}", details = f"Patrolling in {currentSystem}", start = startTime)
            elif "Lyrex" in str(currentChar):
                rpc.update(large_image="rpcImage", state = f"Playing as {currentChar}", details = f"Doing Crime in {currentSystem}", start = startTime)
            elif "Jukin.Johnson" in str(currentChar):
                rpc.update(large_image="rpcImage", state = f"Playing as {currentChar}", details = f"Probably smuggling cardamine in {currentSystem}", start = startTime)
            else:
                rpc.update(large_image="rpcImage", state = f"Playing as {currentChar}", details = f"Freelancing in {currentSystem}", start = startTime)
        else:
            rpc.update(large_image="rpcImage", state = f"Playing as {currentChar}", details = f"Docked on {currentBase}", start = startTime)
        print(f"[{Fore.GREEN}DEBUG{Fore.WHITE}] Freelancer.exe {Fore.GREEN}active{Fore.WHITE}, updating Discord Rich Presence.")
    else:
        print(f"[{Fore.RED}DEBUG{Fore.WHITE}] Freelancer.exe {Fore.RED}not active{Fore.WHITE}, clearing Discord Rich Presence.")
        rpc.clear()
        startTime = time.time()
yoMama(startTime)
while True:
    game_state.refresh()
    currentSystem = game_state.system if game_state.system != None else "None"
    currentChar = game_state.name if game_state.name != None else "None"
    currentBase = game_state.base if game_state.base != None else "None"
    isDocked = game_state.docked if game_state.docked != None else "None"
    if currentBase == None and isDocked == True:
        currentBase = "a POB"
    print(f"currentSystem: {currentSystem}\ncurrentChar: {currentChar}\ncurrentBase: {currentBase}\nisDocked: {isDocked}")
    if not proccessActive("Freelancer.exe"):
        startTime = time.time()
    # events.system_changed.connect(lambda system: yoMama())
    # events.character_changed.connect(lambda name: yoMama())
    print("Current cycle:", i)
    i += 1
    yoMama(startTime)
    time.sleep(5)


