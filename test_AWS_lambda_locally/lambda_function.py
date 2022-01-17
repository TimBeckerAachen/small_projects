#!/usr/bin/env python


def lambda_handler(event, context):
    text = event['text']
    print(text)
    return text
