# -*- coding: utf-8 -*-
from flask import Blueprint
route_api = Blueprint( 'api_page',__name__ )
from web.controllers.api.Test import *


@route_api.route("/")
def index():
    return "Api V1.0~~"