from time import sleep


class UrTube:
    """
    Главный класс, в котором расположены основные функции, методы(возможности) нашего UrTube. Методы:
    Регистрация, вход в аккаунт, выход из аккаунта, добавление видео, поиск видео по запросу, просмотр видео
    """
    users = {}
    videos = {}
    current_user = None
    login = None
    nickname = None
    password = None
    age = None

    """
    Если пользователя нет в "словарике" экей подобие бд, то добавляем ник, хэшируем пароль, возраст.
    Ключом будет - имя пользователя, значением - словарик из пароля и возраста 
    """
    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        if self.nickname not in self.users.keys():
            self.users[self.nickname] = {'password': hash(self.password), 'age': self.age}
            self.current_user = self.nickname
        else:
            print(f'Пользователь {self.nickname} уже существует')

    """
    Ищем ник пользователя по ключам словарика - users
    """
    def log_in(self, login, password):
        self.login = login
        self.password = hash(password)
        if self.login in self.users.keys():
            if self.password == self.users[self.login]['password']:
                self.current_user = self.login

    def log_out(self):
        self.current_user = None

    """
    Добавляем видео в словарик - videos. Схема схожая с users. Ключом будет - название видео.
    Значением - словарь, состоящий из ключа и значения. Сначала мы ищем название видео в словаре, если нет - добавляем
    """
    def add(self, *video_copies):
        for video_title in video_copies:
            if video_title in self.videos:
                continue
            else:
                self.videos[video_title.title] = {'duration': video_title.duration,
                                                  'Time_now': video_title.time_now,
                                                  'Adult_mode': video_title.adult_mode}

    """
    Поиск видео по переданному поисковому слову. Все названия видео(ключи) конвертируются в нижний регистр, так же,
    как и поисковое слово. Предложения(ключи) разбиваются на слова. В резалте у нас хранится True/False. 
    True, если искомое слово есть в нашем сплитанутом предложении.
    """
    def get_videos(self, search_word):
        found_videos = []
        for key in self.videos:
            word_video_key_lower = key.lower()
            word_video_key_split = word_video_key_lower.split()
            search_word_lower = search_word.lower()
            result = any(search_word_lower in word for word in word_video_key_split)
            if result:
                found_videos.append(key)
        return f'Список найденных видео по запросу: {search_word}\nВидео: {found_videos}'

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт чтобы смотреть видео')
            return
        if title in self.videos.keys():
            if self.users[self.current_user]['age'] < 18 and self.videos[title]['Adult_mode'] is True:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                return
            for time_video in range(1, self.videos[title]['duration']+1):
                print(time_video, end=' ')
                sleep(1)
            print('Конец видео')


class Video:
    """
    Класс для поиска видео(будем еще доделывать)
    """
    def __init__(self, title, duration, time_now=None, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def return_params(self):
        return self.title, self.duration, self.time_now, self.adult_mode


class User:
    """
    Класс пользователя, содержащий логин, пароль, возраст(будем еще доделывать)
    """
    def __init__(self, username, password, age):
        self.username = username
        self.password = hash(password)
        if isinstance(age, int):
            self.age = age


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

"""
Вывод в консоль:
['Лучший язык программирования 2024 года']
['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
Войдите в аккаунт чтобы смотреть видео
Вам нет 18 лет, пожалуйста покиньте страницу
1 2 3 4 5 6 7 8 9 10 Конец видео
Пользователь vasya_pupkin уже существует
urban_pythonist

"""


