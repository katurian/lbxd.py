from setup import *

def getContributor(code):
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/contributor/{code}?sort=FilmPopularity&perPage=20&apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
 
    r = requests.get(f'https://api.letterboxd.com/api/v0/contributor/{code}?sort=FilmPopularity&perPage=20&apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    return resultJSON


def getContributions(code):
    nonce = uuid.uuid4()
    timestamp = int(time.time())
    method = "GET"
    url = f'https://api.letterboxd.com/api/v0/contributor/{code}/contributions?sort=FilmPopularity&perPage=20&apikey={apikey}&nonce={nonce}&timestamp={timestamp}'
    bytestring = b"\x00".join(
        [str.encode(method), str.encode(url), str.encode("")]
    )
    signature = hmac.new(
        str.encode(apisecret), bytestring, digestmod=hashlib.sha256
    )
    signature = signature.hexdigest()
    
    r = requests.get(f'https://api.letterboxd.com/api/v0/contributor/{code}/contributions?sort=FilmPopularity&perPage=20&apikey={apikey}&nonce={nonce}&timestamp={timestamp}&signature={signature}', verify=False)
    resultJSON = r.json()
    return resultJSON


