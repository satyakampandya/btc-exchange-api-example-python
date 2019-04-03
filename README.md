# btc-exchange-api-example-python
Simple python example of btc-exchange api

## Before start you should have:
* `API KEY`. If you don't have, please read "How to request API KEY"
* Your generated `private key`

## How to use
* `git clone https://github.com/satyakampandya/btc-exchange-api-example-python.git`
* `cd btc-exchange-api-example-python/`
* `pip install -r requirements.txt`
* `nano btc_api.py` and provide your's `API_KEY` and path of `PRIVATE_KEY`
* Run `python btc_api.py`

## How to request API KEY
Please generate RSA keypair with with your public and private key and send _public key_ to us (info@bitmarket.lt) asking to grant you `API KEY`. 

## How to generate RSA keypair
### Via Commandline: 
* `openssl genrsa -out btc-exchange-api.pem 2048`
* `openssl rsa -in btc-exchange-api.pem -outform PEM -pubout -out btc-exchange-api.public.pem`
* Send `btc-exchange-api.public.pem` to us

### Via Website:
* Open http://travistidwell.com/jsencrypt/demo/
* Change `Key Size` into 2048 and press `Generate New Keys`
* Save `private key` somewhere securely
* Save `public key` somewhere and send this file to us
