# ImageGen: AI Image Generator
##Overview
ImageGen is a Django-based web application that allows users to generate images from text
prompts using a Stable Diffusion model. The application leverages Celery for asynchronous task
processing, enabling the parallel generation of images. Users can either input custom prompts or
generate images using a set of default prompts.

## Features
- Generate images from custom text prompts.
- Generate images from three default prompts in parallel.
- View the latest generated images on the homepage.
- Store and retrieve image generation data, including the prompt, image (in Base64), seed, and creation time.


## Project Structure:
```
ImageGen/
├── ImageGen/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── api/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── tasks.py
│   ├── Image_call.py
│   ├── urls.py
│   ├── tests.py
├── templates/
│   ├── home.html
├── static/
│   ├── css/
│   │   ├── styles.css
├── manage.py
├── celery.py
└── README.md
```
# Installation

## Prerequisites
- Python 3.x
- Django 4.x
- Redis (for Celery)
- Celery
- Stable Diffusion API Access

## Setup
- ## Clone the Repository:

```
git clone https://github.com/yourusername/ImageGen.git
cd ImageGen
```
- ## Create a Virtual Environment and Install Dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- ## Set Up Django:

1. ### Create a .env file in the project root with the following variables:
```
  SECRET_KEY=your_secret_key
  DEBUG=True
  ALLOWED_HOSTS=localhost
  REDIS_URL=redis://localhost:6379/0
  STABLE_DIFFUSION_API_KEY=your_api_key
```
2. ### Apply migrations:

```
  python manage.py migrate
```
3. ### Create a superuser (optional for admin access):
```
  python manage.py createsuperuser
```
- ## Start Redis:

Make sure Redis is running on your machine:
```
redis-server
```
- ## Start Celery:

Run Celery to handle asynchronous tasks:
```
celery -A ImageGen worker --loglevel=info
```

- ## Run the Django Development Server:
```
python manage.py runserver
```

- ## Access the Application:

Open your browser and go to http://localhost:8000/.

## Usage

## Generate Custom Image
- Enter your custom prompt in the text box.
- Click on "Generate Image."
- The generated image will be displayed below the form.
## Generate Default Images
- Click on "Generate Default Images."
- The images for the default prompts will be displayed on the page but not saved to database.
## View Latest Images
- The latest 5 generated images are always displayed at the top of the page.

## Testing
To run the test cases, use the following command:
```
python manage.py test
```
Tests are located in api/tests.py, and they cover various aspects of the application, including image generation, storage, and retrieval.

## Troubleshooting:
- Error generating image: string indices must be integers, not 'str': This error may occur if the API response is incorrectly formatted. Check the API key and ensure the Stable Diffusion service is working properly.

- Image not displaying instantly: If the image does not display immediately after generation, it could be a timing issue. Ensure Celery tasks are completing successfully, and check the console for any errors.

- Running Celery in windows can get Tricky. Use eventlet if errors persist.
  ```
  celery -A ImageGen worker -l info -P eventlet
  ```
License
This project is licensed under the MIT License. See the LICENSE file for details.
