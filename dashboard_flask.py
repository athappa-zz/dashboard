#Flask tutorial
import rescuetime_api as api
import os

#import the Flask class from the flask module
#import the render_template class from the flask module
from flask import (
	Flask,
	abort,
	flash,
	redirect,
	render_template,
	request,
	url_for,
)


app = Flask(__name__)

DEBUG = True

#displays a name if the variable is initialized
@app.route('/')
@app.route('/hello/<name>')
def hello(name='Andrew'):
	return render_template('hello.html', name=name)


@app.route('/about')
def about():
	return 'The about page'

@app.route("/blog")
def blog():
	result = api.download_rescuetime_json()
	return "%s" % result

if __name__ == "__main__":
	if os.environ.get("FLASK_TUTORIAL_DEBUG"):
		DEBUG = True
	print "Running in debug:", DEBUG
	app.run(debug=DEBUG)





'''




#You can dynamically pass in variable names
@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username
show_user_profile('andrew')


data, presentation, orm
django ships with its own orm
flask depends on third party


'''