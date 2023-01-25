from flask import Blueprint, request, jsonify

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def llamarServiciosSet():
    global user,passw
    ##try:
    user =request.json['user']
    passw =request.json['passw']

    print("username",user)
    print("password",passw)

    #inicializarVariables(categoryId)
    