class VehicleCompareAttribute:

    battery_max = 0
    battery_min = 0
    wltp_max = 0
    wltp_min = 0
    year_max = 0
    year_min = 0
    cost_max = 0
    cost_min = 0
    power_max = 0
    power_min = 0

    def __init__(self, cost_max,
                 cost_min,
                 power_max,
                 power_min,
                 battery_max,
                 battery_min,
                 wltp_max,
                 wltp_min,
                 year_max,
                 year_min):
        self.cost_max = cost_max
        self.cost_min = cost_min
        self.power_max = power_max
        self.power_min = power_min
        self.battery_max = battery_max
        self.battery_min = battery_min
        self.wltp_max = wltp_max
        self.wltp_min = wltp_min
        self.year_max = year_max
        self.year_min = year_min
