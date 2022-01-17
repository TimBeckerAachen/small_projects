#!/usr/bin/env python
import requests


if __name__ == '__main__':
    payload = {
        'text': 'Hello world!'
    }

    url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
    response = requests.post(url=url, json=payload)
    print(response.json())
