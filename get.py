def getGenres():
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/films/genres?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    signing_bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), signing_bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    
    r = requests.get(f'https://api.letterboxd.com/api/v0/films/genres?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    print(resultJSON)

def getFilms():
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/films?apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    signing_bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), signing_bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    
    r = requests.get(f'https://api.letterboxd.com/api/v0/films?apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    print(resultJSON)

def searchFilms(query):
    query = query.replace(" ", "%20")
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/search?include=FilmSearchItem&perPage=10&searchMethod=FullText&input={query}&apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    signing_bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), signing_bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    
    r = requests.get(f'https://api.letterboxd.com/api/v0/search?include=FilmSearchItem&perPage=10&searchMethod=FullText&input={query}&apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    print(resultJSON)

def searchReviews(query):
    query = query.replace(" ", "%20")
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/search?include=ReviewSearchItem&perPage=10&searchMethod=FullText&input={query}&apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    signing_bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), signing_bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    
    r = requests.get(f'https://api.letterboxd.com/api/v0/search?include=ReviewSearchItem&perPage=10&searchMethod=FullText&input={query}&apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    print(resultJSON)

def searchLists(query):
    query = query.replace(" ", "%20")
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/search?include=ListSearchItem&perPage=10&searchMethod=FullText&input={query}&apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    signing_bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), signing_bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    
    r = requests.get(f'https://api.letterboxd.com/api/v0/search?include=ListSearchItem&perPage=10&searchMethod=FullText&input={query}&apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    print(resultJSON)
