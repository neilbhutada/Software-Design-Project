from flask import Blueprint, render_template, url_for, request, redirect, flash
from . import db
from flask_login import login_user, logout_user, login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/resources')
@login_required
def resources():
    return render_template('resources.html')

@main.route('/checklist', methods=['POST', 'GET'])
@login_required
def checklist():
    return render_template('checklist.html')

@main.route('/checklist/submit', methods=['POST', 'GET'])
@login_required
def checklistsubmit():
    pathway = request.form.get('pathway1')
    level_type = request.form.get('level_type')
    project = request.form.get('project')
    if(pathway is None or level_type is None or project is None):
        flash("ALERT INVALID INPUT!")
        return(redirect(url_for('main.checklist')))
    #ERROR IN THIS PART
    # if((level_type) is 1):
    #     flash("LEVEL 1")
    # if(str(level_type) is "2"):
    #     flash("Level 2")
    # if(str(level_type) is "3"):
    #     flash("Level 3")
    # if(str(level_type) is "4"):
    #     flash ("Level 4")
    # if(str(level_type) is "5"):
    #     flash("Level 5")
    return render_template('checklistoptions.html', name = current_user.name, pathway = pathway, level_type = level_type, project = project)