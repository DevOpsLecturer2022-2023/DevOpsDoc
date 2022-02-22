# app.py

import boto3

from flask import Flask, jsonify, request
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

def create_table(table_name):
    """
    A description of the function
    
    :param param1: explanation of param1
    :type param1: state the parameter type
    :param param2: explanation of param2
    :type param2: state the parameter type
    
    :return: state what is returned by the function
    :rtype: the type(s) of the return value(s)
    """
    pass
