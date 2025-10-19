# Inventory Management API

## Overview
This project is a Django REST Framework API that helps users manage inventory items, categories, and stock levels.  
It includes user authentication, CRUD operations for items and categories, and inventory tracking features.

## Features
- User authentication and token-based access
- CRUD operations for inventory items
- Category management
- Inventory level tracking and history
- Pagination and filtering support

## Tech Stack
- Django
- Django REST Framework
- SQLite (Development)
- PostgreSQL (Production)
- Heroku / PythonAnywhere (Deployment)

## Setup Instructions
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/inventory-management-api.git

# Navigate to folder
cd inventory-management-api

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
