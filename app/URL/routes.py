from flask import Flask, url_for, render_template, abort, Blueprint, redirect, request
from app.models import *
from .forms import *
from .helpers import *


urlBp = Blueprint('urlBp', __name__)


@urlBp.route('/', methods=['GET', 'POST'])
def home():
    URLform = addURLForm()
    if URLform.validate_on_submit():
        link = URLform.URL.data
        check = URL.query.filter_by(url=link).first() 
        if check == None:
            short = URLSHORT()
            newURL = URL(
                ip=request.remote_addr,
                url=link,
                url_short=short,
            )
            db.session.add(newURL)
            db.session.commit()

            return redirect(url_for('urlBp.cheakout', urlshort=short))

    return render_template('URL/home.html', title='Home Page | URL Short', URLform=URLform)


@urlBp.route('/cheakout/<string:urlshort>')
def cheakout(urlshort):
    return render_template('URL/cheakout.html', 
                           title='cheakout | URL Short', 
                           urlshort=urlshort,
                           link=URL.query.filter_by(url_short=urlshort).first().url
                           )


@urlBp.route('/out/<string:url_short>')
def redirecting(url_short):
    result = URL.query.filter_by(url_short=url_short).first()
    # print(result)
    if result == None:
        return redirect(url_for('urlBp.home'))
    else:
        result.count = result.count + 1
        db.session.add(ips(
            urlID=result.id,
            ip=request.remote_addr,
            info=str(request.headers)
        ))

        db.session.commit()
        return redirect(result.url)


@urlBp.route('/myLinks')
def myLinks():
    allLinks = URL.query.filter_by(ip=request.remote_addr).all()
    return render_template('URL/myLinks.html', title='My Links | URL Short', allLinks=enumerate(allLinks))


@urlBp.route('/delete/<int:ID>')
def delete(ID):
    reselt = URL.query.filter_by(id=ID, ip=request.remote_addr).first()
    if reselt != None:
        db.session.delete(reselt)
        db.session.commit()
        return redirect(url_for('urlBp.myLinks'))
    return redirect(url_for('urlBp.myLinks'))
