# Smart Vending Machine 🥤🍫

A highly logical and structured Smart Vending Machine simulation system built in Python using **Object-Oriented Programming (OOP)** principles. This application mimics a real-world electronic vending machine, handling real-time item tracking, currency validation, and automated change calculations.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML).
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Learning Data Structures & Algorithms (DSA) and data science libraries like **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Dynamic Inventory Tracking:** Manages a variety of items (Snacks, Drinks) with unique codes, prices, and available stock counts.
*   **Cash/Coin Validation:** Accepts and counts simulated currency inserted by the user, ensuring the total covers the selected item's cost.
*   **Smart Change Return Logic:** Automatically calculates and returns the precise balance/change owed to the user after a successful purchase.
*   **Out-of-Stock Alerts:** Prevents users from selecting an empty slot and displays real-time stock status messages.
*   **Transaction Processing:** Dispenses the product only after validating both the user's cash input and the item's availability.

---

## 🛠️ OOP Concepts Implemented

This project focuses on state transitions, encapsulation, and clean data workflows:
*   **Classes & Objects:** Structured around modular classes such as `Item`, `VendingMachine`, and `CoinSlot`.
*   **Encapsulation:** Protects internal cash reservoirs, total earnings, and exact stock numbers using private attributes, exposing them only via secure class methods.
*   **Composition:** The main `VendingMachine` class aggregates multiple `Item` objects, demonstrating a clean system design.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd smart-vending-machine
    ```
3.  **Run the application:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   Python 3.x installed on your machine.
