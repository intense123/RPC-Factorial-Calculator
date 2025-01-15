# RPC Factorial Calculator

A simple client-server application demonstrating Remote Procedure Call (RPC) functionality. The client can request a server to calculate the factorial of a number, and the server responds with the result. Additionally, the server supports direct user input for factorial calculations.

## Features

- **RPC Communication**: The client sends requests to the server for factorial calculations.
- **Interactive Server**: The server also allows direct user input for calculations.
- **Scalable Design**: Supports easy addition of new methods.

## How It Works

1. The **server** listens for RPC requests and processes them.
2. The **client** sends a method invocation request (e.g., `factorial(5)`).
3. The server computes the result and sends it back to the client.
4. The server also supports user input for on-the-spot calculations.

## Getting Started

### Prerequisites

- Python 3.6 or above
- Basic understanding of RPC communication

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rpc-factorial-calculator.git
   cd rpc-factorial-calculator
