# Bazar
This repo for the DOS class project at my university. The project is a very simple book library built using seperate distriubted microservices. This is the repo for the catalog service but the whole project cosists of three services:

The Catalog Service: This has all the books info and store this information inside Sqllite database. Also handles all CRUD requests at the books in addition to search and lookup requests. This service has been developed using Vapor Framework.

The Order Service: This handle the buy book requests from the frontend and communicate with the catalog service to check if the book qunantitiy available or not. This sevice has been developed using Vapor framework.

The Frontend Service: This service handle users request to generate dynamic HTML pages, also this service communicate with the two previous services to handle users interaction with the website. To generate the dynamic html code Leaf templating language has been used with Vapor framework.

Project Architecture

#Technologies Used
html+css(normal
file-system as database
flask-python
python anywhere 
