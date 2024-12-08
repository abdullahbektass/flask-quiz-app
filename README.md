# Flask Quiz App

Flask Quiz App is a web-based application that allows users to sign up, log in, and participate in quizzes. Users can also add new questions and track their high scores.

## Features

- **User Authentication**: Secure signup, login, and logout functionality.
- **Quiz Functionality**: Users can attempt quizzes and see their scores.
- **Add Questions**: Authenticated users can add new questions to the quiz pool.
- **High Score Tracking**: Each user's highest score is tracked and displayed.
- **MongoDB Integration**: Uses MongoDB for storing user and question data.

## Prerequisites

- Python 3.7 or higher
- MongoDB
- Virtual environment (recommended)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/abdullahbektass/flask-quiz-app.git
   cd flask-quiz-app
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your MongoDB instance and update the MongoDB URI in your configuration file.

5. Run the application:

   ```bash
   flask run
   ```

## Folder Structure

```
flask-quiz-app/
│
├── routes.py               # Defines application routes and logic
├── models.py               # Contains User and Question models
├── templates/              # HTML templates for rendering pages
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   ├── add_question.html
│   ├── score.html
│
├── static/                 # Static assets (CSS, JS, Images)
├── __init__.py             # Initializes Flask app and extensions
└── requirements.txt        # Python dependencies
```

## Routes

### `/`
- **Method**: GET
- **Description**: Displays the home page with a list of questions. Requires authentication.

### `/signup`
- **Method**: GET, POST
- **Description**: Allows users to create an account.

### `/login`
- **Method**: GET, POST
- **Description**: Authenticates users and logs them into the application.

### `/logout`
- **Method**: GET
- **Description**: Logs out the current user.

### `/add_question`
- **Method**: GET, POST
- **Description**: Allows authenticated users to add new quiz questions.

### `/score`
- **Method**: POST
- **Description**: Submits quiz answers, calculates the score, and updates the high score if applicable.

## Technologies Used

- **Backend**: Flask, Flask-Login, Flask-Bcrypt
- **Database**: MongoDB
- **Frontend**: HTML, CSS (Bootstrap)
- **Other Libraries**: `bson` for ObjectId handling

## Future Enhancements

- Add categories for quiz questions.
- Implement real-time multiplayer quiz functionality.
- Add support for question images or multimedia.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
