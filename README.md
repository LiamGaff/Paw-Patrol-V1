# Paw-Patrol
PawPatrol is a web application designed to model a charitable organization that deals with housing pets for owners that can no longer take care of their animals due to medical reasons. This website was built as part of my fourth and final milestone project for CodeInstitutes diploma in software development. You can visit the deployed site from [here](https://paw-patrol-lg.herokuapp.com/).


## Development Notes
Due to problems with my payment system I was unable to get the webpage fully operational before my project deadline. The Edit animals function currently can't be used this was also due to time constraints.

# UX
## User Stories
As a user I would like:

* To be informed upon what the website/charity is about.
* To be able to easily navigate the webpage.
* I would like to be able to get in contact with the organization.
* I would like to be to ask questions regarding the charity.
* I would like to be able to sign up for a free account.
* I would like to be able to log in to my account.
* I would like to be able to easily log out of my account.
* I would like to have a place where I can view my previous donations.
* I would like to be able to have readily available options to be directed to the donate page.
* I would like to be able to easily make donations via card payment.
* I would want to know more about both the animals and the volunteers that house them.
* I would like to be informed of when my payment has been made.
* I would like to read updates about how the charity and the animals are doing.


## Organisation Goals
* To raise awareness for the charity and its goals.
* To raise as much money as possible to benefit the cause of the charity.
* To be able to answer users' questions about the organization.
* To sign up new users.
* To have an easy online payment system for users to donate,


## Strategy
This web page was designed as a charity page for a fictional charity. The page should be informative and easily navigated. All the features to be implemented are to inform the user of the value of donating to the charity and make donating as easy as possible.

## Scope
The user needs had to be met as this would encourage the users to make a donation. Being able to access the donation page from any point of the webpage was very important. I wanted them to allow no delay between the user deciding to make a donation and then doing so. Currently, you have to sign up to make a donation but I would like to be able to remove this if you are only making a one-time donation. Signing up and logging in are all done very easily though.

## Structure

**Home**

This page is broken up into three sections. The first is the about sections. This just contains a paragraph about what this
organization does. This is in place to inform users right away about what they might be donating to.

The next section displays all the volunteers working for the charity. These are displayed in cards with some info on each volunteer.

Last is the contact section. This is divided into a general contact info section and contact forum to directly contact the charity through the website.

**Donate**

The donate page has two sections. The most important section is the donate card. This is formed with a stripe element that allows users to submit a donation via card payment. Users need to set up a profile to donate as this allows them to keep track of all their donations. Previously the amount was chosen through set amounts attached to radio buttons. This caused issues so the amount is now chosen through a number input.

The other section just gives a little more info of what the user's donation will contribute to the cause of the organization.

**Animals**

This page displays the animals that are currently in the charity's care. These are displayed in cards and give some basic info on each animal.

**Profile**

The profile page is mainly a place to display the user's info and payment history. The top of the page is divided into user details and the payment history which is displayed on a table.

The profile page also contains a donation card so that a user can make donations straight from their profile.

**Signup/Login/Logout**

The signup, login, and logout pages were all built using allauth and all maintain the same design and features.

## Skeleton
The design of the webpage was first and foremost about the animals. That's why the header image displays two rather cute-looking animals once you open the webpage. I did some research on color schemes to figure out how to make the webpage look serious but yet fun and inviting. The users should know that it is a serious cause but also when it comes to the animals you want them to feel comforted by the idea of the organization, not scared. That's why these colors and fonts were chosen and they will be discussed further in the Design section below.

## Design
**Wire Frames**

 The web page was designed using Balsamiq to create some basic wireframes. The design of the page really evolved from the basic wireframes as it came together so the actual website differs from the original designs(Link below).

 [wire frames](wireframes.md)
 

**Colors**

* The Background color (#c5d5cb) I found while researching web page color schemes. I felt it made the webpage look very professional and also very inviting. The soft soothing green color I found to be relaxing for users and in turn makes them feel safe and trusting of this charity organization.

* The color used for any cards was a lightly tanned color. This paired nicely with the light green background allowing the most important info to stand out. Most of the cards also have a grey box shadow to make them pop out.

* The font colors are mostly charcoal black, navy, or light grey. These colour were chosen to make the text visible for a wide range of users.

* The blog page was styled very differently from the rest of the site. This was done to make it feel like the blog page was its own element. People may come back to the site just to see updates on the charity so I wanted it to feel somewhat seperate from the rest of the site yet still geared towards informing and encouraging users to donate.


**typography**
 
 * For the headings I used a 'Luckiest Guy', cursive font. I hoped this font would add a light and fun element to the site. 

 * For the donation banner I wanted to use another fun-looking font so I chose to go with 'Shadows Into Light', cursive as it gave a nice handwritten effect.

 * I played around with a lot of fonts but eventually, I settled on leaving all other fonts as 'Lora', Lato as it made the content easier to read.

# Features
## Existing Features

* A Navbar which contains links to each page as well as a highlighted donate button which will direct you to the donate page.

* A contact form for directing questions to the charity organisation straigth from the home page.

* A payment section where users can select an amount to donate and then pay with a card trhough a stripe payment system.

* It is possible to Signup, Login and Logout all from the page management link on the navigation menu. All these operations are done with allauth.

* Donate buttons found through out the page which will direct you straight to the donation page. 

* Your profile page also contains a payment section for making donations.

* A donation history section where all your previous donations are saved with the date, amount, and donation ID.

* You can change yoour password from your profile page. This is done through allauth.

* Admin control - as an admin you can edit, delete, and add new animals or blog posts through forms on the webpage.


## Features Still to Be Implemented
* I would like to set up an automatic monthly payment system. As I had some trouble with setting up the stripe payment system I had didn't have time to do this.

# Technologies Used
## Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://javascript.info/)
* [Python](https://www.python.org/download/releases/3.0/)
* [Stripe](https://stripe.com/docs)


## Frameworks and Programs

* [Balsamiq](https://balsamiq.com/wireframes/?gclid=Cj0KCQiA48j9BRC-ARIsAMQu3WSc14tIkeDZUlWDIVOa-Acbyn1s5XvsJJ6CnWplwD7_WPcgk-C4cTgaAsaNEALw_wcB)
> I used Balsamiq to make my wireframes.

* [GitHub](https://github.com/)
> GitHub was used to push content to the repository.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator)
> CSS code was checked using CSS W3C CSS Validator.

* [Online Beautifier](https://beautifier.io/)
> Online Beautifier was used to beautify my HTML, CSS, and JavaScript code.

* [W3C Markup Validator](https://validator.w3.org/nu/#textarea)
>W3C Markup Validator was used to check the HTML code.

* [Google Fonts](https://fonts.google.com/)
>All fonts came from Google Fonts.

* [Django](https://www.djangoproject.com/)
>The entire site was built on the Django framework.

* [AWS S3 Bucket](https://aws.amazon.com/)
> AWS was used to store static and media files.

* [Djngo Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
> Used to style forms.

* [BootStarp](https://getbootstrap.com/)
> Was used to prvide layout and styling.

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
> Was used to handle all the user functionality.

# Database

Production Database: PostgresSQL

Development Database: SQLite3

## Database Table
Table | Value 1 | value 2 | value 3 | value 4 | value 5 | value 6 | value 7 |
----- |  ------ | ------- | ------- | ------- | ------- | ------- | ------- |
Animals | friendly_name| name |type | breed | about | image | id |
Volunteers |  friendly_name | name | about | image | 
Donations |  User | amount | date | id | 
Users |  username | email | first name | last name | 
Blog Posts |  author | story | date| image | id |

# Testing

Most of the testing can be found on my TESTING.md document which can be found [here](TESTING.md).


## Browser Compatibility Test
Nm | Browser | Action | Test result |
-- | ------- | ------ | ----------- |
#1 | Chrome | Open app in browser. |  |
#2 | Firefox | Open app in browser. |  |
#3 | Safari | Open app in browser. |  |


## Deployment

## Heroku
* Sign in to a Heroku account

* Click on the New button to create a new app with an unused name.

* Next select the app and then click on Settings in the menu.

* Find "Config Vars" section and click on the "Reveal Config Vars" button and enter values (e.g SECRET_KEY, STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET...).

* Install Heroku via the terminal using npm install -g Heroku.

*  Log into Heroku via the terminal using heroku login and follow the on-screen instructions to log in.

* Create a requirements.txt via the terminal using pip3 freeze > requirements.txt.

* Create a Procfile.

* Connect GitHub to Heroku via the terminal using Heroku git:remote a appname.

* Commit all files in your project using git add .' followed by 'git commit -m "commit message".

* Set up automatic deployment from heroku dashboard.

* Push and deploy all files to github and Heroku using the terminal command git push.

* Enter the heroku Postgres database URL to the settings.py file.

* Make migrations and migrate to create the database by using the terminal command python3 manage.py makemigrations and python3 manage.py migrate.

* Create a superuser in your new database by using the terminal command python3 manage.py createsuperuser and follow the instructions prompted in the terminal window.

* After setting up the database and the build on Heroku is complete, click on the heroku link or 'view app' button to run the application via Heroku.

## How to Fork it
* log in or Sign Up to GitHub.
* On GitHub, go to []().
* In the top right, click "Fork".
* You should then create an env.py file with your secret values.
* You will need to install all of the project requirements. This can be done using the command pip3 install -r requirements.txt.
* Use python3 manage.py runserver to run the server and view the app.

## How to clone this project
## With Gitpod
* Create a Gitpod account and install Gitpod Browser extension for chrome.
* Log into your gitpod account.
* Go to [Github repository](https://github.com/LiamGaff/Paw_Patrol_V1) and click on the green "Gitpod" button.
* This will open a new Gitpod workspace created from the code in the github repository where you can work.
* You will need to create an env.py file with your values.
* You will need to install all of the project requirements. This can be done using the command pip3 install -r requirements.txt.
* Make migrations and migrate to create the database by using the terminal command python3 manage.py makemigrations and python3 manage.py migrate.
* You will need to create a superuser for your database. This can also be done in the terminal using "python3 manage.py createsuperuser" and then following instructions.
* Use python3 manage.py runserver to run the server and view the app.

## Local IDE
* Go to my Github repository [here](https://github.com/LiamGaff/Paw_Patrol_V1).
* Under the repository name click "Code".
* Here you can either Clone or Download the repository.
* You should clone the repository using HTTPS, clicking on the icon to copy the link.
* Open the terminal.
* Change the current working directory to where you want the cloned directory to be.
* Type git clone, and then paste the URL that was copied in the previous step.
* Press enter and a local clone will be created.
* You will need to create an env.py file with your values.
* You will need to install all of the project requirements. This can be done using the command pip3 install -r requirements.txt.
* Make migrations and migrate to create the database by using the terminal command python3 manage.py makemigrations and python3 manage.py migrate.
* You will need to create a superuser for your database. This can also be done in the terminal using "python3 manage.py createsuperuser" and then follow instructions.
* Use python3 manage.py runserver to run the server and view the app.

# Credits

## Code
* W3 School and StackFlow were greatly used throughout this project.
* I used a combination of code from youtube to build both the blog(Lukas Vyhnalek channel) and the payment system.
* Some code used came from the CodeInstitue Boutique Ado project.

## Acknowledgments
* I would also like to credit and thank my mentor Brian Macharia for all his help and excellent guidance throughout this project. Also Eoin O'Neill who also reviewed my work and was a huge help.

* I would like to thank my tutors and the slack community for all the help they provided me.