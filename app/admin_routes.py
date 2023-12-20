from app import app
from app import db
from app.models import Content
from app.models import User
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import login_required

@app.route('/admin/edit-content', methods=['GET', 'POST'])
@login_required
def edit_content():
    if request.method == 'POST':
        section_name = request.form['section_name']
        content = request.form['content']
        content_record = Content.query.filter_by(section_name=section_name).first()
        if content_record:
            content_record.content = content
        else:
            new_content = Content(section_name=section_name, content=content)
            db.session.add(new_content)
        db.session.commit()
        return redirect(url_for('edit_content'))
    content_list = Content.query.all()
    return render_template('admin/edit_content.html', content_list=content_list)