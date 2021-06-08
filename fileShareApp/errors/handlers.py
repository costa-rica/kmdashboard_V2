from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
	return render_template('errors/404.html'), 404 #must specify for this 

#flask has default , 200 at end of return render_... so no need to do in other routes

@errors.app_errorhandler(403)
def error_403(error):
	print(error)
	return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_500(error):
	return render_template('errors/500.html'), 500

@errors.app_errorhandler(502)
def error_502(error):
	return render_template('errors/502.html'), 502
    
@errors.app_errorhandler(504)
def error_504(error):
	return render_template('errors/504.html'), 504

@errors.app_errorhandler(Exception)
def unhandled_exception(error):
	return render_template('errors/504.html'), 504