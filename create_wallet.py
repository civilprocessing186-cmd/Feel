#!/usr/bin/env python3
"""
Bitcoin Wallet Creation Example using bitcoinlib

This script demonstrates how to create a new Bitcoin wallet with segwit support.
"""

from bitcoinlib.wallets import Wallet, wallet_delete
from bitcoinlib.mnemonic import Mnemonic

# Wallet name
wallet_name = 'my_temp_wallet'

# Delete wallet if it already exists
try:
    wallet_delete(wallet_name, force=True)
except:
    pass  # Wallet doesn't exist, which is fine

# Generate a new mnemonic (seed phrase)
mnemonic = Mnemonic().generate()

# Create a new random wallet; options for witness_type: 'legacy', 'segwit', 'p2tr'
w = Wallet.create(wallet_name, keys=mnemonic, witness_type='segwit')
key = w.get_key()  # first derived key
print("Address:", key.address)
print("WIF (private key):", key.wif)
print("Mnemonic (seed phrase):", mnemonic)
