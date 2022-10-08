import requests
from environs import Env
from dotenv import load_dotenv
load_dotenv()


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
    env = Env()
    env.read_env()
    token = env('BITLY_TOKEN')
    link = input('Введите ссылку: ')
    try:
        if is_bitlink(token, link):
            clicks_num = count_bitlink_clicks(token, link)
            print(f'По ссылке прошли {clicks_num} раз(а)')
        else:
            print('Битлинк', shorten_link(token, link))
    except requests.exceptions.HTTPError:
        print('Вы ввели неправильную ссылку или неверный токен.')


if __name__ == '__main__':
    main()




