from backend import get_model
from flask import Blueprint, current_app, request
import json

crud = Blueprint('crud', __name__)

@crud.route('/')
def index():
    return 'crud index'
