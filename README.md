# Python Security Tools 🔐

A collection of small cybersecurity tools built using Python.

## Tools Included

### 1. Password Strength Checker

This tool evaluates the strength of a password based on:

- Length (minimum 8 characters)
- Uppercase and lowercase letters
- Numbers
- Special characters

## How It Works

The user inputs a password, and the script analyzes it using regex patterns to determine its strength.

## Example

Input:
password123

Output:
Moderate ⚠️

## Use Case

Useful for improving password security and understanding how strong passwords are evaluated in real systems.


### 2. IP Reputation Checker

Checks whether an IP address is flagged as malicious based on a predefined blacklist.

## Example

Input:
192.168.1.10

Output:
Malicious ❌
