# ⭐ Force-encryption

Fetch Star Wars data → Encrypt sensitive fields → Log and analyze!

---

## 🚀 Overview

**Force-encryption** is a Python project that retrieves Star Wars character data from the SWAPI API, encrypts sensitive fields (like `birth_year`), and logs the results for further analysis. It demonstrates secure data handling and modern Python practices.

---

## ✨ Features

- Fetches data from [SWAPI](https://swapi.dev/)
- Encrypts sensitive fields using a pluggable encryption utility
- Uses Python dataclasses for structured data
- Detailed logging for debugging and analytics
- Modular and extensible codebase

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/alexntelifilippidis/Force-encryption.git
cd Force-encryption
```

Install dependencies (use a virtual environment recommended):

```bash
pip install -r requirements.txt
```

---

## ⚡ Usage

Run the main script to fetch, encrypt, and log Star Wars data:

```bash
python src/main.py
```

You can configure logging and debug options in the code.

---

## 🧩 Project Structure

```
Force-encryption/
├── src/
│   ├── swapi_reader.py      # Fetches and processes SWAPI data
│   ├── crypto_utils.py      # Encryption utilities
│   ├── main.py              # Entry point
│   └── ...
├── tests/                   # Unit tests
├── requirements.txt
└── README.md
```

---

## 🔒 Encryption

Sensitive fields (e.g., `birth_year`) are encrypted using the `JSONKeyEncryptor` class before further processing. This ensures data privacy and security.

---

## 📝 License

MIT License

---

## 🤝 Contributing

Pull requests and issues are welcome! Please open an issue to discuss your ideas or report bugs.

---

May the source be with you! 🌌

