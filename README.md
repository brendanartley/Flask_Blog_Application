# Flask_Blog_Application

Thanks to [Corey Schafer's Flask Turotials Series](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH), I was able to learn how to create a fully functional web application from scratch using Flask.

The application is built to function as a Blog. User and Post data are stored in an SQL database. Users can update and delete their own posts, change their profile pictures, reset their password via email-authetication and more. Throughout development, the project transitioned from a few simple python scripts to an application with a full-package structure.

__Completed Project Checklist__

- Flask Forms/User Input
- SQL Database w/ Flask-SQLAlchemy
- Package Structuring
- User Authentication
- Update/Delete/Create Posts
- Pagination
- Email and Password Rest
- Flask Blueprints and Configuration
- Custom Error Pages

## Back-End 

The application is implemented with Flask and SQLAlchemy at its core. The application can be deployed using Heroku or another free-deployment-service (Currently a student with little income).

## Front-End

The user side of the application is written in Javascript and uses Bootsrap 5.0.1 to create responsive design across a wide range of devices. Using Jinja, data is passed into differnet HTML templates to render the final documents.

## Forms/Form Validation

The application contains a variety of classes built using the WTForms Package. Many classes were formed such as LoginForm, RegistrationForm, PostForm, ResetRequestForm, and more. These forms can be passed inputs of different data types and validators to ensure that users only input information relative to that specific form field. Each of these forms inherited the base form class, and often had built in functions to perform extra validation checks and database queries. For example, if a user was trying to reset their password via email, the database had to be queried in order to determine if their was an email associated with a user in the database. These extra validation checks bulletproof the application and deter faulty user-requests from occuring.

## SQL Database

All the data asssociated with the application is stored in an SQL database. This includes both the Users, Posts, and their respective metadata. The User's passwords are hashed to provide further security to potential data breaches. Furthermore, if a user attempts to reset their password via email, a tokenized link is created and must be accessed within a timelimit for the User to successfully change their password. The way that the database is initialized in the application with SQLAlchemy allows for very few lines of code to transition from a local DB to a fully functional PostGreSQL Database.

## Further Improvements

I would like to implement a Natural Language Processing Recurrent Neural Network to provide sentiment analysis on each post that has been created. Flask will work fine for this simple application and for a single RNN model. For large-scale web applications with complex back-end functionality it may be worth looking into building an application using Django.

## Running the application

1. Intall Dependancies

The neccessary dependancies are stored in a requirements.txt file, which was created with the following line of code.

`pip freeze > requirements.txt`

To install these dependancies, activate a venv, navigate to the correct directory and enter the following in the command line.

`pip install -r requirements.txt`

2. Set Secret Keys

Change the SECRET_KEY and SQLALCHEMY_DATABASE_URI variables to access the existing database.

```
SECRET_KEY='5791628bb0b13ce0c676dfde280ba245'
SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
```

Enter your own GMAIL account login into the EMAIL_USER, and EMAIL_PASS in order to send password reset requests to users.

```
EMAIL_USER='your_email_here@gmail.com'
EMAIL_PASS='your_password_here'
```


3. Run Web App

Unzip the app_workspace file, navigate to the app_workspace folder using the command line, the enter the following command.

`python run.py`
