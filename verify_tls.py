#! /usr/bin/env python3

import requests


def main():
    version = requests.get('https://www.howsmyssl.com/a/check').json()['tls_version']
    if version < "TLS 1.2":
        url = "https://pyfound.blogspot.com/2017/01/time-to-upgrade-your-python-tls-v12.html"
        print("Error: The Stripe API requires TLS version 1.2, you are running {version}"
              "\n\nPlease see {url}\nfor instructions to update your environment.".format(
                  version=version, url=url))
        exit(1)
    print("TLS 1.2 supported; no action required.")


if __name__ == "__main__":
    main()
