from distutils.debug import DEBUG
from email.mime import application
from sre_constants import SUCCESS
from unittest import result
from flask import Flask, Response, send_file, request, jsonify
from flask_jwt_extended import *
import bcrypt
import json
import socket
import random, string
from requests import get
import mysqlDB as mDB
from curd import *
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt
from secret import *

app = Flask (__name__)




if __name__ == "__main__":
    app.run()