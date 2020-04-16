from setup import *

def searchFilms(query):
    query = query.replace(" ", "%20")
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/search?include=FilmSearchItem&perPage=10&searchMethod=FullText&input={query}&apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    
    r = requests.get(f'https://api.letterboxd.com/api/v0/search?include=FilmSearchItem&perPage=10&searchMethod=FullText&input={query}&apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    return resultJSON

def searchReviews(query):
    query = query.replace(" ", "%20")
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/search?include=ReviewSearchItem&perPage=10&searchMethod=FullText&input={query}&apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    
    r = requests.get(f'https://api.letterboxd.com/api/v0/search?include=ReviewSearchItem&perPage=10&searchMethod=FullText&input={query}&apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    return resultJSON

def searchLists(query):
    query = query.replace(" ", "%20")
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/search?include=ListSearchItem&perPage=10&searchMethod=FullText&input={query}&apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    
    r = requests.get(f'https://api.letterboxd.com/api/v0/search?include=ListSearchItem&perPage=10&searchMethod=FullText&input={query}&apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    return resultJSON
