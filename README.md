# RecipeClub

**Milestone 2 project for Code institute Software Development Programme.** 

## User Experience (UX)
### Strategy 
The aim of this project is to create an online cookbook where users can create and share their recipes with fellow users. 

#### User Stories
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





