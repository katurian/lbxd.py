from setup import *

def postEntryComment(code, comment):
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "POST"
    url = f'https://api.letterboxd.com/api/v0/log-entry/{code}/comments?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    body = {'comment':comment}
    body = json.dumps(body)
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode(body)]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    r = requests.post(f'https://api.letterboxd.com/api/v0/log-entry/14JSU7/comments?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', headers={'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': bearertoken}, data=body, verify=False)

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

def logFilm(code, review, rating, spoilers, rewatched, date, liked, tags):
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "POST"
    url = f'https://api.letterboxd.com/api/v0/log-entries?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    body = {'rating': rating, 'review':{'containsSpoilers': spoilers, 'text': review}, 'diaryDetails':{'rewatch': rewatched, 'diaryDate': date}, 'like': liked, 'filmId': code, 'tags':tags}
    body = json.dumps(body)
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode(body)]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    r = requests.post(f'https://api.letterboxd.com/api/v0/log-entries?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', headers={'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': bearertoken}, data=body, verify=False)
     
def getReviewsByTag(tagger, query):
    query = query.replace(" ", "%20")
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/log-entries?tagger={tagger}&sort=WhenAdded&where=HasReview&includeTaggerFriends=None&tagCode={query}&perPage=300&apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    
    r = requests.get(f'https://api.letterboxd.com/api/v0/log-entries?tagger={tagger}&sort=WhenAdded&where=HasReview&includeTaggerFriends=None&tagCode={query}&perPage=300&apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    return resultJSON
    
