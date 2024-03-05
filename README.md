# Nihongo-Flashcards

This project allows for the automatic generation of Japanese flashcards based on user input. The site allows the user to create these automatically generated flashcards (or custom cards), and then study them using a spaced repetition method.

# How to run:

FIrst, clone or download the repo
   
## To run the React frontend

1. Navigate to the directory on your computer where the react-frontend-nihongo-flashcards directory lies
2. Run npm i
3. Run npm start


## To run the Django backend

1. Navigate to the directory on your computer where the django-backend-nihongo-flashcards directory lies
2. Install python if it is not locally installed on your computer https://www.python.org/
3. (optional) Create a virtual environment, so that installed packages will only affect / be available this project. To start up a python virtual environment:
      * a. pip install virtualenv                (install the virtual environment package)
      * b. python -m venv nihongo_flashcards     (create a virtual environment)
      * c. nihongo_flashcards\Scripts\activate   (activate the virtual environment)
4. pip install django               (install django in your virtual environment)
5. pip install djangorestframework
6. pip install django-cors-headers  (package for helping Django communicate with React)
7. pip install beautifulsoup4      (package for webscraping)
8. pip install requests
9. python manage.py runserver       (This will run the Django backend server)


### To test out the automatic card generation:
1. Navigate to the 'Create' page
2. Enter a Japanese word of your choice into the 'vocabulary word' text box (for example, try 日本語)
3. Press the 'Get Definition' button
4. Press 'Create Flashcard'

You've created your first automatic flashcard! You can also create your own custom cards if you do not
want to use the automatic creation feature. The app comes preloaded with a few sample cards; you can simply
delete them if you don't want to use them.
I hope you find this app useful, and good luck with your studies!
