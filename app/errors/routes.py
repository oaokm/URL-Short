from flask import Blueprint, render_template, request

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def page_not_found(e):
    backLastPage = request.headers.get('Referer', -1)
    if backLastPage == -1 : 
        backLastPage = None
    print(backLastPage)
    print(request.headers)
    return render_template('errors/404.html', 
                            title='Page Not Found | 404', 
                            meassgeError=e,
                            backLastPage=backLastPage
                            ), 404


@errors.app_errorhandler(403)
def Forbidden(e):
    return render_template('errors/403.html', title='Forbidden | 403', meassgeError=e), 403


@errors.app_errorhandler(400)
def bad_request(e):
    return render_template('errors/400.html', title='Bad Request | 400', meassgeError=e), 400

@errors.app_errorhandler(500)
def server_Error(e):
    return render_template('errors/500.html', title='Server Error | 500', meassgeError=e), 500

