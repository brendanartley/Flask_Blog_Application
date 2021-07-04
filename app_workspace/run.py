from flask_app import create_app

#using default config as we are not passing any variables.
app = create_app()


if __name__ == '__main__':
    app.run(debug=True)

# -- dependancies -- 
# running: pip freeze > requirements.txt creates list of dependancies for other users.

# -- automatic debug mode option -- 
#call: %python flask_app.py
#if called w/ python, debug mode set to true

# -- manual debug mode option (ran in terminal) -- 
#call: %export FLASK_APP=flask_app.py
#call: %export FLASK_DEBUG=1
#call: %flask run

# -- test user account -- 
#u: test@gmail.com
#p: test