# BearRobotics_OA

# Simple ATM Controller

This project implements a simple ATM controller system. The controller facilitates basic ATM operations, including inserting a card, verifying a PIN, selecting an account, and performing transactions such as viewing balance, depositing, and withdrawing funds.

## Features

- **Card Insertion:** Simulates the insertion of an ATM card.
- **PIN Verification:** Verifies the entered PIN using a mock bank interface.
- **Account Selection:** Supports multiple accounts per user.
- **Transactions:**
  - View Balance
  - Deposit
  - Withdraw
- **Simplifications:**
  - Balances are represented as integers (no cents).
  - No real hardware integration for cash bins or card readers.

---

## Future Integration

This code is structured to facilitate future integrations, including:
- **Bank System:** For fetching account information and transaction updates.
- **ATM Hardware:** For handling card readers and cash bins.

---

## Implementation Details

- **Classes:**
  - `ATMController`: Handles the flow and operations of the ATM.
  - `BankSystem`: Simulates a bank API for PIN verification and account management.
  - `Account`: Represents individual user accounts.

- **Testing:** The controller includes unit tests for validating its core functionalities without relying on external systems.

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/alexjaegook/BearRobotics_OA.git
