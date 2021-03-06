# TechLab - _API Server_
## General information
The TechLab API server runs on Django 2.1.7 with the django REST framework 3.9.2 and is developed in Python. 
## Installation
In order to run the django server there are a couple of requirements.  
You nee Python 3.7 and have to install all of the requirements for django by running the following command in the project 
root folder `pip install -r requirements.txt`.  
After the installation of the python requirements for Django there still are a couple of commands that have to be ran 
before you're able to run the server.  

To start with, for the creation of the local database and the addition of the required tables and columns you will have 
to run the following command `python manage.py migrate`. Migrations can be seen as version changes of a database, e.g. 
each time a new functionality with models gets added there will be a new 'migration' for the databases.  
After setting up the database you are able to create a 'superuser', this can be seen as the admin of the web interface,
this can be done by using the following command `python manage.py createsuperuser`, after using the command you will be 
prompted to fill in a username, email and password.   
**Note:** Before you run any of the commands, make sure you are inside of the project folder, i.e. the `TechLab/` folder, 
at which the `requirement.txt`, `manage.py` and this file are located.
## Migrations
After making changes to the database models you want the changes to take effect on the database, but before the database 
knows about the changes it has to compare the old models with the current models. It is a sort of version control for 
the database. These 'versions' get created by using the following command `python manage.py makemigrations`. After 
running this command you ALWAYS have to run the migrate command in order to let the changes take effect to the database.  

## Running the server
After installing all the requirements you are able to run the server in two different configurations.  
1. As Developer `python manage.py runserver --settings=TechLab.settings.development`
2. In Production `python manage.py runserver `

