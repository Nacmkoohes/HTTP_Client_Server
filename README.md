# HTTP Client and Server (Socket Programming)

A minimal **HTTP client** and **HTTP server** implemented using **low-level TCP sockets in Python**.  
This project demonstrates how HTTP communication works internally, without relying on high-level networking libraries.

---

## 📖 Overview

The project consists of two programs:

- **`webclient.py`**  
  A simple HTTP client that connects to a server, sends an HTTP/1.1 GET request, and prints the full HTTP response.

- **`webserver.py`**  
  A basic HTTP server that listens for incoming connections, reads HTTP request headers, and responds with a fixed HTTP response.

Both programs communicate using **HTTP/1.1 over TCP sockets**.

---

## 🎯 Learning Objectives

- Understand **TCP socket programming**
- Learn the structure of **HTTP requests and responses**
- Work with **byte streams** using `sendall()` and `recv()`
- Correctly handle **partial receives**
- Understand **client–server interaction**
- Practice **command-line programs** and Git/GitHub workflow

---

## 🚫 Restrictions

To ensure a low-level understanding of networking, the following are **not used**:

- `socket.create_connection()`
- `socket.create_server()`
- `urllib` or any other HTTP helper libraries

Only the core `socket` API is used.

---

## 🗂 Project Structure

HTTP_Client_Server/


├── webclient.py # HTTP client

├── webserver.py # HTTP server

├── README.md

└── .gitignore

