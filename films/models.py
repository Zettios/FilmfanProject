from application import db

class Film(db.Model):

    __tablename__ = 'Film'

    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.Text)
    jaar = db.Column(db.Integer)
    regisseur_id = db.Column(db.Integer)
    trailer = db.Column(db.Text)

    def __init__(self, titel, jaar, regisseur_id, trailer):
        self.titel = titel
        self.jaar = jaar
        self.regisseur_id = regisseur_id
        self.trailer = trailer

    def __repr__(self):
        return f"Titel: {self.titel}. Jaar {self.jaar}. Regisseur id: {self.regisseur_id}. Trailer link: {self.trailer}."