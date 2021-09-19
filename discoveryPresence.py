#import argparse
from pypresence import Presence
from colorama import Fore
import time
import psutil
# from flair import events, hook as flair
# from flair import FreelancerState

def proccessActive(str):
    if str in (p.name() for p in psutil.process_iter()):
        return True
    else:
        return False

# def print_event(*args):
#     """Print an event to terminal with emphasis (using ANSI colour codes). How this displays exactly varies between
#     terminals."""
#     print('\033[1m' + ' '.join(map(str, args)) + '\033[0m')

rpc = Presence("888528830040526889")
rpc.connect()

while True:
    if proccessActive("Freelancer.exe"):
        print(f"[{Fore.GREEN}DEBUG{Fore.WHITE}] Freelancer.exe {Fore.GREEN}active{Fore.WHITE}, updating Discord Rich Presence.")
        rpc.update(large_image="rpcImage")
    else:
        print(f"[{Fore.RED}DEBUG{Fore.WHITE}] Freelancer.exe {Fore.RED}not active{Fore.WHITE}, clearing Discord Rich Presence.")
        rpc.clear()

    time.sleep(5)
    #     # parse command line arguments
    # parser = argparse.ArgumentParser(prog='flair', description='flair, a novel client-side hook for Freelancer')
    # parser.add_argument('freelancer_dir', help='Path to a working Freelancer install directory')



    # events.system_changed.connect(lambda system: print_event('System entered:', system))
    # events.character_changed.connect(lambda name: print_event('Character loaded:', name))

    # arguments = parser.parse_args()

    # game_state = FreelancerState(arguments.freelancer_dir)
    # game_state.begin_polling(print_state=False)


