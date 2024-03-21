#! /usr/bin/env python
import requests
def main():
    result = requests.get('https://www.howsmyssl.com/a/check').json()
    version = result['tls_version']
    rating = result['rating']

    if version < "TLS 1.2":
        url = "https://pyfound.blogspot.com/2017/01/time-to-upgrade-your-python-tls-v12.html"
        print("Error: The Stripe API requires TLS version 1.2, you are running {version}"
              "\n\nPlease see {url}\nfor instructions to update your environment.".format(
                  version=version, url=url))
        exit(1)
    print("TLS 1.2 supported; no action required.")
    print("Rating is ", rating)

if __name__ == "__main__":
    main()
