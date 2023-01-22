def log(msg):
    print(msg)
class Elevator:
    MAX_FLOOR = 15

    def __init__(self):
        self.current_floor = 0
        self.direction = "UP"
        self.is_stop = True
        self.internal_req = []
        self.external_req = []  # tuple (floor , destination)


    def add_internal_req(self, floor):
        if floor not in self.internal_req:
            self.internal_req.append(floor)

    def add_external_req(self, floor, destination):
        self.external_req.append((floor, destination))

    def max_up(self):
        return max(self.internal_req + [x[0] for x in self.external_req])

    def max_down(self):
        return min(self.internal_req + [x[0] for x in self.external_req])

    def do(self):
        if self.internal_req == [] and self.external_req == []:
            self.is_stop = True
            log("No request")
            return
        else:
            self.is_stop = False

        if self.current_floor in self.internal_req:
            log(f"Stop at {self.current_floor}")
            self.internal_req.remove(self.current_floor)
            self.is_stop = True
            if self.current_floor in [x[0] for x in self.external_req]:
                log(f"Stop at {self.current_floor} for external request")
                reqs = [x for x in self.external_req if x[0] == self.current_floor]
                for req in reqs:
                    self.internal_req.append(req[1])
                    self.external_req.remove(req)
            return

        if self.current_floor in [x[0] for x in self.external_req]:
            log(f"Stop at {self.current_floor} for external request")
            reqs = [x for x in self.external_req if x[0] == self.current_floor]
            for req in reqs:
                self.internal_req.append(req[1])
                self.external_req.remove(req)
            self.is_stop = True
            return

        if self.direction == "UP":
            if self.current_floor < self.max_up():
                self.current_floor += 1
                log(f"Move to {self.current_floor}")
            else:
                self.direction = "DOWN"
                log("Change direction to DOWN")
        if self.direction == "DOWN":
            if self.current_floor > self.max_down():
                self.current_floor -= 1
                log(f"Move to {self.current_floor}")
            else:
                self.direction = "UP"
                log("Change direction to UP")