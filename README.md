# Feel

Bitcoin Wallet Creation Example

## Description

This repository demonstrates how to create a Bitcoin wallet using the `bitcoinlib` library with support for different witness types (legacy, segwit, p2tr).

## Requirements

- **Python**: 3.7 or higher
- **Platform**: Compatible with Windows, macOS, and Linux
- **Dependencies**: bitcoinlib library (automatically installed via pip)

## Installation

### Quick Install
```bash
pip install bitcoinlib>=0.6.14
```

Or install from the requirements file:
```bash
pip install -r requirements.txt
```

## Usage

Run the wallet creation script:
```bash
python create_wallet.py
```

This will create a new random Bitcoin wallet with segwit support and display:
- The Bitcoin address
- The WIF (Wallet Import Format) private key
- The mnemonic seed phrase (BIP39)

## Features

- Creates a new random Bitcoin wallet
- Supports multiple witness types: 'legacy', 'segwit', 'p2tr'
- Displays wallet address, private key, and mnemonic seed phrase

## Security Warning

⚠️ **IMPORTANT**: This is an example/demonstration script. Never share your private keys or mnemonic seed phrases. Store them securely and never commit them to version control.