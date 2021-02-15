# MAHE-Toastmasters-Project-Tracker
1. Download this repository and open it in the terminal
2. pip install flask
3. pip install flask-sqlalchemy
4. python
	- from project import db, create_app
	- db.create_all(app=create_app())
	- quit()
5.
	- FOR WINDOWS:
		- set FLASK_APP=project
		- set FLASK_DEBUG=1
	- FOR LINUX:
		- export FLASK_APP=project
		- export FLASK_DEBUG=1
6. flask run
- [Tutorial](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login#configuring-the-database)
