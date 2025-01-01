import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# db_folder = os.path.join(os.path.dirname(BASE_DIR), 'new')
# db_path = os.path.join(os.path.dirname(BASE_DIR), 'new', 'demo.db')

# if not os.path.exists(db_folder):
#     print(f"Directory does not exist. Creating directory: {db_folder}")
#     os.makedirs(db_folder, exist_ok=True)
    
class Config:
    # print(db_path)
    SECRET_KEY = os.environ.get('SECRET_KEY') or "KEYSSS"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', f'sqlite:///{db_path}')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///demo.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False