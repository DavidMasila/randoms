from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for

class Controller(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def not_auth(self):
        return "You are not Authorized to access this page"
    
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login'))