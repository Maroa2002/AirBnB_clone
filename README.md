# Airbnb Clone Project

## Overview

This project aims to deploy a simplified version of the Airbnb website on your server, emphasizing fundamental concepts in the higher-level programming track. Over a span of 4 months, the development will lead to a comprehensive web application consisting of:

1. **Command Interpreter**
   - A command-line interface (CLI) for manipulating data without a visual interface. This is particularly useful for development and debugging purposes.

2. **Front-end Website**
   - A dynamic and static website that showcases the final product to users. This component will serve as the user interface for interacting with the application.

3. **Data Storage (Database or Files)**
   - Implementation of a data storage system, whether it be a database or file-based, to store and manage objects/data related to the application.

4. **API (Application Programming Interface)**
   - An API that establishes a communication interface between the front-end and the data storage. This API will facilitate operations such as data retrieval, creation, deletion, and updating.

## Project Structure

The project is structured into distinct modules, each serving a specific purpose:

- **Command Interpreter**
  - Located in the `command_interpreter` directory, this module contains the command-line interface for developers to manipulate and interact with the data.

- **Front-end Website**
  - The web application's user interface resides in the `front_end` directory. This includes both static and dynamic components to provide a seamless experience for end-users.

- **Data Storage**
  - The `data_storage` directory houses the implementation of the data storage system, be it a database or file-based, for efficient management of application data.

- **API**
  - The `api` directory contains the API implementation responsible for mediating communication between the front-end and the data storage. This includes functionalities for CRUD operations.

## Getting Started

To set up and run the Airbnb clone on your server, follow these steps:

1. **Clone the Repository**
   ```
   git clone https://github.com/your-username/airbnb-clone.git
   ```

2. **Navigate to Project Directory**
   ```
   cd airbnb-clone
   ```

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```
   python console.py
   ```

   Ensure that you configure the necessary settings for the database or file storage system in the `config.py` file.

