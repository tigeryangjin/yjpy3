class User:
    def __init__(self, first_name, last_name, gender, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birthday = birthday

    def describe_user(self):
        print(self.first_name + ' ' + self.last_name + '    性别：' + self.gender + '     生日：' + self.birthday)

    def greet_user(self):
        print('hello, ' + self.first_name + self.last_name)


class Admin(User):
    def __init__(self, first_name, last_name, gender, birthday):
        super().__init__(first_name, last_name, gender, birthday)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)


yj = Admin('jin', 'yang', '男', '1979-09-09')
yj.privileges.show_privileges()
