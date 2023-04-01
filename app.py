from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'test'


db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app, name='INSTRUMENTS', template_mode='bootstrap4')

class InstrumentType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    instruments = db.relationship('MusicInstrument', backref='type', lazy=True)  
    # свойство позволяет получить все адреса этого типа
    
    def __repr__(self):
        return self.name


class MusicInstrument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    type_id = db.Column(db.Integer, db.ForeignKey('instrument_type.id'), nullable=False)
    
    def __repr__(self):
        return self.name


admin.add_view(ModelView(MusicInstrument, db.session))
admin.add_view(ModelView(InstrumentType, db.session))


app.run()


