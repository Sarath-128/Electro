![Django](https://img.shields.io/badge/Python-blue)
![Uiverse](https://img.shields.io/badge/Uiverse-yellow)
![Stripe](https://img.shields.io/badge/Stripe-red)


# Electro - E-Commerce Website

![Screenshot 2024-11-13 183242](https://github.com/user-attachments/assets/187700e4-f17d-47da-99cd-626337010238)

**Electro** is a responsive and fully-featured e-commerce platform built with **Django**, **Stripe**, and **Uiverse**. It provides a seamless shopping experience for users across all devices, with secure payment processing and an intuitive user interface.

## Features

- **Responsive Design**: Optimized for mobile, tablet, and desktop views using Uiverse's customizable UI components.
- **User Authentication**: Secure user login and registration with password management.
  
 ![Screenshot 2024-11-13 183316](https://github.com/user-attachments/assets/b2eed7c8-6739-4e08-a3af-f09f2819771c)

- **Product Catalog**: Display products with images, descriptions, and prices.
  
 ![Screenshot 2024-11-13 183304](https://github.com/user-attachments/assets/f1dec617-c478-4c77-808c-4c1726bd0c86)

- **Shopping Cart**: Users can add, update, and remove items from their cart.
  
 ![Screenshot 2024-11-13 183513](https://github.com/user-attachments/assets/4d18b325-bc7f-46d4-8dbd-3159034cb887)

- **Secure Payments**: Integrated with Stripe for reliable and secure payment processing.
         **Note**: Use debit card number - 4242 4242 4242 4242. And other details are default
  
 ![Screenshot 2024-11-13 183528](https://github.com/user-attachments/assets/5970db56-2350-4a2c-ab7b-4c51187d580f)

-**After Successful Payment**: The quantity of the products decreases

![Screenshot 2024-11-13 183539](https://github.com/user-attachments/assets/f4cadec7-ba52-40bb-81fd-b66290da76d2)

- **Admin Panel**: Admins can manage products, orders, users, and more via Django's admin interface.
  
![Screenshot 2024-11-13 190603](https://github.com/user-attachments/assets/509e4fdb-e19e-48f3-b32a-ded5b5283b7b)

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: Uiverse UI Components
- **Payment Integration**: Stripe
- **Database**: SQLite (or PostgreSQL, depending on your configuration)

## Installation

### Prerequisites

Before you start, make sure you have the following installed:

- Python 3.12
- Stripe account (for payment gateway integration)
- Uiverse account (for UI components)

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/electro.git
