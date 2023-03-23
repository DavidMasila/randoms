from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_principal import Principal, Permission, RoleNeed

admin = Admin()
db=SQLAlchemy()
migrate = Migrate()

principal = Principal()

admin_role = RoleNeed('admin')
user_role = RoleNeed('user')
admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))