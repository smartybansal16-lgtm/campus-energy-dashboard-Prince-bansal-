class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh

class Building:
    def __init__(self, name):
        self.name = name
        self.readings = []

    def add_reading(self, reading: MeterReading):
        self.readings.append(reading)

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.readings)

    def generate_report(self):
        total = self.calculate_total_consumption()
        return f"{self.name}: Total Consumption = {total} kWh"

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def add_record(self, building, timestamp, kwh):
        if building not in self.buildings:
            self.buildings[building] = Building(building)
        self.buildings[building].add_reading(MeterReading(timestamp, kwh))

    def generate_all_reports(self):
        return [b.generate_report() for b in self.buildings.values()]
