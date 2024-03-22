import random as r


class UserData():
    email = 'korolev_6_sun@yandex.ru'
    password = 'Ghbvfn2501!'

    def new_email(self):
        email = f'arsenii_korolev_6_{r.randint(100, 999)}@ya.ru'
        return email

    def new_password_correct(self):
        password = r.randint(100000, 999999)
        return password

    def new_password_incorrect(self):
        password = r.randint(1, 99999)
        return password

