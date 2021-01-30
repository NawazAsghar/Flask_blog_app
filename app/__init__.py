from flask import Flask

app = Flask(__name__, template_folder= 'tamplats')

# from app import data_base
from app import Admin
from app import Public
