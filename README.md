# 🔎 Python Port Scanner

A simple and lightweight **TCP Port Scanner** written in Python.

This project was created to learn and practice **Python, networking, sockets, IP addresses, DNS resolution, and port scanning**.

> ⚠️ **Disclaimer:** This tool is intended for educational purposes and authorized security testing only. Do not scan systems or networks without permission.

---

## 📌 Features

* 🔍 Scan TCP ports on a target host
* 🌐 Resolve domain names to IP addresses
* ⚡ Fast port scanning
* 🧵 Support for concurrent scanning
* 📊 Display open ports
* 🐍 Written entirely in Python
* 🧠 Useful for learning basic network security concepts

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

## 🐍 Sc_port.py

`Sc_port.py` is the basic version of the port scanner.

It uses Python's `socket` module to try connecting to ports on the target machine.

Example:

```bash
python Sc_port.py
```

The program asks for a target and scans the specified ports.

---

## ⚡ Sc_port_fast.py

`Sc_port_fast.py` is an optimized version of the scanner.

It uses **concurrent scanning** to check multiple ports at the same time, making the scanning process faster than the basic version.

Run it with:

```bash
python Sc_port_fast.py
```

---

## 🛠️ Technologies

* **Python 3**
* `socket`
* `threading` / concurrency
* DNS resolution
* TCP networking

---

## 🌐 How Port Scanning Works

A port represents a communication endpoint on a device.

For example:

| Port | Common Service |
| ---- | -------------- |
| 22   | SSH            |
| 53   | DNS            |
| 80   | HTTP           |
| 443  | HTTPS          |
| 3306 | MySQL          |

The scanner attempts to establish a TCP connection to each port.

If the connection succeeds, the port is considered **open**.

```text
Target
  │
  ├── Port 22  → Open
  ├── Port 80  → Open
  ├── Port 443 → Open
  ├── Port 8080 → Closed
  └── ...
```

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

Go to the scanner directory:

```bash
cd Scan-Port
```

Run the scanner:

```bash
python Sc_port.py
```

Or use the faster version:

```bash
python Sc_port_fast.py
```

---

## 💻 Requirements

Python 3.x

Check your Python version:

```bash
python --version
```

No external Python packages are required.

---

## 📚 What I Learned

This project helped me practice:

* Python functions
* Variables and data types
* Loops
* Exception handling
* User input
* `socket` programming
* IP addresses
* DNS resolution
* TCP connections
* Network ports
* Concurrency
* Basic network security concepts
* Git and GitHub

---

## 🔐 Legal & Ethical Use

This project is designed for **learning and authorized security testing**.

Only scan:

* Your own computer
* Your own servers
* Your own lab/network
* Systems for which you have explicit permission to perform security testing

Unauthorized port scanning may violate laws, policies, or terms of service.

---

## 🔮 Future Improvements

Possible future features:

* [ ] Custom port ranges
* [ ] Scan multiple targets
* [ ] Service detection
* [ ] Banner grabbing
* [ ] Better error handling
* [ ] Command-line arguments
* [ ] Export scan results
* [ ] Improved concurrent scanning
* [ ] Progress indicator
* [ ] Timeout configuration

---

## 👨‍💻 Author

**Hatim Hansal**

GitHub:

https://github.com/hatimhansal

---

## ⭐ Project

If you find this project useful for learning, feel free to ⭐ the repository.
