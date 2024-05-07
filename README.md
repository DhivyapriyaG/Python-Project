# Flight Booking System

This is a flight booking system implemented in Python. It allows users to sign up, sign in, book tickets, check ticket status, cancel tickets, and view/print bills. There are two main user roles: passengers and cashiers.

## Features

- **Passenger**
  - Sign up for a new account.
  - Sign in to an existing account.
  - Book tickets for desired destinations and classes (Business/Economic).
  - Check the status of booked tickets.
  - Cancel booked tickets.
  - View and print bills.

- **Cashier**
  - Log in to manage ticket approvals and cancellations.
  - View a list of booked tickets.
  - Approve pending tickets.
  - Cancel booked tickets.

## How It Works

The system is divided into several classes:

- `pa_det`: Represents passenger details and functionalities.
- `Book_det`: Manages available tickets and passenger bookings.
- `b_list`: Maintains a list of booked tickets.
- `Tic_det`: Stores ticket prices and details.

### Main Functions

- **Passenger Functions:**
  - `passenger()`: Handles passenger sign up, sign in, booking, ticket status check, cancellation, and bill viewing.
  
- **Cashier Functions:**
  - `cashier()`: Manages cashier login, ticket approval, cancellation, and ticket list viewing.

## Usage

1. Clone this repository to your local machine.
2. Run the `flightbooking.py` file using a Python interpreter.
3. Follow the prompts to navigate through the system as either a passenger or a cashier.

## Requirements

- Python 3.x

## Contributors

- Dhivyapriya G ([link-to-profile](https://github.com/DhivyapriyaG)) - Role Developer 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
