from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from app.models import Inventory

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    inventory = Inventory.query.all()
    return render_template('index.html', inventory=inventory)

@main_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        mac_address = request.form['mac_address']
        serial_number = request.form['serial_number']
        manufacturer = request.form['manufacturer']
        description = request.form['description']

        new_item = Inventory(name=name, price=price, mac_address=mac_address, 
                             serial_number=serial_number, manufacturer=manufacturer, 
                             description=description)
        db.session.add(new_item)
        db.session.commit()

        flash('Item added successfully!')
        return redirect(url_for('main.index'))

    return render_template('add.html')

@main_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    item = Inventory.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.price = request.form['price']
        item.mac_address = request.form['mac_address']
        item.serial_number = request.form['serial_number']
        item.manufacturer = request.form['manufacturer']
        item.description = request.form['description']

        db.session.commit()
        flash('Item updated successfully!')
        return redirect(url_for('main.index'))

    return render_template('edit.html', item=item)

@main_bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    item = Inventory.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully!')
    return redirect(url_for('main.index'))


#change