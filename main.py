from time import sleep
from elevator import Elevator
def get_input(elv):
    inp = input("Enter floor and destination: ")
    if inp == '' :
        return
    inp = inp.split()
    if len(inp) == 1:
        elv.add_internal_req(int(inp[0]))
    elif len(inp) == 2:
        elv.add_external_req(int(inp[0]), int(inp[1]))


elvator = Elevator()
while True:
    get_input(elvator)
    elvator.do()
    sleep(1)