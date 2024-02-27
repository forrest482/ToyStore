# Django Toy Store Project

This repository contains the Django project for a toy store, which includes a blog, an online store, a shopping cart, and a payment system. This project is structured into four main Django apps: `blog`, `store`, `cart`, and `payment`.

## Features

- **Blog**: Allows users to read and comment on blog posts.
- **Store**: Users can browse through toy categories and products.
- **Cart**: Users can add products to their shopping cart and manage cart items.
- **Payment**: Integrates a simple payment system to process transactions.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Django 3.2 or higher
- Other dependencies listed in `requirements.txt`

### Installation

1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/forrest482/ToyStore.git
   ```

2. Navigate to the project directory:
   ```sh
   cd toystore
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply the migrations to create the database schema:
   ```sh
   python manage.py migrate
   ```

5. Run the development server:
   ```sh
   python manage.py runserver
   ```

6. Open a web browser and navigate to `http://127.0.0.1:8000/` to view the project.

## Usage

- Access the **Blog** section to read and comment on posts.
- Visit the **Store** to explore toy categories and products.
- Add products to your **Cart** and review them before proceeding to checkout.
- Use the **Payment** system to simulate transactions for your purchases.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
