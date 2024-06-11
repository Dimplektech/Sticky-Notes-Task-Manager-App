# Sticky-Notes-Task_Manager-App


In this README file:
- **Project Overview** gives a brief introduction to the project.
- **Features** lists the key functionalities of the project.
- **Installation** provides step-by-step instructions to set up the project locally.
- **Usage** explains how to access and use the application.
- **Models** and **Views** sections give details about the database models and the main views in the application.
- **Running Tests** explains how to run the tests.
- **Credits** 

<h2>Project Overview</h2>
Sticky Note Task Manager Application is Web application designed using django, Pthon and SQLite to help user to create Notes efficiently. It allows users to create, update, delete, and view Posts and notes related to that one of the Post. This application is important for learning fundamental DJango, CRUD (Create, Read, Update, Delete) and creating Database in SQlite. It also allows user to nevigate to one page to another page for view and edit notes.In this apllication one to many relationship has applied to Post and Notes Models where Posts is Parent and Notes is child.

## Features
- **Posts Management**: Create, view, edit, and delete posts.
- **Notes Management**: Create, view, edit, and delete notes associated with specific posts.
- **User Authentication**: Allows users to create and manage posts and notes if authenticated.
- **Automatic Timestamps**: Automatically records the creation and last update time for both posts and notes.

## Installation
1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/sticky-notes-app.git
    cd sticky-notes-app
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## Usage
1. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/`.
## Screenshots
Here are some screenshots of the application in action:
### Home Page With List of Posts
![image](https://github.com/Dimplektech/Sticky-Notes-Task-Manager-App/assets/163059141/cfd3dbaf-a245-4bc2-90ca-109965faed88)

### Post Details
![image](https://github.com/Dimplektech/Sticky-Notes-Task-Manager-App/assets/163059141/c2bc76b7-2c06-459e-9173-8ad43c70cbaf)

### Add new Post
![image](https://github.com/Dimplektech/Sticky-Notes-Task-Manager-App/assets/163059141/3f02abca-8f99-4bd9-8ee6-7ac317b242fa)

### Edit Post
![image](https://github.com/Dimplektech/Sticky-Notes-Task-Manager-App/assets/163059141/24da1e56-22b4-48e5-aafc-52c7b1c06d2b)


### Add new Note to Perticulat Post
![image](https://github.com/Dimplektech/Sticky-Notes-Task-Manager-App/assets/163059141/860276df-ba95-41c9-b769-451136f07f14)


### Edit Note
![image](https://github.com/Dimplektech/Sticky-Notes-Task-Manager-App/assets/163059141/e84d1888-74fb-4cbe-8075-133a3ae89151)


### Note Details
![image](https://github.com/Dimplektech/Sticky-Notes-Task-Manager-App/assets/163059141/c8ecec7a-eb31-495a-a14e-4ef0a0ebb4b6)
   

## Models
### Post
- `title`: The title of the post.
- `content`: The content of the post.
- `created_at`: Timestamp when the post was created.
- `updated_at`: Timestamp when the post was last updated.

### Notes
- `title`: The title of the note.
- `content`: The content of the note.
- `post`: Foreign key relationship to the `Post` model.
- `created_at`: Timestamp when the note was created.
- `updated_at`: Timestamp when the note was last updated.

## Views
### Post Views
- `post_list`: Displays a list of all posts.
- `post_details`: Displays details of a specific post along with its associated notes.
- `post_new`: Form to create a new post.
- `post_edit`: Form to edit an existing post.
- `post_delete`: Deletes a specified post.

### Notes Views
- `note_list`: Displays a list of all notes associated with a specific post.
- `note_detail`: Displays details of a specific note.
- `note_new`: Form to create a new note.
- `note_edit`: Form to edit an existing note.
- `note_delete`: Deletes a specified note.

## Running Tests
To run the tests for this project, use the following command:
```sh
python manage.py test
```

<h2>Credits</h2>
<h3> Author: Dimpal Kaware </h3>
<h3>Repository: https://github.com/Dimplektech</h3>
