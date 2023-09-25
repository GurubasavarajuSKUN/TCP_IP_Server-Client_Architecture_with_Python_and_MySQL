# TCP_IP_Server-Client_Architecture_with_Python_and_MySQL

## Overview

This project demonstrates a simple yet robust TCP/IP server-client architecture implemented in Python. It allows for efficient communication between a server and multiple clients, utilizing socket programming for network communication and MySQL for database interaction.

## Features

- **Dynamic Configuration:** Server and client IP addresses and port numbers are fetched from XML configuration files, making it easy to adapt to different network setups.
  
- **Query Response:** The server handles various client queries and responds appropriately. It's designed to be extensible, allowing for the addition of new query types with minimal code changes.

- **Database Integration:** The server can connect to a MySQL database and retrieve data based on client requests. This integration showcases the power of combining network programming with database management.

## Prerequisites

Before running this project, ensure you have the following dependencies installed:

- Python 3.x
- MySQL Server
- Required Python packages (specified in `requirements.txt`)

## Setup

1. Clone this repository to your local machine using `git clone`.

2. Configure the server and client XML files with the appropriate IP addresses and port numbers for your environment.

3. Install the required Python packages using `pip install -r requirements.txt`.

4. Run the server and client Python scripts to establish a connection.

## Usage

1. Start the server by running `server.py`. It will listen for incoming client connections.

2. Run `client.py` on a separate machine or terminal to connect to the server.

3. Use the client to send queries to the server, which will process and respond accordingly.

## Database Integration

- To configure database connection details, edit the `config.ini` file in the `server` directory.

- Create a MySQL database and import the provided `schema.sql` to set up the required tables.

- The server can execute SQL queries on the database, and the client can request data retrieval from the server.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## Acknowledgments

We would like to thank the open-source community for their valuable contributions and the developers of Python, MySQL, and the various libraries used in this project.
