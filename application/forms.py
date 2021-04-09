class LoginForm(FlaskForm):
    filmfan = SubmitField('FilmFan')
    login = SubmitField('Login')
    account = SubmitField('Account')
    logout = SubmitField('Logout')
    contact = SubmitField('Contact')
    