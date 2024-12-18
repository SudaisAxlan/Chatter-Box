from flask import Blueprint
from Module import sngup, modules,login,CreateNotes,home,SendMessage

# routes = Blueprint("routes", __name__)

routes=Blueprint("routes",__name__)

routes.add_url_rule("/",view_func=home.home)
routes.add_url_rule("/sendMessage",view_func=SendMessage.sendMessage,methods=['POST'])
# routes.add_url_rule("/",view_func=modules.homes)
# routes.add_url_rule("/createnotes",view_func=CreateNotes.CreateNotes,methods=['POST'])
routes.add_url_rule("/register",view_func=sngup.userRegister,methods=['POST'])
routes.add_url_rule("/login",view_func=login.login,methods=['POST'])

