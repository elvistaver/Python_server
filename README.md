# Simple Python HTTP Server

This project is a basic local web server built using Python's built-in tools. It serves a fun welcome page, handles custom name greetings using web links, and includes a signup form that processes user submissions.

## Features

* **Built-in Tools**: Runs completely on Python without installing extra libraries.
* **Custom Welcome Page**: Displays a moving marquee text on the main homepage.
* **Dynamic Greetings**: Reads your name from the web link to show a personalized message.
* **HTML Form Handling**: Serves an interactive HTML form and processes submitted data using **POST requests**.
* **Error Handling**: Sends a clear 404 "Page Not Found" message for invalid links.

## Prerequisites

You only need **Python 3** installed on your computer to run this project.

## How to Setup and Run

Follow these easy steps to get your server running:

1. **Save the Code**: Copy the Python code and save it in a file named `server.py`.
2. **Open Terminal**: Open your command line, terminal, or command prompt.
3. **Navigate to Folder**: Move into the folder where you saved your file (e.g., `cd path/to/folder`).
4. **Start the Server**: Run the following command:
   ```bash
   python3 server.py
   ```

## Server Routes and How to View

Open your web browser and test these links:

* **Main Page**: `http://localhost:8000/` 
  * Displays the moving marquee welcome message (**GET**).
* **Personalized Greeting**: `http://localhost:8000/welcome?name=YourName`
  * Greets you dynamically (**GET**)! For example, `http://localhost:8000/welcome?name=Elvis` will say `*Welcome Elvis!*`. 
  * If you go to `http://localhost:8000/welcome` without a query, it defaults to `*Welcome Guest!*`.
* **Interactive Signup Form**: `http://localhost:8000/homepage`
  * Displays a text input form where you can enter a name and press submit (**GET**).
* **Form Processing**: `http://localhost:8000/submit_signup`
  * Receives data submitted from the homepage form (**POST**) and returns a customized `Hello YourName!` confirmation message.
* **Invalid Pages**: `http://localhost:8000/any_other_page`
  * Returns a `404 Error:Page Not Found` message.
