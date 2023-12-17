from flask import request, redirect, render_template, abort, url_for, current_app
from flask import Blueprint


mainBp = Blueprint('mainBp', __name__)

@mainBp.route('/terms-of-use')
def termsOfUse():
    return render_template('main/termsOfUse.html', title='terms of use Page')

@mainBp.route('/privacy-policy')
def privacyPolicy():
    return render_template('main/privacyPolicy.html', title='Privacy Policy Page')

@mainBp.route('/robots.txt')
def robots():
    return open('./app'+url_for('static', filename='robots.txt'), 'r').read()