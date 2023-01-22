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
def nearest_elevator(elv1,elv2,elv3, floor):
    return min([elv1,elv2,elv3], key=lambda x: x.arrival_time(floor))

elevator1 = Elevator(1)
elevator2 = Elevator(2)
elevator3 = Elevator(3)

extr_req = (3, 5)

elevator1.current_floor = 10
elevator1.add_internal_req(2)
elevator1.add_external_req(3, 5)
elevator1.add_external_req(6, 5)
elevator1.direction = "UP"
print(elevator1.arrival_time(5))

# while True:
#     get_input(elvator)
#     elvator.do()
#     sleep(1)