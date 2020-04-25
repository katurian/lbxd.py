from setup import *

def postListComment(code, comment):
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "POST"
    url = f'https://api.letterboxd.com/api/v0/list/{code}/comments?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    body = {'comment':comment}
    body = json.dumps(body)
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode(body)]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    r = requests.post(f'https://api.letterboxd.com/api/v0/list/{code}/comments?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', headers={'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': bearertoken}, data=body, verify=False)

def getListInfo(code):
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/list/{code}?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    r = requests.get(f'https://api.letterboxd.com/api/v0/list/{code}?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    return resultJSON

def getListComments(code):
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/list/{code}/comments?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    r = requests.get(f'https://api.letterboxd.com/api/v0/list/{code}/comments?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    return resultJSON

def getListEntries(code):
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/list/{code}/entries?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    r = requests.get(f'https://api.letterboxd.com/api/v0/list/{code}/entries?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    return resultJSON

def getListStats(code):
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/list/{code}/statistics?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    r = requests.get(f'https://api.letterboxd.com/api/v0/list/{code}/statistics?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    return resultJSON

def createList(name, description, entries, tags, ranked):
    entrieslist = []
    count = 1
    for entry in entries:
        entriesdict = {
            "rank":    count,
            "containsSpoilers": False,
            "film":  entry,
        }
        count = count + 1
        entrieslist.append(entriesdict)
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "POST"
    url = f'https://api.letterboxd.com/api/v0/lists?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    body = {"published":True,"tags":tags,"name":name,"entries":entrieslist,"ranked":ranked,"description":description}
    body = json.dumps(body)
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': bearertoken}
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode(body)]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    r = requests.post(f'https://api.letterboxd.com/api/v0/lists?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', headers=headers, data=body, verify=False)
