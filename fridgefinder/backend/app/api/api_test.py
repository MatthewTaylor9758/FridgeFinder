# 'http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3'
from flask import Blueprint, Flask, request

api_test = Blueprint('tests', __name__)

@api_test.route('/')
def test_api():
    req = requests.get('http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3')
    res = req.json()
    print(res)