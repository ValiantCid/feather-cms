class Config(object):

#: You may edit from this line...

	#:-- BEGIN FEATHER SETTINGS

	#: Install secret code
	#: (go to <hostname>/feather-install/<installcode> to install)
	#: make sure no-one knows this code otherwise bad things might happen
	INSTALL_CODE = 'MYSECRETCODE'

	#: set to true to allow the server to be accesses from any
	#: networked machine in development
	GLOBAL_ACCESS = True

	#:-- END FEATHER SETINGS

	#:-- BEGIN FLASK SETTINGS

	#: Recommended that DEBUG is set to False for production
	#: reloads the server on code update
	DEBUG = True

	#: A secret key is required for sessions to work
	#: Must be unique
	SECRET_KEY = 'MYSESSIONCODE'

	#:-- END FLASK SETTINGS
#: ...to this line