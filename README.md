# Inventory CRUD Flask Application

A simple CRUD application for managing inventory items, built with Flask, SQLAlchemy, Bootstrap, and Docker.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)

## Features

- Add, edit, delete, and view inventory items.
- Responsive user interface using Bootstrap.
- Dockerized for easy deployment.

## Technologies

- **Backend:** Flask, SQLAlchemy
- **Frontend:** Bootstrap
- **Database:** MySQL
- **Containerization:** Docker

## Setup and Installation

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) (for containerization)

### Clone the Repository

```bash
git clone https://github.com/Pablo-pelaez/inventory_crud_flask
cd inventory-crud-flask
```

### Build and Run the app with Docker
```
docker-compose build
docker-compose up
```

## Usage
  * Home Page: View the list of inventory items.
  * Add Item: Navigate to /add to add a new inventory item.
  * Edit Item: Click the "Edit" button on any item to update its details.
  * Delete Item: Click the "Delete" button and confirm to remove an item from the inventory.


## API Endpoints
  * GET /: Displays the list of inventory items.
  * GET /add: Displays the form to add a new inventory item.
  * POST /add: Submits the form to create a new inventory item.
  * GET /edit/<id>: Displays the form to edit an existing inventory item.
  * POST /edit/<id>: Submits the form to update an existing inventory item.
  * POST /delete/<id>: Deletes an inventory item.


## Troubleshooting

  * Docker Issues: Ensure Docker and Docker Compose are installed correctly. Use docker-compose logs to check for any errors.
  * Application Errors: Check the application logs for error messages. Ensure all required environment variables are set.

NOTE: If there's any doubt related to the project or its execution, please let me know!
