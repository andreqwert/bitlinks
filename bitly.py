import requests
from environs import Env
import argparse


def parse_args():
    """Parse arguments from input"""

    parser = argparse.ArgumentParser(description='Making links shorter')
    parser.add_argument('-l', '--link', help='Link which you would like to make shorter')
    args = parser.parse_args()
    return args


def shorten_link(token, link):
    """Make bitlink from link (= make link shorter)"""
    
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }    

    payload = {
        'long_url': link
    }

    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response_post = requests.post(url, headers=headers, json=payload)
    response_post.raise_for_status()

    bitlink = response_post.json().get('id')
    return bitlink


def count_bitlink_clicks(token, bitlink):
    """Count number of clicks for bitlink"""

    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }

    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    clicks_num = response.json().get('total_clicks')
    return clicks_num


def is_bitlink(token, link):
    """Check if link is a bitlink."""

    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }

    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    
    args = parse_args()
    env = Env()
    env.read_env()
    token = env('BITLY_TOKEN')
    try:
        if is_bitlink(token, args.link):
            clicks_num = count_bitlink_clicks(token, args.link)
            print(f'Number of redirects from your bitly link: {clicks_num}')
        else:
            print('Bitlink:', shorten_link(token, args.link))
    except requests.exceptions.HTTPError:
        print('Your input link or token is incorrect.')


if __name__ == '__main__':
    main()




