from flask import Blueprint, render_template, flash, redirect, url_for, request,current_app
from myblog.users.forms import RegistrationForm, LoginForm
from myblog import db, bcrypt, create_myblog
from myblog.models import User
from flask_login import login_user, current_user, logout_user, login_required
import requests
import datetime

# app = create_myblog()
# with app.app_context():
#     # db.drop_all()
#     db.create_all()

from datetime import datetime
from myblog.models import Project

def test_is_new(test_client, init_db):
    first_post = Project.query.filter_by(user_id=1).first()
    new = False
    utcnow = '2020-06-12 20:00:28.070383'
    diff = datetime.utcnow() - first_post.data_posted
    diff_indays = diff.total_seconds()/86400
    if diff_indays <= 7:
        assert new == True

