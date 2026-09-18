#!/usr/bin/env python3
# Simple IoT ECC Encryption System
# This demonstrates a basic implementation of ECC for IoT device communication

import base64
import hashlib
import os
import time
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# --- DEVICE IDENTITY SETUP ---
class IoTDevice:
    def __init__(self, device_id):
        """Initialize an IoT device with a unique ID and generate its ECC key pair"""
        self.device_id = device_id
        # Generate ECC key pair using the P-256 curve (also known as secp256r1)
        self.private_key = ec.generate_private_key(ec.SECP256R1())
        self.public_key = self.private_key.public_key()
        print(f"Device {device_id} initialized with ECC key pair")

# --- SECURE COMMUNICATION ---
def encrypt_message(message, key):
    """Encrypt a message using AES-GCM with the derived key"""
    # Generate a random initialization vector, this meaans the encrypted data will never bee the same twice
    iv = os.urandom(12)
    
    # Create an encryptor object
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv)
    ).encryptor()
    
    # Add device ID as associated data for authentication
    encryptor.authenticate_additional_data(b"IoT_Device")
    
    # Encrypt the message
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    
    # Get the authentication tag
    tag = encryptor.tag
    
    # Return IV, ciphertext, and tag as a single payload
    return {
        'iv': base64.b64encode(iv).decode(),
        'ciphertext': base64.b64encode(ciphertext).decode(),
        'tag': base64.b64encode(tag).decode(),
        'timestamp': int(time.time())
    }

def decrypt_message(encrypted_payload, key):
    """Decrypt a message using AES-GCM with the derived key"""
    # Decode the components from the payload
    iv = base64.b64decode(encrypted_payload['iv'])
    ciphertext = base64.b64decode(encrypted_payload['ciphertext'])
    tag = base64.b64decode(encrypted_payload['tag'])
    
    # Create a decryptor object
    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag)
    ).decryptor()
    
    # Add device ID as associated data for authentication
    decryptor.authenticate_additional_data(b"IoT_Device")
    
    # Decrypt the message
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    return plaintext.decode()

# --- DEMO FUNCTIONALITY ---
def simulate_iot_communication():
    """Simulate a simple IoT communication between a device and server"""
    # Create an IoT device and server
    device = IoTDevice("temp_sensor_001")
    server_private_key = ec.generate_private_key(ec.SECP256R1())
    server_public_key = server_private_key.public_key()
    
    # Key exchange happens directly now - bypassing serialization/deserialization
    print("\n--- PERFORMING KEY EXCHANGE ---")
    
    # Device derives a key using the server's public key
    shared_secret = device.private_key.exchange(ec.ECDH(), server_public_key)
    device_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,  # 256-bit key for AES-256
        salt=None,
        info=b'IoT Encryption Key'
    ).derive(shared_secret)
    
    # Server derives the same key using the device's public key
    server_shared_secret = server_private_key.exchange(ec.ECDH(), device.public_key)
    server_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'IoT Encryption Key'
    ).derive(server_shared_secret)
    
    # Verify both parties have the same key
    print(f"Device key: {device_key.hex()[:10]}...")
    print(f"Server key: {server_key.hex()[:10]}...")
    print(f"Keys match: {device_key == server_key}")
    
    # Encrypt a message from the device
    print("\n--- ENCRYPTING SENSOR DATA ---")
    sensor_data = '{"temperature": 22.5, "humidity": 45, "battery": 87}'
    encrypted_data = encrypt_message(sensor_data, device_key)
    print(f"Original data: {sensor_data}")
    print(f"Encrypted data: {encrypted_data}")
    
    # Decrypt the message on the server
    print("\n--- DECRYPTING SENSOR DATA ---")
    decrypted_data = decrypt_message(encrypted_data, server_key)
    print(f"Decrypted data: {decrypted_data}")

if __name__ == "__main__":
    simulate_iot_communication()