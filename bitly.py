import requests
from environs import Env


def shorten_link(token, link):
    """Make bitlink from link (= make link shorter)"""
    
    headers = {
        'Authorization': 'Bearer {}'.format(str(token))
    }    

    payload = {
        'long_url': link
    }

    response_get = requests.get(link)
    response_get.raise_for_status()

    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response_post = requests.post(url, headers=headers, json=payload)
    response_post.raise_for_status()

    bitlink = response_post.json().get('id')
    return bitlink


def count_clicks(token, bitlink):
    """Count number of clicks for bitlink"""

    headers = {
        'Authorization': 'Bearer {}'.format(str(token))
    }

    payload = {
        'units': -1,
        'unit': 'day',
    }

    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    return response


def is_bitlink(token, link):
    """Check if link is a bitlink."""

    headers = {
        'Authorization': 'Bearer {}'.format(str(token))
    }

    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
    response = requests.get(url, headers=headers)
    if response.ok:
        return True
    else:
        return False


def main():
    env = Env()
    env.read_env()
    token = env('TOKEN')
    link = input('Введите ссылку: ')
    try:
        if is_bitlink(token, link):
            total_clicks = count_clicks(token, link).json().get('total_clicks')
            print(f'По ссылке прошли {total_clicks} раз(а)')
        else:
            print('Битлинк', shorten_link(token, link))
    except requests.exceptions.SSLError:
        print('Link is invalid.')
        exit()


if __name__ == '__main__':
    main()





