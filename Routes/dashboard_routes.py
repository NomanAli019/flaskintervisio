from flask import Blueprint, render_template, session, redirect, url_for
dashboard_pages = Blueprint('dashboard_pages', __name__)

@dashboard_pages.route('/dashhome')
def dashHome():
    return render_template('homepagesTemp/index.html')