# Simple Python HTTP Server

This project is a basic local web server built using Python's built-in tools. It serves a fun welcome page, handles custom name greetings using website links, and shows an error page for any invalid links.

## Features

* **Built-in Tools**: Runs completely on Python without installing extra libraries.
* **Custom Welcome Page**: Displays a moving marquee text on the main homepage.
* **Dynamic Greetings**: Reads your name from the web link to show a personalized message.
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
  * Displays the moving marquee welcome message.
* **Personalized Homepage**: `http://localhost:8000/homepage?name=YourName`
  * Greets you dynamically! For example, `http://localhost:8000/homepage?name=Elvis` will say **\*Welcome Elvis!\***. 
  * If you just go to `http://localhost:8000/homepage`, it defaults to **\*Welcome Guest!\***.
* **Invalid Pages**: `http://localhost:8000/other_page_not_in_path`
  * Returns a `404 Error:Page Not Found` message.
