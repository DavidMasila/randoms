from app import app
from app.models import migrate, db

if __name__ == "__main__":
        app.run(debug=True)