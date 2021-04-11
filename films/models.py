from application import db

class Acteur(db.Model):

    __tablename__ = 'Acteurs'

    id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.Text)
    achternaam = db.Column(db.Text)

    rol = db.relationship('Rol', backref='rol_acteur', lazy='dynamic')

    def __init__(self, voornaam, achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam

    def __repr__(self):
        return f"Voornaam: {self.voornaam}. Achternaam: {self.achternaam}."

class Regisseur(db.Model):

    __tablename__ = 'Regisseurs'

    id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.Text)
    achternaam = db.Column(db.Text)

    films = db.relationship('Film', backref='regisseur', lazy='dynamic')

    def __init__(self, voornaam, achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam

    def __repr__(self):
        return f"{self.voornaam} {self.achternaam}"

class Film(db.Model):

    __tablename__ = 'Films'

    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.Text)
    jaar = db.Column(db.Integer)
    regisseur_id = db.Column(db.Integer, db.ForeignKey('Regisseurs.id'))
    trailer = db.Column(db.Text)

    rol = db.relationship('Rol', backref='rol_film', lazy='dynamic')
    comment = db.relationship('Comment', backref='comment_film', lazy='dynamic')

    def __init__(self, titel, jaar, regisseur_id, trailer):
        self.titel = titel
        self.jaar = jaar
        self.regisseur_id = regisseur_id
        self.trailer = trailer

    def __repr__(self):
        return f"Titel: {self.titel}. Jaar {self.jaar}. Regisseur id: {self.regisseur_id}. Trailer link: {self.trailer}."

class Rol(db.Model):

    __tablename__ = 'Rollen'

    id = db.Column(db.Integer, primary_key=True)
    id_acteur = db.Column(db.Integer, db.ForeignKey('Acteurs.id'))
    id_film = db.Column(db.Integer, db.ForeignKey('Films.id'))
    naam_personage = db.Column(db.Text)

    def __init__(self, id_acteur, id_film, naam_personage):
        self.id_acteur = id_acteur
        self.id_film = id_film
        self.naam_personage = naam_personage

    def __repr__(self):
        return f"id_acteur: {self.id_acteur}. id_film {self.id_film}. naam_personage {self.naam_personage}."

class Comment(db.Model):

    __tablename__ = 'Comments'

    id = db.Column(db.Integer, primary_key=True)
    id_film = db.Column(db.Integer, db.ForeignKey('Films.id'))
    id_gebruiker = db.Column(db.Integer, db.ForeignKey('Gebruikers.id'))
    comment = db.Column(db.Text)

    def __init__(self, id_film, id_gebruiker, comment):
        self.id_film = id_film
        self.id_gebruiker = id_gebruiker
        self.comment = comment

    def __repr__(self):
        return f"id_film: {self.id_film}. id_gebruiker {self.id_gebruiker}. comment {self.comment}."