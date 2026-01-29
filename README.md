# Python Port-Scanner

This project is a simple TCP port scanner written in Python. It scans a target host for open ports within a specified range using socket connections.

The tool is intended for educational and learning purposes to demonstrate basic networking concepts and socket programming.

## Overview

The port scanner attempts to connect to each port in a given range on a target host. If a connection is successful, the port is considered open and is reported to the user.

This project helps illustrate how services listen on ports and how basic reconnaissance tools work at a low level.

## Features

- Scans a target IP address or hostname
- User defined port range
- Identifies open TCP ports
- Simple and readable implementation using Python sockets

## Requirements

- Python 3.x
- No external libraries required

## Usage

Run the script from the terminal:

```bash
python3 port_scanner.py
