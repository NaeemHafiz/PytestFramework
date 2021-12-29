import os

# def date_time():
# date_time_stamp = "{:%Y%m%d_%H%H_}".format(date_time.datetime.now())
# return date_time_stamp

# BASE URL CONFIGURATION FILE
CONFIG_FILE = "../configurations/url.ini"
# VARIABLE TO GET CURRENT DATE TIME STRING VALUE
# d_t = (date_time())

# JSON_FILE_PATH = os.path.absolute(os.path.dirname("../configurations/"))
# CONFIG FILE PATH
CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'url.ini')

# ReqREs End Points


GET_USER_LIST_END_POINT_URL = "users"
GET_SINGLE_USER_END_POINT_URL = "users/2"
GET_SINGLE_USER_NOT_FOUND_END_POINT_URL = "users/23"
GET_LIST_RESOURCE_END_POINT_URL = "unknown"
GET_SINGLE_RESOURCE_END_POINT_URL = "unknown/2"
GET_SINGLE_RESOURCE_NOT_FOUND_END_POINT_URL = "unknown/23"
CREATE_USER_END_POINT_URL = "users"
UPDATE_SINGLE_USER_END_POINT_URL = "users/2"
DELETE_SINGLE_USER_END_POINT_URL = "users/2"
REGISTER_SINGLE_USER_END_POINT_URL = "register"
LOGIN_SUCCESSFUL_USER_END_POINT_URL = "login"
DELAYED_RESPONSE_END_POINT_URL = "users?delay=3"
