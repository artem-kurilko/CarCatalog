from flask import render_template, Blueprint, request, redirect, flash, url_for
from website import db
from website.models import Car

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        car_name = str(request.form['name']).strip()
        description = str(request.form['desc']).strip()
        print(description)
        if car_name is not None and description is not None:
            exist = Car.query.filter_by(name=car_name).first()
            if exist is None:
                car = Car(name=car_name, description=description)
                db.session.add(car)
                db.session.commit()
                flash('Your car has been added.', category='success')
                return redirect(url_for('views.index'))
            else:
                flash('The car with this name already exists.', category='error')
                return redirect(url_for('views.index'))
        else:
            flash('Please fill out all fields', category='error')
            return redirect(url_for('views.index'))
    cars = Car.query.all()
    return render_template('index.html', cars=cars)
