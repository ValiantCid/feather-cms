from flask import session, redirect, request
from .models import User, Section, SystemProperty, db
from Feather import app
from Feather.config import Config

#: DO NOT EDIT THIS FILE
#: This file contains all interface routes
#: You may break things


#: redirect any get requests to interface files to dashboard
@app.route('/interface/<task>/', methods=['get'])
def interface_reroute(task):
    return redirect('/admin/dashboard/')

#: do the system install if it's not already done
@app.route('/feather-install/<secret>')
@app.route('/interface/install/<secret>', methods=['get'])
def interface_install(secret):
    if secret == Config.INSTALL_CODE:
        db.create_all()
        sysname = SystemProperty('name', 'MyFeather', 0)
        mc_api_key = SystemProperty('mc_api_key', '', 0)
        mc_list_id = SystemProperty('mc_list_id', '', 0)
        admin = User('admin', 'password')
        sect = Section('default', 'Default', 'This is a section')
        db.session.add(sysname)
        db.session.add(mc_api_key)
        db.session.add(mc_list_id)
        db.session.add(sect)
        db.session.add(admin)
        db.session.commit()
        return redirect('/admin/login/?s=Feather%20is%20now%20installed')
    return """You need to run /feather-install/<install_key>
            where install key is the key you configured"""


#: login request
@app.route('/interface/login/', methods=['post'])
def interface_login():
    user = User.get(request.form['username'])
    sha_pass = User.hash_password(request.form['password'])
    if user is None:
        return redirect('/admin/login/?e=Bad%20username')
    if user.password != sha_pass:
        return redirect('/admin/login/?e=Bad%20password')
    session['user'] = user.username
    return redirect('/admin/dashboard/')


#: logout request
@app.route('/logout/')
@app.route('/interface/logout/', methods=['get'])
def interface_logout():
    session.pop('user')
    return redirect('/admin/login/?e=Logged%20out')


#: System update request
@app.route('/interface/update-system/', methods=['post'])
def interface_update_system():
    for prop in request.form:
        db_prop = SystemProperty.query.filter_by(attr=prop).first()
        if db_prop.value != request.form[prop]:
            db_prop.value = request.form[prop]
            db.session.add(db_prop)
    db.session.commit()
    return redirect('/admin/system?s=Settings%20updated.')


#: remove attribute from system
@app.route('/interface/delete-prop/<attr>', methods=['get'])
def interface_delete_prop(attr):
    prop = SystemProperty.get_full(attr)
    if prop.custom and User.is_logged_in():
        db.session.delete(prop)
        db.session.commit()
        return redirect('/admin/system?s=Property%20deleted.')
    return redirect('/admin/system?e=You%20can\'t%20do%20that.')


#: create attribute for system
@app.route('/interface/create-prop', methods=['post'])
def interface_create_prop():
    if not request.form['newattr']:
        return redirect('/admin/system?e=Attribute%20field%20empty.')
    prop = SystemProperty(request.form['newattr'].lower(),
                          request.form['newvalue'], 1)
    db.session.add(prop)
    try:
        db.session.commit()
    except:
        return redirect('/admin/system?e=Property%20already%20exists.')
        db.session.flush()
    return redirect('/admin/system?s=Property%20created.')


#: edit or create a section
@app.route('/interface/edit-section', methods=['post'])
def interface_edit_section():
    section = Section.get(request.form['name'])
    if section is None:
        #: creating a new section
        section = Section(request.form['name'],
                          request.form['title'],
                          request.form['content'])
        db.session.add(section)
    else:
        #: updating an existing section
        section.name = request.form['name']
        section.title = request.form['title']
        section.content = request.form['content']
    db.session.commit()
    return redirect('/admin/sections/{}/?s=Section%20updated'
                    .format(request.form['name']))


#: delete section
@app.route('/interface/delete-section/<name>/', methods=['get'])
def interface_delete_section(name):
    section = Section.get(name)
    if User.is_logged_in():
        db.session.delete(section)
        db.session.commit()
        return redirect('/admin/sections?s=Section%20deleted.')
    return redirect('/admin/sections?e=You%20can\'t%20do%20that.')

#: update user
@app.route('/interface/edit-user', methods=['post'])
def interface_edit_user():
    if (request.form['password'] == ""):
        return redirect('/admin/users?e=No%20password%20supplied.')
    if (request.form['password'] != request.form['confirm_password']):
        return redirect('/admin/users?e=Password%20don\'t%20match.')
    user = User.get(request.form['username'])
    user.password = User.hash_password(request.form['password'])
    db.session.add(user)
    db.session.commit()
    return redirect('/admin/users?s=Password%20updated.')