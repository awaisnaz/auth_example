import argparse
import json
import requests

from urllib.parse import urlparse
from auth import AWSSignatureV4


def create_auth(args):
    return AWSSignatureV4(
        region='eu-west-1',
        service='execute-api',
        aws_access_key=args.access_key_id,
        aws_secret_key=args.secret_access_key,
        aws_api_key=args.api_key
    )


def main(args):
    auth = create_auth(args)
    uri = urlparse(f'{args.api_endpoint}/documents')
    body = json.dumps({'contentType': 'image/jpeg', 'consentId': '1234'}).encode()

    auth_headers = auth.sign_headers(
        uri=uri,
        method='POST',
        body=body
    )

    headers = {**auth_headers, 'Content-Type': 'application/json'}

    post_documents = requests.post(
        url=uri.geturl(),
        headers=headers,
        data=body
    ).json()

    print(post_documents)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('api_endpoint')
    parser.add_argument('api_key')
    parser.add_argument('access_key_id')
    parser.add_argument('secret_access_key')
    args = parser.parse_args()

    main(args)
