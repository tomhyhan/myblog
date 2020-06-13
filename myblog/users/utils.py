import os
import secrets
from PIL import Image
from flask import current_app, url_for
from myblog import mail
from flask_mail import Message


def save_picture(form_picture):
    file_name = secrets.token_hex(8)
    _, ext = os.path.splitext(form_picture.filename)
    picture_file_name = file_name + ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_picture', picture_file_name)

    resize = (125,125)
    img = Image.open(form_picture)
    img.thumbnail(resize)
    if ext == '.jpg':
        img = img.convert('RGB')
    img.save(picture_path)

    return picture_file_name


def send_email(user):
    token = user.get_reset_token()
    msg = Message('Your Account Recovery',
                  recipients=[user.email])
    msg.body = f'''To reset your password, please visit the following link:
{url_for('users.reset_password', token=token, _external=True)}
    
If you are not trying to change your password, please ignore this email. It is possible that another user entered their information incorrectly.
'''
    mail.send(msg)
