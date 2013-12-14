from flask import render_template, session
from models import User, Section, SystemProperty, MC
import markdown
from Feather import app

#: Markdown filter
@app.template_filter()
def md_to_html(content):
    return markdown.markdown(content)

#: This file does all non-admin routing
#: Place all routes here

#: It is recommended for cleanliness that all templates for these
#: routes go into the templates/public/ folder

####: Start Editing

#: Static files (keep dict structure intact)
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

#: Render function (this must return always return a view)
def render_public_template(template, title, args):
    return render_template(template,
        title = title,
        sysname = SystemProperty.get('name'),
        site = site,
        args = args)

#: Routes
@app.route('/')
def public_homepage():
    return render_public_template(
        'public/test.html',
        'HomePage',
        {
            'sections': Section.get_all()
        }
    )

####: Stop Editing