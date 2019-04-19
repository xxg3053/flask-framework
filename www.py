# -*- coding: utf-8 -*-
from application import app


'''
统一拦截处理和统一错误处理
'''
from web.interceptors.ErrorInterceptor import  *

'''
蓝图功能，对所有的url进行蓝图功能配置
'''

from web.controllers.index import route_index
from web.controllers.static import route_static
from web.controllers.api import route_api

from web.controllers.user.User import route_user




app.register_blueprint( route_index,url_prefix = "/" )
app.register_blueprint( route_static,url_prefix = "/static" )
app.register_blueprint( route_api,url_prefix = "/api" )

app.register_blueprint( route_user,url_prefix = "/user" )
