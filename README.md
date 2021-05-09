# BetOnYou_Test
Test of job soft skills

### first commande : install virtual env

~~~~{python}
Run in terminal : -> pipenv shell
~~~~

### second commande : install dependencies 

~~~~{python}
Run in terminal : -> pipenv install
~~~~

### fourth commande : initiate and migrate database SQLITE 

~~~~{python}
Run in terminal : -> python application.py db init
                  -> python application.py db migrate --message 'initial database migration'
                  -> python manage.py db upgrade
~~~~

### fifth commande : Run flask app 

~~~~{python}
Run in terminal : -> python application.py run
~~~~

### sixth commande : Run flask test config 

~~~~{python}
Run in terminal : -> python application.py test
~~~~
---
---
## using the API

The api can be used in two ways :

- #### Postman using :
The use with postman is done with predefined urls such as :

    - For all player (Method : GET) -> http://localhost:5000/player
    - For get player by id (Method : GET) -> http://localhost:5000/player/<:id>
    - For create player (Method : POST) -> http://localhost:5000/player
    - For update player (Method : PUT) -> http://localhost:5000/player/<:id>
    - For delete player (Method : DELETE) -> http://localhost:5000/player/<:id>

Or Just import ****BetOnYou_Postman.json**** file in Postman app


- #### Url [localhost](http://localhost:5000) using
You just have to go to a browser and type the url localhost and follow the instructions of the swagger

 All the action urls on the model player are listed there with the possibility of doing a test and seeing the result
 
                                            ...thank you...
