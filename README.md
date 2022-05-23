# Electric-Vehicle-Database
Python

DATABASEHANDLER.PY
	So, For the datastore handling, I created a class I created this class named Database handler. This class initially initialise a datastore and datastore client variable and after that there is three main functions which are following.

def get_all_vehicle(self):  
	This is the method to retrieve all the vehicles from the datastore. This method contains no parameters.
	
 
def get_single_vehicle_object():  
	This is the method to retrieve a single object of vehicles from the datastore. This method contains one parameters and it returns the single object of vehicle.
 
def update_vehicle_information(): 
	This method is used to update the information of the given vehicle key. Along with the key we pass the updated values of the that vehicles through parameters.



ELECTRICVEHICLE.PY

I created an electric vehicle class. This class has a parameterized constructor. And this class is just used to create an object of Electric Vehicle. It only contains one init method which I have defined in the following.

def __init__(self, …): 
  This method is called the constructor and is called when an object is created. The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided with electric vehicle attributes .




HELPER.PY

	This class is just helper class for this application which is used to find the average, min, max and colours of the attributes which contains the minimum and maximum values. I will define about those method one by one now.
	
def find_max_value():
	It takes one parameter and which is of list and from the list it finds the maximum value and returns that.

def find_min_value():
	It takes one parameter and which is of list and from the list it finds the minimum value and returns that.

def get_given_argument_list() :
	This method is actually takes two list of vehicles entities and the name of the attributes whose values we have to extract and convert into list and then returns to the caller I used this method for the purpose of finding maximum and minimum values among all those vehicles.

def get_vehicles _compares_attributes () :
	This method is mainly used to check whose attributes contains a maximum and minimum values.


	
MAIN.PY

This class is main.py where I have defined the necessary function structure for my project. Then, it contains my main python project by writing the codes required to compile the program here.


def create_new_electricVehicle_to_database():
	This method is used  for vehicle name, manufacturer and year is taken as parameters/filters and checked with the data store if there is any data available first to avoid multiple entry of same data. If data is not available in datastore then a new entry is created with the parameters taken from user in form of electVehicle object.


def store_time():
	This method is used to save email id in the datastore when user has logged in.


def root():
	This method is used to render the first page of the application i.e., the index.html file. The initial flow of the application starts with this root method.

def get_vehicle_page():
	This method renders add_new_vehicle.html page


def add_new_vehicle_to_the_database():
	This method is used  for vehicle name, manufacturer, year, battery size,  wltp range, cost and power these parameters are taken from the user and passed to create_new_electricVehicle_to_database function for adding it to datastore.


def view_all_Vehicle():
	This method is used  for all the list of vehicles are extracted from datastore with help of database handler and passed to view_all_vehicle.html for rendering.


def get_vehicle_information():
	This method is used to get the vehicle information using GET method. 

def update_vehicle_information():
	This method is used a single object of vehicle is extracted from datastore with id as a parameter using database handler and passed to show_information_vehicle.html for rending.


def delete_vehicle_information():
	This method is used  for id is taken as a parameter for deleting its entry from datastore and then the list of vehicles are extracted from datastore with help of database handler and passed to view_all_vehicle.html for rendering.


def compare_more_than_one_element():
	This method is used  for comparing two vehicle data with help of checkboxes which are marked checked. A for loop is taken for multiple id to get vehicle data from datastore then added to vehicle_comparing_list with help of vehicle helper class. The compared data is then rendered on comparing_vehicle_page.html.
