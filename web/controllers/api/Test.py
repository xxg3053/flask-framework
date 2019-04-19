from web.controllers.api import route_api
from common.libs.Helper import *

@route_api.route("/test")
def test():
    return success('test')
