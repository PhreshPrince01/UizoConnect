Usizo connect

This project is a platform where users can register, log in, create health-related campaigns, or donate to existing campaigns. It provides secure user authentication, campaign management, and file uploads, organized through Flask’s blueprint architecture and utilizing Flask-Login for session handling

Table of Contents

    Getting Started
    Features
    Project Structure
    Routes and Endpoints
    Forms and Models
    Running the Application
    Contributing
    License

Getting Started
Prerequisites

    Python 3.x: Ensure Python is installed. You can download it from python.org.
    Flask & Dependencies: Install dependencies via requirements.txt.

Installation

    Clone the repository:

    bash

git clone <repository-url>

Navigate to the project directory:

bash

cd <project-directory>

Install required dependencies:

bash

    pip install -r requirements.txt

    Configure the application by creating a config.py file with database connection details and other configurations.

Features

    User Registration and Login: New users can register, and existing users can log in.
    Campaign Management: Users can create, view, and manage their campaigns.
    File Uploads: Users can upload documents for campaign verification.
    Secure Authentication: User passwords are securely hashed.

Project Structure

    run.py: Application entry point.
    app/__init__.py: Contains the application factory function create_app() and initializes extensions.
    app/routes.py: Defines routes for user and campaign-related functionalities.
    app/models.py: Defines the database models (User and Campaign).
    app/forms.py: Contains form classes for registration, login, and campaign creation.
    templates/: HTML templates for rendering views.
    static/: CSS and static files for styling.

Routes and Endpoints
User Authentication

    /register: Register a new user account.
    /login: Log in to an existing user account.
    /logout: Log out of the current session.

Campaign Management

    /campaign: Create a new campaign.
    /donate: View campaigns associated with the current user.
    /payment-method: Display payment options for a selected campaign.
    /welcome: User welcome page post-login.
    /: Application homepage.

Forms and Models
Forms

    RegistrationForm: Handles user registration with email and password fields.
    LoginForm: Manages user login credentials.
    CampaignForm: Collects details for creating a campaign, including campaign name, description, and document uploads.

Models

    User: Manages user data (email, password, and registration date).
    Campaign: Stores campaign information, including name, description, fund target, and associated user ID.

Running the Application

    Start the Flask development server:

    bash

    python run.py

    Access the application by navigating to http://127.0.0.1:5000 in a web browser.

Contributing

    Fork the project.
    Create a new branch (git checkout -b feature-branch).
    Commit your changes (git commit -m 'Add feature').
    Push to the branch (git push origin feature-branch).
    Open a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.


