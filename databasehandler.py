from google.cloud import datastore

datastore_client = datastore.Client()

class databasehandler:
    def get_all_vehicles(self):
        query = datastore_client.query(kind='electric_vehicle')
        vehicles = query.fetch()
        return vehicles

    def get_single_vehicle_object(vehicle_id):
        key = datastore_client.key('electric_vehicle', vehicle_id)

        return datastore_client.get(key)

    def update_vehicle_information(self, vehicle_name, vehicle_manufacture, vehicle_year, vehicle_battery_size,
                                   vehicle_wltp_range, vehicle_cost, vehicle_power):
        entity = datastore.Entity(key=datastore_client.key('electric_vehicle', self))

        entity.update({
            'name': vehicle_name,
            'manufacturer': vehicle_manufacture,
            'year': vehicle_year,
            'battery_size': vehicle_battery_size,
            'WLTP_range': vehicle_wltp_range,
            'cost': vehicle_cost,
            'power': vehicle_power
        })
        datastore_client.put(entity)
