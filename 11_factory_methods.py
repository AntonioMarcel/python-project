class Transport:
    TRANSPORT_TYPES = ("car", "boat", "plane")

    def __init__(self, transport_type, cargo_space, avg_cost, max_speed):
        self.transport_type = transport_type
        self.cargo_space = cargo_space
        self.avg_cost = avg_cost
        self.max_speed = max_speed

    @classmethod
    def create_car(cls, cargo_space, avg_cost, max_speed):
        return cls(cls.TRANSPORT_TYPES[0], cargo_space, avg_cost, max_speed)

    @classmethod
    def create_boat(cls, cargo_space, avg_cost, max_speed):
        return cls(cls.TRANSPORT_TYPES[1], cargo_space, avg_cost, max_speed)

    def __repr__(self):
        return f"<Transport({self.transport_type}, {self.cargo_space}, {self.avg_cost}, {self.max_speed})>"


car = Transport.create_car(200, 400, 300)
boat = Transport.create_boat(200, 400, 300)
print(car)
print(boat)
