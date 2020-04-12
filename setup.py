import hashlib
import hmac
import json
import logging
import os
import time
import uuid
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

apikey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
apisecret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
