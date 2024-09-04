# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from app.models import Inventory
# import config

# app = Flask(__name__)
# app.config.from_object(config.Config)
# db = SQLAlchemy(app)

# with app.app_context():
#     db.create_all()

#     # Initial data insertion if the table is empty
#     if not Inventory.query.first():
#         initial_item = Inventory(
#             name='Laptop',
#             price=1000.00,
#             mac_address='00:00:00:00:00:00',
#             serial_number='1234567890',
#             manufacturer='Dell',
#             description='This is a laptop'
#         )
#         db.session.add(initial_item)
#         db.session.commit()

# from app import routes



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    with app.app_context():
        # Import models after app and db initialization
        from app.models import Inventory
        
        # Create tables
        db.create_all()

        # Insert initial data if table is empty
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

    # Import routes after app is created
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app

app = create_app()

