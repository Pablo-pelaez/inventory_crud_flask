from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)

    db.init_app(app)

    with app.app_context():
        from app.models import Inventory
        
        db.create_all()

        if not Inventory.query.first():
            initial_item = Inventory(
                name='Laptop',
                price=1000.00,
                mac_address='00:00:00:00:00:00',
                serial_number='1234567890',
                manufacturer='Dell',
                description='This is a laptop'
            )
            db.session.add(initial_item)
            db.session.commit()

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app

app = create_app()

