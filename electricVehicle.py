class electricVehicle:
    vehicle_name: str = ""
    vehicle_manufacturer: str = ""
    vehicle_year = ""
    vehicle_battery_size = ""
    vehicle_wltp_range = ""
    vehicle_cost = ""
    vehicle_power = ""

    def __init__(self, vehicle_name, vehicle_manufacturer, vehicle_year,
                 vehicle_battery_size, vehicle_wltp_range, vehicle_cost, vehicle_power):

        self.vehicle_name = vehicle_name
        self.vehicle_manufacturer = vehicle_manufacturer
        self.vehicle_year = vehicle_year
        self.vehicle_battery_size = vehicle_battery_size
        self.vehicle_wltp_range = vehicle_wltp_range
        self.vehicle_cost = vehicle_cost
        self.vehicle_power = vehicle_power
