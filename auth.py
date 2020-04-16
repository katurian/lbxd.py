from setup import * 

def generateToken(username, password):
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "POST"
    url = f'https://api.letterboxd.com/api/v0/auth/token?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    body = f'grant_type=password&username={username}&password={password}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode(body)]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    r = requests.post(f'https://api.letterboxd.com/api/v0/auth/token?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', headers={'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}, data=f'grant_type=password&username={username}&password={password}', verify=False)
    resultJSON = r.json()
    accesstoken = resultJSON['access_token']
    refreshtoken = resultJSON['refresh_token']
    tokens = [accesstoken, refreshtoken]
    return tokens

def refreshToken():
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "POST"
    url = f'https://api.letterboxd.com/api/v0/auth/token?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    body = f'grant_type=refresh_token&refresh_token={refreshtoken}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode(body)]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    r = requests.post(f'https://api.letterboxd.com/api/v0/auth/token?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', headers={'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}, data=f'grant_type=refresh_token&refresh_token={refreshtoken}', verify=False)
    resultJSON = r.json()
    return resultJSON

def checkUsername(username):
    username = username.replace(" ", "%20")
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/auth/username-check?username={username}&apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    r = requests.get(f'https://api.letterboxd.com/api/v0/auth/username-check?username={username}&apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    return resultJSON
    


