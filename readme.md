# Notification Preferences API

## Project Description

This project provides REST APIs to manage user notification preferences. Users can view and update their notification preferences, including frequency and channels (email, push, SMS).

## Setup Instructions

1. Clone the repository https://github.com/anirbanchakraborty123/Notification_Service.git

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
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

- `GET /api/v1/notification-types/`: List all notification types.
- `POST /api/v1/notification-types/`: Create a new notification type.

### Notification Preferences

- `GET /api/v1/notification-preferences/`: List all notification preferences.
- `POST /api/v1/notification-preferences/`: Create a new notification preference.
- `GET /api/v1/notification-preferences/<id>/`: Retrieve a notification preference.
- `PUT /api/v1/notification-preferences/<id>/`: Update a notification preference.
- `DELETE /api/v1/notification-preferences/<id>/`: Delete a notification preference.

## Testing the APIs

You can use tools like `curl`, Postman, or any API client to test the endpoints.
