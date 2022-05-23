import google.oauth2.id_token
from flask import Flask, render_template, request
from google.auth.transport import requests
from google.cloud import datastore
from databasehandler import databasehandler
from Helper import Helper
from electricVehicle import electricVehicle

app = Flask(__name__)
datastore_client = datastore.Client()
firebase_request_adapter = requests.Request()
data_base_handler = databasehandler()
vehicle_helper = Helper()


def create_new_electricVehicle_to_database(electVehicle):
    ev_entity_key = electVehicle.vehicle_name + electVehicle.vehicle_manufacturer + str(electVehicle.vehicle_year)

    entity = datastore.Entity(key=datastore_client.key('electric_vehicle', ev_entity_key))

    query_to_check = datastore_client.query(kind='electric_vehicle')
    query_to_check.add_filter("name", "=", electVehicle.vehicle_name)
    query_to_check.add_filter("manufacturer", "=", electVehicle.vehicle_manufacturer)
    query_to_check.add_filter("year", "=", electVehicle.vehicle_year)

    if len(list(query_to_check.fetch())) <= 0:
        entity.update({
            'name': electVehicle.vehicle_name,
            'manufacturer': electVehicle.vehicle_manufacturer,
            'year': electVehicle.vehicle_year,
            'battery_size': electVehicle.vehicle_battery_size,
            'WLTP_range': electVehicle.vehicle_wltp_range,
            'cost': electVehicle.vehicle_cost,
            'power': electVehicle.vehicle_power
        })
        datastore_client.put(entity)


def store_time(email):
    entity = datastore.Entity(key=datastore_client.key('User', email, 'visit'))
    entity.update({'email': email})
    datastore_client.put(entity)


@app.route('/')
def root():
    id_token = request.cookies.get("token")
    error_message = None
    claims = None
    if id_token:
        try:
            claims = google.oauth2.id_token.verify_firebase_token(id_token, firebase_request_adapter)
            store_time(claims['email'])

        except ValueError as exc:
            error_message = str(exc)
    return render_template('index.html', user_data=claims, error_message=error_message)


@app.route('/get_vehicle_page', methods=["get"])
def get_vehicle_page():
    return render_template('add_new_vehicle.html')


@app.route('/add_new_vehicle_to_the_database', methods=["post"])
def add_new_vehicle_to_the_database():
    vehicle_name = request.form['vehicle_name']
    vehicle_manufacturer = request.form['vehicle_manufacturer']
    vehicle_year = request.form['vehicle_year']
    vehicle_battery_size = request.form['vehicle_battery_size']
    vehicle_wltp_range = request.form['vehicle_wltp_range']
    vehicle_cost = request.form['vehicle_cost']
    vehicle_power = request.form['vehicle_power']
    ev = electricVehicle(vehicle_name, vehicle_manufacturer, vehicle_year, vehicle_battery_size,
                         vehicle_wltp_range, vehicle_cost, vehicle_power)
    create_new_electricVehicle_to_database(ev)
    return render_template('index.html')


@app.route('/view_All_Vehicle', methods=["get"])
def view_all_Vehicle():
    vehicle_entities = data_base_handler.get_all_vehicles()

    return render_template('view_all_vehicle.html', vehicle_entities=vehicle_entities)


@app.route('/get_vehicle_information/<string:id>', methods=["get"])
def get_vehicle_information(id):
    entity = databasehandler.get_single_vehicle_object(id)

    return render_template('show_information_vehicle.html', vehicle_object=entity)


@app.route('/update_vehicle_information/<string:id>', methods=["post"])
def update_vehicle_information(id):
    vehicle_name = request.form['vehicle_name']
    vehicle_manufacture = request.form['vehicle_manufacture']
    vehicle_year = request.form['vehicle_year']
    vehicle_battery_size = request.form['vehicle_battery_size']
    vehicle_wltp_range = request.form['vehicle_wltp_range']
    vehicle_cost = request.form['vehicle_cost']
    vehicle_power = request.form['vehicle_power']

    databasehandler.update_vehicle_information(id, vehicle_name, vehicle_manufacture, vehicle_year,
                                               vehicle_battery_size, vehicle_wltp_range, vehicle_cost,
                                               vehicle_power)

    entity = databasehandler.get_single_vehicle_object(id)

    return render_template('show_information_vehicle.html', vehicle_object=entity)


@app.route('/delete_vehicle_information/<string:id>', methods=["get"])
def delete_vehicle_information(id):
    electric_vehicle = datastore_client.key('electric_vehicle', id)
    datastore_client.delete(electric_vehicle)
    vehicle_entities = data_base_handler.get_all_vehicles()

    return render_template('view_all_vehicle.html', vehicle_entities=vehicle_entities)


@app.route('/compare_more_than_one_element', methods=["post"])
def compare_more_than_one_element():
    comparing_vehicles_id = request.form.getlist('comparing_vehicles_checkboxes')
    vehicles_multi_keys = []
    for i in range(len(comparing_vehicles_id)):
        vehicles_multi_keys.append(datastore_client.key('electric_vehicle', comparing_vehicles_id[i]))
    vehicle_comparing_list = datastore_client.get_multi(vehicles_multi_keys)

    vehicle_attributes_comparisons = vehicle_helper. \
        get_vehicle_compare_attributes_comparison(vehicle_comparing_list)

    return render_template('comparing_vehicle_page.html',
                           vehicle_entities=vehicle_comparing_list,
                           vehicle_attributes_comparisons=vehicle_attributes_comparisons)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
