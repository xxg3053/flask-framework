# -*- coding: utf-8 -*-
from flask import Blueprint

route_user = Blueprint( 'user',__name__ )

@route_user.route("/")
def index():
    return "Hello User"


