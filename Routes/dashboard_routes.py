from flask import Blueprint, render_template, session, redirect, url_for , sessions
dashboard_pages = Blueprint('dashboard_pages', __name__)

@dashboard_pages.route('/dashhome')
def dashHome():
    return render_template('DashboardTemp/dashindex.html')

@dashboard_pages.route('/dashresume')
def dash_resum():
    return render_template('DashboardTemp/dashresume.html')

@dashboard_pages.route('/dashinter')
def dash_inter():
    return render_template('DashboardTemp/dashinterview.html')