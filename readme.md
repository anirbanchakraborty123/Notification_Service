# Notification Preferences API

## Project Description

This project provides REST APIs to manage user notification preferences. Users can view and update their notification preferences, including frequency and channels (email, push, SMS).

## Setup Instructions

1. Clone the repository.
2. Install the dependencies:
    ```sh
    pip install django djangorestframework
    ```
3. Run the migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
4. Run the development server:
    ```sh
    python manage.py runserver
    ```

## API Endpoints

### Notification Types

- `GET /api/notification-types/`: List all notification types.
- `POST /api/notification-types/`: Create a new notification type.

### Notification Preferences

- `GET /api/notification-preferences/`: List all notification preferences.
- `POST /api/notification-preferences/`: Create a new notification preference.
- `GET /api/notification-preferences/<id>/`: Retrieve a notification preference.
- `PUT /api/notification-preferences/<id>/`: Update a notification preference.
- `DELETE /api/notification-preferences/<id>/`: Delete a notification preference.

## Testing the APIs

You can use tools like `curl`, Postman, or any API client to test the endpoints.