## More information 
For some more information on the usage of Django and a development tutorial [Click Here](https://docs.djangoproject.com/en/2.1/intro/)

## API requests

At this moment the following will be the API for the application. It hasn't been implemented yet, but will very soon.
~~~~
items/
	-> GET
	-> Data Params GET:
		- {}
	-> Success Response GET:
		- code: 200 
		- content: [{
				"books": [{
					"book_title": "",
					"book_description": "",
					"book_image": "https://www.example.com/image/example.jpg",
					"writers": ["", "", ""],
					"isbn": "",
					"publisher": "",
					"is_available": true,
					"borrow_days": 5
				}], 
				"electronics": [{
					"electronic_title": "",
					"electronic_description": "",
					"electionric_image": "https://www.example.com/image/example.jpg",
					"manufacturer": ["", "", ""],
					"category": "",
					"is_available": false,
					"borrow_days": 3

				}]
			}]

electronics/
	-> GET: een lijst van alle electronics opvragen
	-> POST: nieuw electronics item aanmaken
	-> Data Params GET:
		- {}
	-> Data Params POST: 
		-  {
					product_id: string, 
					borrow_days: int, 
					description: string, 
					image: BASE64, 
					manufacturer: list[int], 
					category: int, 
					name: string, 
					stock: int, 
					api_key: uuid
				}
	-> Success Response GET:
		- code: 200 
		- content: [{
				"electronic_title": "",
				"electronic_description": "",
				"electionric_image": "https://www.example.com/image/example.jpg",
				"manufacturer": [],
				"category": "",
				"is_available": false,
				"borrow_days": 3
			}]
	-> Success Response POST:
		- code: 200 
		- content: {"success": "The item has been added. "}
	-> Error Response POST:
		- code: 401 - Unauthorized 
		- content: {"error": "The user is not allowed to POST to here. "}

electronics/<id>/
	-> GET: alle data van electronics id
	-> POST: update alle data van electronics id
	-> DELETE: het verwijderen van een electronics item
	-> Data Params GET: 
		- {}
	-> Data Params POST:
		-  {
				product_id: string, 
				borrow_days: int, 
				description: string, 
				image: BASE64, 
				manufacturer: list[int], 
				category: int, 
				name: string, 
				stock: int, 
				api_key: uuid
			}
	-> Data Params DELETE
		- {api_key: uuid}
	-> Success Response GET:
		- code: 200 
		- content: {
				"electronic_title": "",
				"electronic_description": "",
				"electionric_image": "https://www.example.com/image/example.jpg",
				"manufacturer": [],
				"category": "",
				"is_available": false,
				"borrow_days": 3
			}
	-> Success Response POST:
		- code 200
		- content: {"success": "The item has been updated. "}
	-> Success Response DELETE:
		- code: 200 
		- content: {"success": "The item has been deleted. "}	
	-> Error Response GET: 
		- code 404
		- content: {"error": "No asset found electronic with id <id>."}
	-> Error Response POST: 
		- code 404
		- content: {"error": "No asset found electronic with id <id>."}
	-> Error Response DELETE:
		- code: 401 - Unauthorized 
		- content: {"error": "The user is not allowed to POST to here. "}

books/
	-> GET: een lijst van alle books opvragen
	-> POST: nieuw books item aanmaken
	-> Data Params:
	-> Data Params GET:
		- {}
	-> Data Params POST:
		-{
				title: string, 
				borrow_days: int, 
				description: string, 
				image: BASE64, 
				writers: list[int], 
				isbn: string, 
				publisher: int, 
				stock: int, 
				api_key: uuid
			}
	-> Success Response GET:
		- code: 200 
		- content: [{
					"book_title": "",
					"book_description": "",
					"book_image": "https://www.example.com/image/example.jpg",
					"writers": [],
					"isbn": "",
					"publisher": "",
					"is_available": true,
					"borrow_days": 5
				}]
	-> Success Response POST:
		- code 200
		- content: {"success": "The item has been added. "}

books/<id>/
	-> GET: alle data van books id
	-> POST: update alle data van books id
	-> DELETE: het verwijderen van een books item
	-> Data Params GET: 
		- {}
	-> Data Params POST:
		-  {
				"title": string, 
				"borrow_days": int, 
				"description": string, 
				"image": BASE64, 
				"writers": list[int], 
				"isbn": string, 
				"publisher": int, 
				"stock": int, 
				"api_key": uuid
			}
	-> Data Params DELETE
		- {api_key: uuid}
	-> Success Response GET:
		- code: 200 
		- content: {
					"book_title": "",
					"book_description": "",
					"book_image": "https://www.example.com/image/example.jpg",
					"writers": [],
					"isbn": "",
					"publisher": "",
					"is_available": true,
					"borrow_days": 5
				}
	-> Success Response POST:
		- code 200
		- content: {"success": "The item has been updated. "}
	-> Success Response DELETE:
		- code: 200 
		- content: {"success": "The item has been deleted. "}	
	-> Error Response GET: 
		- code 404
		- content: {"error": "No asset found electronic with id <id>."}
	-> Error Response POST: 
		- code 404
		- content: {"error": "No asset found electronic with id <id>."}
	-> Error Response DELETE:
		- code: 401 - Unauthorized 
		- content: {"error": "The user is not allowed to POST to here. "}

BorrowItems/
	-> GET: lijst van geleende items van gebruiker x				
	-> POST: item lenen
	-> Data Params GET:
		- {
				user_id: int
			}
	-> Data Params POST:
		- {
				"item_id": int, 
				"user_id": int, 
				"borrow_date": date, 
				"return_date": date
			}
	-> Success Response GET:
		- code 200
		- content: [{
				"item": {
					"type":"Book",
					"book_title": "",
					"book_description": "",
					"book_image": "https://www.example.com/image/example.jpg",
					"writers": [],
					"isbn": "",
					"publisher": "",
					"is_available": true,
					"borrow_days": 5
				},
				"user": user_id,
				"borrow_date": 21-01-2019,
				"return_date": 23-01-2019,
			}] 
	-> Success Response POST:
		- code 200
		- content: {"success": "The item has been borrowed"}
	-> Error Response POST:
		- code 200
		- content: {"error":"Item not found. "}
	-> Error Response POST:
		- code 200
		- content: {"error":"Invalid borrow date. "}
	-> Error Response POST:
		- code 200
		- content: {"error":"Invalid return date. "}

ReturnItems/
	-> POST: item terugbrengen
	-> GET: lijst van teruggebrachte items van gebruiker x
	-> Data Params GET:
		- {
				user_id: int
			}
	-> Data Params POST:
		- {
				"borrow_id": int,
				"item_id": int, 
				"user_id": int, 
				"borrow_date": date, 
				"return_date": date
			}
	-> Success Response GET:
		- code 200
		- content: [{
				"item": {
					"type":"Book",
					"book_title": "",
					"book_description": "",
					"book_image": "https://www.example.com/image/example.jpg",
					"writers": [],
					"isbn": "",
					"publisher": "",
					"is_available": true,
					"borrow_days": 5
				},
				"user": user_id,
				"borrow_date": 21-01-2019,
				"return_date": 23-01-2019,
				"hand_in_date": 23-01-2019
			}] 
	-> Success Response POST:
		- code 200
		- content: {"success": "The item has been returned"}
	-> Error Response POST:
		- code 200
		- content: {"error":"Item not found. "}
	-> Error Response POST:
		- code 200
		- content: {"error":"BorrowItem not found. "}
~~~~
### Not yet finished. 
~~~~
manufacturers/
	-> GET: lijst van alle manufacturers
	-> POST: nieuwe manufacturer aanmaken
	-> Data Params:
		- GET: {}
		- POST: {name: string}

writers/
	-> GET: lijst van alle writers
	-> POST: nieuwe manufacturer aanmaken
	-> Data Params:
		- GET: {}
		- POST: {name: string}

categories/
	-> GET: lijst van alle categories
	-> POST: nieuwe manufacturer aanmaken
	-> Data Params:
		- GET: {}
		- POST: {name: string}

publishers/
	-> GET: lijst van alle publishers
	-> POST: nieuwe manufacturer aanmaken
	-> Data Params:
		- GET: {}
		- POST: {name: string}

beheerders/
	-> GET: verkrijg een lijst van alle beheerders
	-> POST: Voeg een nieuwe beheerder toe
	-> Data Params:
		- GET: {}
		- POST: {email: email, user_id: int, api_key: uuid}, DELETE: {user_id: int, api_key: uuid}

beheerders/<id>/ - {GET: {}, DELETE: {api_key: uuid}}
				-> GET: controleer of gebruiker met user_id x een beheerder is
				-> DELETE: verwijder een beheerder
				
statistics/ - {GET: {}}
				-> GET: Het ophalen van globale statistieken van de gebruikers. 
~~~~
