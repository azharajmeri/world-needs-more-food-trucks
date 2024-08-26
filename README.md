# 🚀 RAKT's "Out-of-the-Box" Engineering Challenge 🌟

## 🌐 The Problem : World Needs More Food Trucks!

Our team in San Francisco are on a quest to discover the hidden gems of street food, particularly food trucks! Your challenge is to to make it possible for us to find a food truck no matter where our work takes us in the city.

This is a freeform assignment. You can write a web API that returns a set of food trucks (our team is fluent in JSON). You can write a web frontend that visualizes the nearby food trucks. We also spend a lot of time in the shell, so a CLI that gives us a couple of local options would be great. And don't be constrained by these ideas if you have a better one!

The only requirement for the assignment is that it give us at least 5 food trucks to choose from a particular latitude and longitude.

Feel free to tackle this problem in a way that demonstrates your expertise of an area -- or takes you out of your comfort zone. For example, if you build Web APIs by day and want to build a frontend to the problem or a completely different language instead, by all means go for it - learning is a core competency in our group. Let us know this context in your solution's documentation.

San Francisco's food truck open dataset (csv) is included in this [repo](https://raw.githubusercontent.com/RAKT-Innovations/P1-django-take-home-assignment/main/food-truck-data.csv).


## Setup Instructions

### Python version is mentioned in runtime.txt

1. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Run migrations:**
    ```bash
    python3 manage.py migrate
    ```

3. **Import data:**
    ```bash
    python3 manage.py import_food_trucks
    ```
   This command loads the data into the database from the CSV file.

4. **Run the development server:**
    ```bash
    python3 manage.py runserver
    ```

## Endpoints

- **Frontend endpoint:**
  
    http://127.0.0.1:8000/get/food-trucks/?lat=37.7535091222127&lng=-122.4500712081

- **API endpoint:**
  
    http://127.0.0.1:8000/api/get/food-trucks/?lat=37.7535091222127&lng=-122.4500712081


## DATABASE (Using PostGIS with Django)

PostGIS is an extension for PostgreSQL that provides spatial database capabilities. 
It allows you to store and query geographic objects and perform spatial operations directly in the database. 
PostGIS is ideal for applications that require geographic data handling, such as mapping or 
location-based services.

### CREATE DATABASE
    postgres=# create database foodtruckdb;

### CREATE ROLE
    postgres=# create user foodtruckuser with encrypted password 'hard@123';

### GRANT
    postgres=# grant all privileges on database foodtruckdb to foodtruckuser;

### ALTER ROLE TO SUPERUSER
    postgres=# alter role foodtruckuser superuser;

#### CREATE EXTENSION "postgis"

### ALTER ROLE TO NOSUPERUSER
    postgres=# alter role foodtruckuser nosuperuser;

### SAMPLE ".env"

    DATABASE_NAME=foodtruckdb
    DATABASE_USER=foodtruckuser
    DATABASE_PASSWORD=hard@123
    DATABASE_HOST=localhost
    DATABASE_PORT=5432

