from usercontroller import signup
def user_routes(app):
	app.add_url_rule('/signup', 'signup', signup, methods = ['POST'])