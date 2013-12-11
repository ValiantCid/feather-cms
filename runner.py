from Feather import app, config

app.config.from_object(config.Config)

if __name__ == '__main__':
	if config.Config.GLOBAL_ACCESS == True:
		app.run(host='0.0.0.0')
	else:
		app.run()