# Bitlinks
Make your links shorter.    
If you send the bitlink then you'll receive how many times this bitlink was used to get access to the site. If you send the initial link (not bitlink) then you'll receive the bitlink as a response.

## Brief install
Python3 should already be installed. Use pip3 to install dependencies:
`pip3 install -r requirements.txt`

## Quick start
1. Get your token from API section of `bitly.com`.
2. Create file `.env` with the following content:      
`BITLY_TOKEN = ...` <-- paste your token there
3. Launch this script with the bash command: `python3 bitly.py <your_link>`

## Examples
In example below we provide some links that could be processed:
```python
<<< python3 bitly https://google.com   
Bitlink: bit.ly/3CrgtY5
<<< python3 bit.ly/3CrgtY5
Number of redirects from your bitly link: 5
```

## Project goals
This code is written for educational purposes.