from ctypes import resize
from flask import Blueprint, request, redirect, Response, render_template
from database_init import db
from models import Link
from generate_unique import generate_unique
import json

BASE_URL = "http://localhost:5000/"
short = Blueprint('short', __name__)

@short.route('/add_link', methods=['POST'])
def add_link():
    original_link = request.get_json()['original_link']
    shorten_url=generate_unique(original_link)
    response = json.dumps(
        {
            "original": original_link,
            "shorten" : BASE_URL+shorten_url
        }
    )
    if Link.query.filter_by(shorten_url=shorten_url).first() != None:
        return Response(response, 201)
    link = Link(original_url=original_link, shorten_url=shorten_url)
    db.session.add(link)
    db.session.commit()

    return Response(response, 201)


@short.route('/<short_url>')
def redirect_to(short_url):
    link = Link.query.filter_by(shorten_url=short_url).first()
    if link == None:
        return("<h1>Invalid short URL</h1>")
    link.views += 1
    db.session.commit()

    return redirect(link.original_url)


@short.route('/<short_url>/stats')
def total_views(short_url):
    link = Link.query.filter_by(shorten_url=short_url).first()
    if link == None:
        return Response("Invalid short URL", 404)
    response = json.dumps(
        {
            "original": link.original_url,
            "shorten" : BASE_URL+link.shorten_url,
            "views"   : link.views,
            "date created" : str(link.date_created)
        }
    )
    return Response(response, 200)