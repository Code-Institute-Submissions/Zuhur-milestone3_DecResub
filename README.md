# RecipeClub

**Milestone 3 project for Code institute Software Development Programme.**
![](/static/ms3wireframes/ms3-responsive.png)
[Live site](https://milestone-three.herokuapp.com/)
## Table of contents
-   [User Experience](#user-experience)
    *   [Strategy](#strategy)
    *   [User Stories](#user-stories)
-   [Design](#design)
    *   [Wireframes](#wireframes)
    *   [Colours](#colours)
    *   [Fonts](#fonts)
-   [Features](#features)
    *   [Existing Features](#existing-features) 
    *   [Future eatures](#future-features)
-   [Technologies](#technologies)   
-   [Testing](#testing)
-   [Deployment](#deployment)

## User Experience
### Strategy 
The aim of this project is to create an online cookbook where users can create and share their recipes with fellow users. <br>

### User Stories
**As an unregistered user**
1.	I want to be able to understand the purpose of the website
- At the centre of the home page there is a brief description of the purpose of the page and with registrations comes with access to various recipes and uploading own recipes will give user a chance to win recipe of the month.
2.	Be able to register to the website
- There is a call to action button for registration on the index page. As the user scrolls down, they’ll be prompted to register again with another call to action button.
3.	View recipe of the month
- In the home page user only has to scroll to see the recipe of the month.

**As a registered user I would like to**
1.	Be able to log in/log out
- Log in button is available on the navbar for all users at the home page and the log out button only available to logged in users.
3.	Be able to Create, View, Update and Delete recipes
- Users can easily create recipes by following link presented on the navbar. Once a user selects one of their own recipes, they will be presented with both and edit and delete button.
4.	Be able to share recipes while keeping some private
- While creating a recipe, a user can select whether they want to keep the recipe private or not.
5.	Be able to browse and search all public recipes
- In the navbar users can easily navigate to all recipes and select what recipe they'd like to view.

**As the site Admin I would like to be able to**
1.	Post recipe of the month on the Home page
- In the navbar only visible to the admin there, they can click the 'winner' link to where they can then select which recipe has won. The recipe is automatically shown on the index page.
2.	Delete all users’ recipes
- While users can delete their own recipes. These privileges are also awarded to the admin so they can make sure appropriate content is posted.


## Design
### Wireframes
The wireframes were designed using the balsamiq tool for different sections and screen sizes. These can be found [here](static/ms3wireframes/ms3-wireframes.pdf).

### Colours
- #fb8600
- #faedcd
- #f5f5f5
- #28a745
- #f79d65
- #ced4da
- #faebd7

### Fonts
Google fonts: Roboto

## Features

### Existing Features
Features differ between visitors, users and admin. 

**Visitors:** Minimal features available. They can access login and register page. <br>
**Users:** Have access to the above features and all recipes, my recipes, create recipes, logout. They can also edit and delete their own recipes. <br>
**Admin:** Have access to the above features and winners feature. Can also edit and delete all recipes. <br>

### Future features
**Users:** Allow users to participate in voting for recipe of the month. <br>
**Admin:** Give admin rights to delete users. <br>

## Technologies

-	HTML5: For the structure of the site.
-	CSS3: For styling of the site.
-	Bootsrap4: For fast development of the site and its responsiveness.
-	Fontawesome: For visual icons.
-	Github: For remote access of the project.
-	Git: For version-control.
-	Visual Studio Code: A development environment as an upgrade to gitpod.
-  Mongodb: As the database for storing users data
-  Python/Flask: Used for the backend and for communication with mongodb
-  Heroku: Deployment of project

## Testing
[PEP8](http://pep8online.com/) was used to check python file, until file was pep8 compliant. <br>
The HTML validator used was [https://validator.w3.org/](https://validator.w3.org/). Several errors caught due to jinja the other errors were corrected until no errors shown. <br>
The CSS validator used was [https://jigsaw.w3.org/css-validator/validator]( https://jigsaw.w3.org/css-validator/validator). <br>
Google devtools was used to make sure the site is responsive to different devices and screen sizes. <br>

### Manual Testing
#### Testing of user stories
These are tests done on the project based on the user stories, to make sure all functionalities are tested. 

**As an unregistered user I want to**
1.	Be able to register to the website <br/>
Both register buttons lead to the registration page successfully. 
User must enter a name, email with the correct format, and a password with appropriate strength and confirm the password. Incorrectly filled section will prompt user to refill with correct input and entering mismatched password leads to a flash message guiding user to enter matching passwords.

**As a registered User I want to**
1.	Be able to log in <br/>
**Test 1:** Does log in button work? <br/>
**Result:** Log In button on the navigation bar successfully goes to the login page <br/>
**Test 2:** Can a user log in? <br/>
**Result:** User who enters an existing email/password will be logged in successfully. A user who writes an invalid email or password will be prompted to enter correct values. A wrong email/password will ask user to try again. <br/>

2.	Be able to Create, View, Update and Delete recipes <br />
**Test 1:** Does create link work? Can a user create recipe? <br />
**Result:** Yes. all inputs work correctly and require user input. Cancel button redirects user to all recipes page. Delete button also functions and recipe can be deleted. Private recipes are only accessible to owner through ‘My recipes’ link. <br />
**Test 2:** Does ‘Go to recipe’ link work? Can a user view their own recipes? <br/>
**Result:** Yes. ‘My recipes’ button also works and shows user all their recipes. <br/>
**Test 3:** Does Edit button work? Can a user edit their recipe? <br/>
**Result:** Yes. User is directed to the ’Edit recipe’ page. The edit form is functional, cancel button and update button also work. <br/>
**Test 4:** Does delete button work? <br/>
**Result:** Yes. <br/>
**Test 5:** Can admin delete/edit recipes? <br/>
**Result:** Admin can only delete recipe not make edits. <br/>

3.	Be able to share recipes while keeping some private <br/>
**Test 1:** Can users have their recipes public/private? <br/>
**Result:**  Yes. If user does not check the ‘private’ input, their recipe will be public. The user can edit their recipe and decide to make it private by checking the private box. <br/>

**As the Admin I want to**
1.	Post a ‘Recipe of the month’ to the home page <br/>
**Test 1:** Does Winner link work? <br/>
**Result:**  Yes. <br/>
**Test 2:** Can Admin choose a user and recipe? <br/>
**Result:** Yes, drop down shows all public recipes in the database along with the author email. <br/>

2.	Be able to delete any users’ recipes <br/>
**Test 1:** Does delete button work? <br/>
**Result:** Yes.


#### User authentication
Testing has been carried out to make sure unauthenticated users can’t access all pages. Two functions were created to enforce user authentication. The function `def is_authenticated():
    return 'user' in session
`, checks if a user is authenticated by checking if a user is in session object, if not the user is directed to the login page.
The second function `def is_user_owner_of(recipe):
    return recipe['author'] == session['user']` authenticates if a user is the owner of a recipe. If a registered user tries to edit, delete a recipe other than theirs they are redirected to ‘All recipes’ page available to all authenticated users.

## Deployment

- Create app.py file
- Install flask <code> python -m pip install flask </code>
- Create env.py file
- Make sure env.py in gitignore file
- Create requirements.txt file <code> python -m pip freeze > requirements.txt </code>
- Create Procfile <code> echo web: python app.py > Procfile </code>
- Install dnspython <code> python -m pip install flask </code>
- Install flask-pymongo <br>
To Heroku
- Heroku can not read env.py files therefore the contents need to be manually input into config vars (via settings).
- Push all code to GitHub
- Enable automatic deployment to allow automatic update when code pushed to GitHub.

## Credits
### Images
Home page background: https://www.freepik.com/photos/background <br>
Recipe
- https://unsplash.com/photos/Qf-gqJSWFYQ
- https://unsplash.com/photos/TkzdkVn1AyA
- https://unsplash.com/photos/2v-XcWsjftY
- https://unsplash.com/photos/MqT0asuoIcU
- https://unsplash.com/photos/1rqk6XVnw44


