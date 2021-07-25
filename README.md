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
**As a user I would like to**
1. Be able to register to the website
- There is a call to action button for registeration on the index page 
2. Be able to log in/log out
- Log in button is available on the navbar for all users at the home page and the log out button only available to logged in users. 
3. Be able to Create, Update and Delete recipes
- Users can easily create recipes by following link presented on the navbar. Once a user selects a one of there own recipes they will be presented with both and edit and delete button.
4. Be able to share recipes while keeping some private
- While creating a recipe users can select whether they want to keep the recipe private or not.
5. Be able to browse and search all public recipes
- In the navbar users can easily navigate to all recipes and select what recipe they'd like to view.

**As the site Admin I would like to**
1. Post recipe of the month on the Home page
- In the navbar only visible to the admin there, they can click the 'winner' link to where they can then select which recipe has won. The recipe is automatically shown on the index page.
2. Maintain functionality such as editting and deleting recipes.
- While users can edit and delete their own recipes. These privileges are also awarded to the admin so they can make sure approproiate content is posted.

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
- Mongodb: As the database for storing users data
- Python/Flask: Used for the backend and for communication with mongodb

## Testing
[PEP8](http://pep8online.com/) was used to check python file, until file was pep8 compliant. <br>
The HTML validator used was [https://validator.w3.org/](https://validator.w3.org/). Several errors caught due to jinja the other errors were corrected until no errors shown.<br>
The CSS validator used was [https://jigsaw.w3.org/css-validator/validator]( https://jigsaw.w3.org/css-validator/validator). <br>
Google devtools was used to make sure the site is responsive to different devices and screen sizes. <br>

### Manual Testing
Navbar: All navlinks for users and admin where tested and making sure they worked and destination where correct. <br>
Buttons: All buttons where manually tested to see if the worked. Delete and edit recipes where tested for admin and regular users, admin has access to edit and delete buttons while uses only have access to recipes they created. <br>
Forms: All inputs were tested to see if any wrong enteries where caught i.e. not filling in required fields results in prompt message before submission allowed.

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


