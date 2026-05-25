# LMS01 - Learning Management System

A Django-based Learning Management System built with Python and SQLite. This project provides a complete platform for managing products, user authentication, and transactions.

## Features

- **User Authentication**: Sign up and login functionality with secure password management
- **Product Management**: Create, edit, and manage products with pricing
- **Product Transactions**: Track product sales with transaction history and quantity tracking
- **Contact Management**: Built-in contact form functionality
- **Responsive Design**: Mobile-friendly templates using HTML/CSS
- **Admin Dashboard**: Django admin interface for database management

## Tech Stack

- **Backend**: Django 6.0.4
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Python Version**: 3.x
- **Additional Libraries**:
  - asgiref
  - Pillow (image processing)
  - sqlparse
  - tzdata

## Project Structure

```
LMS01/
├── app/                    # Main application module
│   ├── models.py          # Data models
│   ├── views.py           # View logic
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin configuration
│   ├── templates/         # HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   └── contact.html
│   └── migrations/        # Database migrations
├── myauth/                # Authentication app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── login.html
│   │   └── signup.html
│   └── migrations/
├── product/               # Product management app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── templates/
│   │   ├── add_product.html
│   │   ├── edit_product.html
│   │   ├── buy_product.html
│   │   ├── product.html
│   │   ├── error_404.html
│   │   └── error_500.html
│   └── migrations/
├── project/               # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py           # Main URL configuration
│   ├── wsgi.py           # WSGI configuration
│   └── asgi.py           # ASGI configuration
├── static/                # Static files (CSS, JS)
│   ├── assets/
│   ├── js/
│   └── my_css/
│       └── styles.css
├── media/                 # User uploaded files
│   ├── contact/
│   └── products/
├── env/                   # Python virtual environment
├── manage.py             # Django management script
├── db.sqlite3            # SQLite database
└── README.md             # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository** (if applicable)
   ```bash
   git clone <repository-url>
   cd LMS01
   ```

2. **Create and activate virtual environment**
   ```bash
   # On Windows
   python -m venv env
   env\Scripts\activate
   
   # On macOS/Linux
   python -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or manually install the required packages:
   ```bash
   pip install Django==6.0.4
   pip install Pillow==12.2.0
   pip install asgiref
   pip install sqlparse
   pip install tzdata
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (admin account)
   ```bash
   python manage.py createsuperuser
   ```

## Usage

### Running the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

### Access the Admin Panel

```
http://127.0.0.1:8000/admin
```

Log in with the superuser credentials created during setup.

### Main Pages

- **Home**: `http://127.0.0.1:8000/` - Main landing page
- **About**: `http://127.0.0.1:8000/about/` - About page
- **Contact**: `http://127.0.0.1:8000/contact/` - Contact form
- **Login**: `http://127.0.0.1:8000/login/` - User login
- **Sign Up**: `http://127.0.0.1:8000/signup/` - New user registration
- **Products**: `http://127.0.0.1:8000/products/` - Product listing and management

## Database Models

### App Models
- Core application data models

### Authentication Models (myauth)
- User authentication and profile management

### Product Models (product)
- **Product**: Product information with pricing and user association
- **ProductTransactions**: Transaction records with quantity and user tracking

## Development

### Create Migrations
After modifying models:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Tests
```bash
python manage.py test
```

### Collect Static Files
```bash
python manage.py collectstatic
```

## Media Files

User-uploaded files are stored in the `media/` directory:
- `media/contact/` - Contact form uploads
- `media/products/` - Product images and files

## Security Notes

- Keep `SECRET_KEY` in `settings.py` secure
- Use environment variables for sensitive configuration
- Set `DEBUG = False` in production
- Update `ALLOWED_HOSTS` for production deployment

## Deployment

For production deployment:

1. Update `DEBUG = False` in `settings.py`
2. Configure allowed hosts
3. Set up a production database (PostgreSQL recommended)
4. Use a production web server (Gunicorn, uWSGI)
5. Configure HTTPS and SSL certificates
6. Set up static and media file serving

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is provided as-is. Add appropriate license information as needed.

## Support

For issues or questions, please create an issue in the repository.

---

**Last Updated**: May 2026
