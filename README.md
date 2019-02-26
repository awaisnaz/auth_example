### AWS Sig v4 authorization example

#### Prerequisites

* Python 3.6 or higher

#### Install

```bash
$ pip install -r requirements.txt
```

#### Usage

You will need to acquire below values by contacting Lucidtech

* API key (<api_key>)
* AWS Access Key Id (<access_key_id>)
* AWS Secret Access Key (<secret_access_key>)
* API Endpoint Prefix (<endpoint_prefix>)

Note: Your REST API endpoint might not have support for all prediction types

Invoice prediction:

```bash
$ python src/main.py https://<endpoint_prefix>.api.lucidtech.ai/v1 <api_key> <access_key_id> <secret_access_key> invoice_prediction invoice.pdf application/pdf
$ python src/main.py https://<endpoint_prefix>.api.lucidtech.ai/v1 <api_key> <access_key_id> <secret_access_key> invoice_prediction invoice.jpeg image/jpeg
```

Receipt prediction:

```bash
$ python src/main.py https://<endpoint_prefix>.api.lucidtech.ai/v1 <api_key> <access_key_id> <secret_access_key> receipt_prediction receipt.pdf application/pdf
$ python src/main.py https://<endpoint_prefix>.api.lucidtech.ai/v1 <api_key> <access_key_id> <secret_access_key> receipt_prediction receipt.jpeg image/jpeg
```

Document split:

```bash
$ python src/main.py https://<endpoint_prefix>.api.lucidtech.ai/v1 <api_key> <access_key_id> <secret_access_key> document_split document.pdf application/pdf
```
