class UserName:

    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f'{name}は文字数のルール違反やで！')

        self.name = name

    def screen_name(self):
        return self.name.upper()


hibiki = UserName(name='hibiki')
a
print(hibiki)
print(hibiki.screen_name())
