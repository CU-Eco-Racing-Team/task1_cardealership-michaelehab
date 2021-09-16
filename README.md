# Car Dealer API

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

Working within a virtual environment is recommended.

#### PIP Dependencies

Make sure you're in the root directory and run:

```bash
pip install -r requirements.txt
```

This will install all of the required packages in the `requirements.txt` file.

## Database Setup
With Postgres running run:
```bash
python manage.py makemigrations
```
When you run it for the first time, the default models in  our project will get migrated and the makemigrations command creates a file with all the SQL commands that needs to be executed for the models. The migrate command will execute SQL commands :
```bash
python manage.py migrate
```
### API Endpoints

#### GET /api/cars
- General: 
  - Sends a list of sold and unsold cars.

#### POST /api/cars
- General: 
  - Adds a new unsold car to the DB.
  - Sample Request : <br>`{
    "car_model": "X6",
    "industry": 1,
    "price": 1000
    }`<br>
   - Response: Returns the added car.

#### GET /api/cars/<int:id>
- General: 
  - Sends all the details related to the requested car.

#### PUT /api/cars/<int:id>
- General: 
  - Edit a car details.
  - Must be signed in as Owner or a Dealer with Administrative permissions

#### DELETE /api/cars/<int:id>
- General: 
  - Deletes a car from the DB.
  - Must be signed in as Owner or a Dealer with Administrative permissions

#### POST /api/register/customer
- General: 
  - Register a new customer.
  - Sample Request : <br>`{
    "username": "John",
    "email": "test@domain.com",
    "password1": "pass",
    "password2": "pass",
    "ssn": 12345678,
    "phone": 0162323332
    }`<br>
   - Response: Returns the user Token

#### POST /api/register/dealer
- General: 
  - Register a new dealer.
  - Sample Request : <br>`{
    "username": "John",
    "email": "test@domain.com",
    "password1": "pass",
    "password2": "pass",
    "ssn": 12345678,
    "phone": 0162323332
    }`<br>
   - Response: Returns the user Token

#### POST /api/register/industry
- General: 
  - Register a new industry.
  - Sample Request : <br>`{
    "username": "BMW",
    "email": "test@domain.com",
    "password1": "pass",
    "password2": "pass",
    "phone": 0162323332
    }`<br>
   - Response: Returns the user Token

#### GET /api/customers
- General: 
  - Sends a list of current customers.

#### GET /api/dealer
- General: 
  - Sends a list of current dealers.

#### GET /api/industries
- General: 
  - Sends a list of current industries.

#### GET /api/contracts
- General: 
  - Sends a list of current contracts.
  - Must be logged in as a dealer or an industry to access the contracts.

#### POST /api/contracts
- General: 
  - Creates a new contract between a dealer and an industry.
  - Must be logged in as a dealer or an industry.
  - Sample Request : <br>`{
    "id": 1,
    "start_date": "2021-09-15",
    "end_date": "2021-10-15",
    "supervisor": 1,
    "industry": 1,
    "number": 3
}`<br>
   - Response: Returns the created contract
   - NOTE : Editing or Deleting a contract is forbidden.

#### GET /api/deals
- General: 
  - Sends a list of deals made by customers.

#### POST /api/deals
- General: 
  - Creates a new deal with customer for buying a specific car.
  - Sample Request : <br>`{
    "car": 1,
    "customer": 1,
    "plate": "abc123",
    "payment": 1
}`<br>
  - NOTE : Editing or Deleting a deal is forbidden.

#### GET /api/deals/<int:id>
- General: 
  - Sends all the details related to the requested deal.