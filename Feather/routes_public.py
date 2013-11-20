from models import User, Section, SystemProperty, MC
from Feather import app

#: This file does all non-admin routing
#: Place all routes here

#: It is recommended for cleanliness that all templates for these
#: routes go into the templates/public/ folder

####: Start Editing

#: Static files
site = {
	'css': {
		'header': [],
		'footer': []
	},
	'js': {
		'header': [],
		'footer': []
	}
}

#: Render function
def render_public_template(template, title, args):
	return render_template(template,
		title = title,
		sysname = SystemProperty.get('name'),
		site = site,
		args = args)

#: Routes
@app.route('/')
def public_homepage():
	return '''
	<h1>Feather is working</h1>
	Update 'routes_public.py' to start playing<br />
	or <a href="/admin/login">log in</a> to the admin area.
	'''

####: Stop Editing