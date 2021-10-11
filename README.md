# Paw-Patrol


# UX
## User Stories
As a user I would like:

* To be informed upon what the website/charity is about.
* To be able to easily navigate the webpage.
* I would like to be able to get in contact with the organisation.
* I would like to be to ask questons regarding the charity.
* I would like to be able to sign up for a free account.
* I would like to have a place where i can view my previous donations.
* I would like to be able to have readily available options to be directed to the donate page.
* 



## Strategy
This web page was designd as a charity page for a ficitional charity(the idea is still usefull). The page should be informative and easily navigated. All the features to be implemented are to inform the user of the value of donating to the charity and make donating as easy as possible.

## Scope
The user needs had to be meet as this would encourage the users to make a donation. Being able to access the doantion page from any point of the webpage was very importnant. I wanted the to allow no dealy between the user deciding to make a donation and then doing so. Currently you have to sign up to make a donation but I would like to be able to remove this if your only making a one time donation. Signing up and loging in are all done very easily though.

## Structure

### Home


### Donate


### Animals


### Profile


### Signup/Login/Logout



## Skeleton
The design of the webpage was first and foremost about the animals. Thats why the header image displays two rather qute looking animals once you open the webpage. I done some research on color schemes to figure out how to make the webpage look serious but yet fun and inviting. The users should know that it is a serious cause but also when it comes to the animals you want them to feel comferted by the idea of the organisation, not scared. That's why these colours and fonts were chosen and they will be discussed forther in the Design section below.

## Design
**Wire Frames**

 The web page was designed using Balsamiq to create some basic wire frames. The design of the page really evolved from the basic wire frames as it came together so the actual website slightly differs from the original designs(Link below).

 [wire frames](wireframes.md)
 

**Colors**

* The Background colour () I found while researching web page colour scemes. I felt it it mde the webpage look very professional and also very inviting. The soft soothing green colour I found to be relaxing for users and in turn make them feel safe and trusting of this charity organisation.

**typography**
 

# Features
## Existing Features

* A Navbar to which contains links to each page aswell ass a hihlighted donate button which will direct you to the donate page.

* A contact form for directing questions the charity organisation straigth from the home page.

* A payment section where users cn select an amount to donate and then pay with card trhough a stripe payment system.

* It is possible to Signup, Login and Logout all from the page management link on the navigation menue. All these operations are done with allauth.

* Donate buttons found through out the page which will direct you straight to the donation page. 

* Your profile page also contains payment section for making donations.

* A donation history section where all your previous donations are saved with the date, amount and donation ID.

* You can change yoour password from your profile page. This is done throuh allauth.


## Features Still to Be Implemented


# Technologies Used
## Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://javascript.info/)
* [Python](https://www.python.org/download/releases/3.0/)
* [MongoDB](https://www.mongodb.com/)
* [Django]()
* [Stripe]()


## Frameworks and Programs

* [Balsamiq](https://balsamiq.com/wireframes/?gclid=Cj0KCQiA48j9BRC-ARIsAMQu3WSc14tIkeDZUlWDIVOa-Acbyn1s5XvsJJ6CnWplwD7_WPcgk-C4cTgaAsaNEALw_wcB)
> I used Balsamiq to make my wire frames.

* [GitHub](https://github.com/)
> GitHub was used to push content to the repository.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator)
> CSS code was checked using CSS W3C CSS Validator.

* [Online Beautifier](https://beautifier.io/)
> Online Beautifier was used to beautify my HTML, CSS and JavaScript code.

* [W3C Markup Validator](https://validator.w3.org/nu/#textarea)
>W3C Markup Validator was used to check the HTML code.

* [Google Fonts](https://fonts.google.com/)
>All fonts came from Google Fonts.

# Database

Production Database: PostgresSQL

Development Database: SQLite3


# Testing

<!-- Most of the testing can be found on my TESTING.md document which can be found [here](TESTING.md). -->


## Browser Compatibility Test
Nm | Browser | Action | Test result |
-- | ------- | ------ | ----------- |
#1 | Chrome | Open app in browser. |  |
#2 | Firefox | Open app in browser. |  |
#3 | Safari | Open app in browser. |  |


## Deployment

## On GitHub repository
<!-- * Use pip3 to install all modules.

* Create an env.py file and make sure it is listed in your .gitignore file. Input all your important secret variables into this file e.g (API_key, SECRET_KEY, IP, PORT, MONGO_URI, and MONGO_DBNAME.)

* Enter this at the top of your python app file - if os.path.exists("env.py"): import env.

* For each environmental variable, define the variables in the app.py file

* When all the necessary modules are installed and the env.py file is complete, your Requirements.txt file and list all the modules by entering this into the terminal - pip3 freeze --local > requirements.txt

* Create a Procfile that will tell Heroku how to run your app - echo web: python app.py > Procfile

* Git add, commit and push all your changes to the github repository. -->

## Heroku
* Sign in to a Heroku account

* Click on the New button to create a new app with an unused name.

* Next select the app and then click on Settings in the menu.

* Find "Config Vars" section and click on the "Reveal Config Vars" button.

## How to Fork it
<!-- * log in or Sign Up to GitHub.
* On GitHub, go to []().
* In the top right, click "Fork".
* You should then create an env.py file with your values, and create a MongoDB database with the data keys that are in the above example.
* You will need to install all of the project requirements. This can be done using the command pip3 install -r requirements.txt.
* Type python3 app.py in your GitPod terminal to run the project. -->

## How to clone this project
## With Gitpod
<!-- * Create a Gitpod account and install Gitpod Browser extension for chrome.
* Log into your gitpod account.
* Go to [Github repository]() and click on the green "Gitpod" button.
* This will open a new Gitpod workspace created from the code in the github repository where you can work.
* You will need to create an env.py file with your values, and create a MongoDB database with the data keys given in the example above.
* You will need to install all of the project requirements. This can be done using the command pip3 install -r requirements.txt.
* Type python3 app.py in your GitPod terminal to run the project. -->

## Local IDE
<!-- * Go to my Github repository [here]().
* Under the repository name click "Code".
* Here you can either Clone or Download the repository.
* You should clone the repository using HTTPS, clicking on the icon to copy the link.
* Open the terminal.
* Change the current working directory to where you want the cloned directory to be.
* Type git clone, and then paste the URL that was copied in the previous step.
* Press enter and a local clone will be created.
* You will need to create an env.py file with your values, and create a MongoDB database with the data keys given in the example above.
* You will need to install all of the project requirements. This can be done using the command pip3 install -r requirements.txt. -->

# Credits

## Code
* W3 School and StackFlow were greatly used throughout this project.

## Acknowledgments
* I would also like to credit and thank my mentor Brian Macharia for all his help and excellent guidance throughout this project. Also Eoin O'Neill who also reviewed my work and was a huge help.

* I would like to thank my tutors and the slack community for all the help they provided me with.