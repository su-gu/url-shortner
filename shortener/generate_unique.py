import hashlib
from database_init import db
from models import Link
from datetime import date, datetime

def generate_unique(long_url,len=7):
    unique_str = str(hashlib.md5(long_url.encode()).hexdigest())[:len]
    link = Link.query.filter_by(shorten_url=unique_str).first()
    if link != None and link.original_url != long_url:
        return generate_unique(long_url+datetime.now())
    return unique_str