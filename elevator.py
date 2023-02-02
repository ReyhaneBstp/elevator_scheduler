from request import Request
class Elevator:
    MAX_FLOOR = 15

    def __init__(self, num: str):
        self.current_floor = 0
        self.direction = "UP"
        self.is_stop = True
        self.internal_req = []  # tuple (floor , age)
        self.external_req = []  # tuple (floor , destination, age)
        self.num = num

    def log(self, msg):
        print("elevator " + str(self.num) + ": " + msg)
        # (msg)

    def internal_req_list(self):
        return [x.floor for x in self.internal_req]

    def external_req_list(self):
        return [(x.floor,x.dest) for x in self.external_req]

    def add_internal_req(self, floor):
        if floor not in self.internal_req_list():
            self.internal_req.append(Request(floor))

    def add_external_req(self, floor, destination):
        self.external_req.append(Request(floor, destination))

    def max_up(self):
        l = self.internal_req + self.external_req
        if l == []:
            return self.current_floor
        return max(l,key=lambda x : x.floor).floor

    def max_down(self):
        l = self.internal_req + self.external_req
        if l == []:
            return self.current_floor
        return min(l,key=lambda x : x.floor).floor

    def move(self):
        if self.internal_req == [] and self.external_req == []:
            self.is_stop = True
            self.log("No request")
            return
        else:
            self.is_stop = False

        if self.current_floor in self.internal_req_list():
            self.log(f"Stop at {self.current_floor}")
            self.internal_req = [x for x in self.internal_req if x.floor != self.current_floor]
            self.is_stop = True
            if self.current_floor in [x.floor for x in self.external_req]:
                self.log(f"Stop at {self.current_floor} for external request")
                reqs = [x for x in self.external_req if x.floor == self.current_floor]
                for req in reqs:
                    self.internal_req.append(Request(req.dest))
                self.add_external_req = [x for x in self.external_req if x.floor != self.current_floor]
            return

        if self.current_floor in [x.floor for x in self.external_req]:
            self.log(f"Stop at {self.current_floor} for external request")
            reqs = [x for x in self.external_req if x.floor == self.current_floor]
            for req in reqs:
                self.internal_req.append(Request(req.dest))
            self.is_stop = True
            self.external_req = [x for x in self.external_req if x.floor != self.current_floor]
            return

        if self.direction == "UP":
            if self.current_floor < self.max_up():
                self.current_floor += 1
                self.log(f"Move to {self.current_floor}")
            else:
                self.direction = "DOWN"
                self.log("Change direction to DOWN")
        if self.direction == "DOWN":
            if self.current_floor > self.max_down():
                self.current_floor -= 1
                self.log(f"Move to {self.current_floor}")
            else:
                self.direction = "UP"
                self.log("Change direction to UP")

    def arrival_time(self, floor: int):
        if self.current_floor < floor and self.direction == "UP":
            t = floor - self.current_floor
            for i in self.internal_req_list():
                if i > self.current_floor and i < floor:
                    t += 1
            for i in self.external_req_list():
                if i[0] > self.current_floor and i[0] < floor:
                    t += 1
            return t
        elif self.current_floor > floor and self.direction == "DOWN":
            t = self.current_floor - floor
            for i in self.internal_req_list():
                if i < self.current_floor and i > floor:
                    t += 1
            for i in self.external_req_list():
                if i[0] < self.current_floor and i[0] > floor:
                    t += 1
            return t
        elif self.current_floor < floor and self.direction == "DOWN":
            t = self.current_floor - self.max_down() + floor - self.max_down()
            for i in self.internal_req_list():
                if i < floor:
                    t += 1
            for i in self.external_req_list():
                if i[0] < floor:
                    t += 1
            return t
        elif self.current_floor > floor and self.direction == "UP":
            t = self.max_up() - self.current_floor + self.max_up() - floor
            for i in self.internal_req_list():
                if i > floor:
                    t += 1
            for i in self.external_req_list():
                if i[0] > floor:
                    t += 1
            return t
        else:
            return 0
    def update_age(self):
        for i in self.internal_req:
            i.age += 1
        for i in self.external_req:
            i.age += 1
    def nearest_elevator(elv1, elv2, elv3, floor):
        return min([elv1, elv2, elv3], key=lambda x: x.arrival_time(floor))
