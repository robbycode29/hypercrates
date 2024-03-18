# Hypercrates
An ACL rudimentary demo for medical systems management

Live at: https://hypercrates-900239d97135.herokuapp.com/

# Getting started

Fork and then clone this repo on a machine where you have docker and docker-compose installed,
then use the following commands:
    - `$ cd hypercrates/hyper`
    - `$ docker-compose up`

After installation you will need to apply migrations in order to set up the db:
   - `$ docker-compose exec web python manage.py migrate`

And also create a superuser in order to access Django Admin at `/admin` (optional)
   - `$ docker-compose exec web python manage.py migrate` - follow the instructions provided

It is necessary to load the fixture users.json as it provides groups for access rights.
   - `$ docker-compose exec web python manage.py loaddata users.json`

You can also load mock data into the db by doing:
   - `$ docker-compose exec web python manage.py loaddata data.json`

# 📄 How to use

This REST API app allows for basic hospital management tasks to be done in an ACL manner.

## 🔖 How to use the Hypercrates

### OAuth 2.0

- Use /api/login/ to log into one of these users to get a Token:
    - `"username": "gm_user", "password": "pass1"`.
    - `"username": "doctor_user", "password": "pass2".`
    - `"username": "assistant_user", "password": "pass3".`
- Use the token to access any other endpoints you have permission to use.
- Here is a list with usable endpoints:
                                                                                  
![Background (1)](https://github.com/robbycode29/hypercrates/assets/91128928/ef8e1403-03f4-43c4-9ce3-ff20bc188d50)


# Tesing 

The API has a test suite implemented containing integration and unit tests. You can check tests by doing:
   - `$ docker-compose exec web python manage.py test`

# Contact

For any questions regarding this API please contact me at: robertandrei.oprescu@gmail.com
---
