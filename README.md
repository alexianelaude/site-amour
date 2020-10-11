# Django web-app to promote "Camino Royale" 

This project is part of MinesParisTech school's associative life, as it aims to promote my list "Camino Royale" for the 2019 Student's council campaign. The website is user-based for mines-paristech email adresses only.

It is composed of: 
- a chat
- the list of events organized, past and future
- Humoristic polls every day
- Forms to place orders for our hotlines 
- A page dedicated to our electoral program, with the possibility to rate and comment the different points, as well as submitting any suggestion.

This website is no longer available online for financial reasons.

# Installation

To install the various requirements, run 
```bash
pip install -r requirements.txt
```

Then to launch the app, run:
```bash
python manage.py runserver
```

# Usage

To create a superuser and have full access to the website's functionnalities, run:
```bash
python manage.py createsuperuser
```
then fill in the required informations. The admin page is accessible at ~/admin url

Mines paristech email adresses are required to create regular users
