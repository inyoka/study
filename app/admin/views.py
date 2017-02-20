from flask import abort, render_template
from flask_login import current_user, login_required
from . import admin

# add admin dashboard view
@admin.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('home/dashboard.html', title="Dashboard")
