from setup import *

def getMe():
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/me?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    
    r = requests.get(f'https://api.letterboxd.com/api/v0/me?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', headers={'Authorization': bearertoken}, verify=False)
    resultJSON = r.json()
    return resultJSON
    
