from app import create_app, db
from werkzeug.security import generate_password_hash
from datetime import datetime
import os

# Create the application instance
app = create_app()

# Create database tables and admin user
with app.app_context():
    from app.models.user import User
    from app.models.medical_record import MedicalRecord, Notification
    
    db.create_all()
    
    # Create admin user if not exists
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(
            username='admin',
            email='lieutien124@gmail.com',
            password_hash=generate_password_hash('admin'),
            role='admin'
        )
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    # Use environment variables for host and port if available, with defaults if not
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    app.run(host=host, port=port)