#  Python Port Scanner

A simple **TCP Port Scanner written in Python** for learning network programming, sockets, DNS resolution, and basic cybersecurity concepts.

The project contains two versions of the scanner:

* `Sc_port.py` — basic port scanner
* `Sc_port_fast.py` — faster version using concurrent scanning

> ⚠️ **Disclaimer:** This project is for educational purposes and authorized security testing only. Never scan systems or networks without permission.

---

## 📌 Features

* 🔍 Scan TCP ports
* 🌐 Accept a hostname or IP address
* 🔄 Resolve hostnames to IP addresses
* 📡 Test TCP connections
* 🟢 Detect open ports
* ⚡ Faster scanning with concurrency
* 🐍 Uses Python's standard library
* 💻 Works from the terminal

---

## 📂 Project Structure

```text
python-port-scanner/
│
├── Scan-Port/
│   ├── Sc_port.py
│   └── Sc_port_fast.py
│
└── README.md
```

---

## 🐍 Basic Scanner

### `Sc_port.py`

This is the basic implementation of the port scanner.

It uses Python's `socket` module to attempt TCP connections to ports on the target.

If a connection can be established, the port is reported as open.

Run it with:

```bash
python Sc_port.py
```

---

## ⚡ Fast Scanner

### `Sc_port_fast.py`

This version improves the scanning speed by checking multiple ports concurrently.

Run it with:

```bash
python Sc_port_fast.py
```

The idea is:

```text
Basic Scanner

Port 1 → Scan
          ↓
Port 2 → Scan
          ↓
Port 3 → Scan
          ↓
Port 4 → Scan


Fast Scanner

Port 1 → Scan ─┐
Port 2 → Scan ─┤
Port 3 → Scan ─┤ → Results
Port 4 → Scan ─┘
```

---

## 🌐 How It Works

The scanner follows a simple process:

```text
        Target
          │
          ▼
   Hostname / IP
          │
          ▼
    DNS Resolution
          │
          ▼
   TCP Connection
          │
      ┌───┴───┐
      │       │
   Success   Failed
      │       │
      ▼       ▼
    OPEN    CLOSED
```

For example:

| Port | Common Service |
| ---- | -------------- |
| 22   | SSH            |
| 53   | DNS            |
| 80   | HTTP           |
| 443  | HTTPS          |
| 3306 | MySQL          |

The scanner does **not** exploit these services. It only checks whether a TCP connection can be established.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/hatimhansal/python-port-scanner.git
```

Enter the project:

```bash
cd python-port-scanner
```

Enter the scanner directory:

```bash
cd Scan-Port
```

Run the basic scanner:

```bash
python Sc_port.py
```

Or run the faster version:

```bash
python Sc_port_fast.py
```

---

## 💻 Requirements

* Python 3.x
* No external Python packages are required.

Check your Python version:

```bash
python --version
```

---

## 🧠 Concepts Practiced

This project helped me practice:

* Python functions
* Variables
* Loops
* Conditions
* Exception handling
* User input
* `socket`
* TCP connections
* IP addresses
* DNS resolution
* Network ports
* Concurrent scanning
* Basic network security
* Git and GitHub

---

## 🔮 Future Improvements

Possible improvements for future versions:

* [ ] Custom port ranges
* [ ] Command-line arguments
* [ ] Scan multiple targets
* [ ] Service detection
* [ ] Banner grabbing
* [ ] Configurable timeout
* [ ] Better error handling
* [ ] Export results to a file
* [ ] Progress indicator
* [ ] Better scan statistics
* [ ] IPv6 support

---

## 🔐 Ethical Use

This tool should only be used against systems that you own or have explicit permission to test.

Good targets for learning include:

```text
127.0.0.1
localhost
Your own virtual machines
Your own lab network
CTF / authorized training environments
```

Unauthorized scanning can violate laws, security policies, or terms of service.

---

## 👨‍💻 Author

**Hatim Hansal**

GitHub:

https://github.com/hatimhansal

---

## ⭐ Project

If this project helped you learn Python networking or cybersecurity fundamentals, feel free to ⭐ the repository.
