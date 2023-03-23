from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

class Controller(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def not_auth(self):
        return "You are not Authorized to access this page"