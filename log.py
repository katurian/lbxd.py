from setup import *

def getEntryInfo(code):
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/log-entry/{code}?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    r = requests.get(f'https://api.letterboxd.com/api/v0/log-entry/{code}?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    return resultJSON

def getEntryComments(code):
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/log-entry/{code}/comments?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    r = requests.get(f'https://api.letterboxd.com/api/v0/log-entry/{code}/comments?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    return resultJSON

def getEntryStats(code):
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/log-entry/{code}/statistics?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    r = requests.get(f'https://api.letterboxd.com/api/v0/log-entry/{code}/statistics?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    return resultJSON
