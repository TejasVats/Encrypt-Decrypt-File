# File Encryptor

A simple Python script to **encrypt and decrypt files** using symmetric key encryption via the [cryptography](https://cryptography.io/) library.

## Features

- Generate a secure secret key and save it to disk (**do not share or commit this key**)
- Encrypt any file in-place using strong symmetric encryption (Fernet/AES)
- Decrypt previously-encrypted files in-place
- Minimal and user-friendly interface

## Requirements

- Python 3.6+
- cryptography

Install using pip:

## Usage

### 1. Key Generation

First, generate a new secret key.  
**This key will be saved as `secret.key`. You must keep it safe!**

Uncomment and run:

Or in the terminal:

This will create a `secret.key` file in your working directory.

### 2. Encrypt a File

Uncomment and modify:

Replace `FILENAME` with the path to your file.  
Example:

Or run from the terminal with `encrypt_file` uncommented in your script.

### 3. Decrypt a File

Uncomment and modify:
Replace `FILENAME` with the path to your encrypted file.  
Example:

Or run from the terminal with `decrypt_file` uncommented.

- ## How it Works

- Calls `write_key()` once to generate and save an encryption key.
- The same key in `secret.key` is loaded to encrypt/decrypt any files.
- Uses symmetric encryption (the same key for both encrypt and decrypt).

## Contribution

Pull requests are welcome!  
For feature requests or questions, open an issue.

## Disclaimer

This tool is for educational use. For production, always follow advanced security best practices.
