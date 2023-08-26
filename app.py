from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pres.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


class Presentation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(30))
    problem_user = db.Column(db.String(500))
    problem_gpt = db.Column(db.String(500))
    description = db.Column(db.Text)
    adv = db.Column(db.Text)
    value_proposition = db.Column(db.Text)
    desc_vp_gpt = db.Column(db.Text)
    product = db.Column(db.Text)
    industry = db.Column(db.String(300))
    tam = db.Column(db.Integer)
    sam = db.Column(db.Integer)
    som = db.Column(db.Integer)
    bm = db.Column(db.Text)
    APRU = db.Column(db.Integer)
    lt = db.Column(db.Integer)
    ltv = db.Column(db.Integer)
    finance = db.Column(db.Text)
    team = db.Column(db.Text)
    investors = db.Column(db.Text)
    investmens = db.Column(db.Text)
    roadmap = db.Column(db.Text)
    contact = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/w',methods = ['POST', 'GET'])
def w():
    if request.method == 'POST':
        return ''
    else:
        try:
            project_name = request.json['project_name']
            problem = request.json['problem']
            za = request.json['za']
            description = request.json['description']
            adv = request.json['adv']
            product = request.json['product']
            team = request.json['team']
            investors = request.json['investors']
            value_of_investments = request.json['value_of_investments']
            where_inv = request.json['where_inv']
            roadmap = request.json['roadmap']
            phone = request.json['phone']
            email = request.json['email']
            website = request.json['website']
            #industry for tam sam som нет на сайте
            APRU = 1  # выручка на число клиентов
            churn_rate = 1
            lt = 1 / churn_rate
            ltv = APRU * lt
            presentation = Presentation(project_name=project_name)
            try:
                db.session.add(presentation)
                db.session.commit()
                return '2'
            except:
                return '4'
        except:
            return ''

if __name__=='__main__':
    app.run(debug=True)
