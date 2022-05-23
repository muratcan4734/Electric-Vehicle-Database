from Vehicle_Compare_attribute import VehicleCompareAttribute


class Helper:
    def __init__(self):
        pass

    def find_maximum_value(self, list):
        max = list[0]

        for i in list:
            if i > max:
                max = i
        return str(max)

    def find_minimum_value(self, list):
        min = list[0]

        for i in list:
            if i < min:
                min = i
        return str(min)

    def get_given_argument_list(self, vehicle_string_attribute, vehicles):
        list = []
        for i in vehicles:
            string_cast = i[vehicle_string_attribute]
            string_cast = int(string_cast)
            list.append(string_cast)

        return list

    def get_vehicle_compare_attributes_comparison(self, vehicles):

        #  for cost
        list = self.get_given_argument_list("cost", vehicles)

        cost_max = self.find_maximum_value(list)
        cost_min = self.find_minimum_value(list)

        list = self.get_given_argument_list("battery_size", vehicles)
        battery_size_max = self.find_maximum_value(list)
        battery_size_min = self.find_minimum_value(list)

        list = self.get_given_argument_list("year", vehicles)
        year_max = self.find_maximum_value(list)
        year_min = self.find_minimum_value(list)

        list = self.get_given_argument_list("WLTP_range", vehicles)
        WLTP_range_max = self.find_maximum_value(list)
        WLTP_range_min = self.find_minimum_value(list)

        list = self.get_given_argument_list("power", vehicles)
        power_max = self.find_maximum_value(list)
        power_min = self.find_minimum_value(list)

        return VehicleCompareAttribute(cost_max,
                                       cost_min,
                                       power_max,
                                       power_min,
                                       battery_size_max,
                                       battery_size_min,
                                       WLTP_range_max,
                                       WLTP_range_min,
                                       year_max,
                                       year_min)
