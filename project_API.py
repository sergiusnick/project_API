# -*- coding: utf8 -*-
import math
import pygame
import random
import requests
import sys
import os

pygame.init()
screen = pygame.display.set_mode((600, 500))

choose_game_mode = True
# список городов которые будут в игре

# режим: столицы
capitals = ['Амстердам', 'Андорра-ла-Велья', 'Афины', 'Белград', 'Берлин', 'Берн', 'Братислава',
            'Брюссель', 'Будапешт', 'Бухарест', 'Вадуц', 'Валлетта', 'Варшава', 'Ватикан', 'Вена',
            'Вильнюс', 'Дублин', 'Загреб', 'Киев', 'Кишинёв', 'Копенгаген', 'Лиссабон', 'Лондон',
            'Любляна', 'Люксембург', 'Мадрид', 'Минск', 'Монако', 'Москва', 'Осло', 'Париж',
            'Подгорица', 'Прага', 'Рейкьявик', 'Рига', 'Рим', 'Сан-Марино', 'Сараево', 'Скопье',
            'София', 'Стокгольм', 'Таллин', 'Тирана', 'Хельсинки', 'Абу-Даби', 'Амман', 'Анкара',
            'Ашхабад', 'Багдад', 'Баку', 'Бангкок', 'Бандар-Сери-Бегаван', 'Бейрут', 'Бишкек',
            'Вьентьян', 'Дакка', 'Дамаск', 'Дели (Нью-Дели)', 'Джакарта', 'Дили', 'Доха', 'Душанбе',
            'Ереван', 'Иерусалим', 'Исламабад', 'Кабул', 'Катманду', 'Куала-Лумпур', 'Мале',
            'Манама', 'Манила', 'Маскат', 'Нейпьидо', 'Никосия', 'Нур-Султан', 'Пекин', 'Пномпень',
            'Пхеньян', 'Сана', 'Сеул', 'Сингапур', 'Ташкент', 'Тбилиси', 'Тегеран', 'Токио',
            'Тхимпху', 'Улан-Батор', 'Ханой', 'Шри-Джаяварденепура-Котте', 'Эль-Кувейт', 'Эр-Рияд',
            'Абуджа', 'Аддис-Абеба', 'Аккра', 'Алжир', 'Антананариву', 'Асмэра', 'Бамако', 'Банги',
            'Банжул', 'Бисау', 'Браззавиль', 'Виктория', 'Виндхук', 'Габороне', 'Гитега', 'Дакар',
            'Джибути', 'Джуба', 'Додома', 'Каир', 'Кампала', 'Кигали', 'Киншаса', 'Конакри',
            'Либревиль', 'Лилонгве', 'Ломе', 'Луанда', 'Лусака', 'Малабо', 'Мапуту', 'Масеру',
            'Мбабане', 'Могадишо', 'Монровия', 'Морони', 'Найроби', 'Нджамена', 'Ниамей', 'Нуакшот',
            'Порт-Луи', 'Порто-Ново', 'Прая', 'Претория', 'Рабат', 'Сан-Томе', 'Триполи', 'Тунис',
            'Уагадугу', 'Фритаун', 'Хараре', 'Хартум', 'Ямусукро', 'Яунде', 'Асунсьон', 'Бастер',
            'Бельмопан', 'Богота', 'Бразилиа', 'Бриджтаун', 'Буэнос-Айрес', 'Вашингтон', 'Гавана',
            'Гватемала', 'Джорджтаун', 'Каракас', 'Кастри', 'Кингстаун', 'Кингстон', 'Кито', 'Лима',
            'Манагуа', 'Мехико', 'Монтевидео', 'Нассау', 'Оттава', 'Панама', 'Парамарибо',
            'Порт-о-Пренс', 'Порт-оф-Спейн', 'Розо', 'Сан-Сальвадор', 'Сан-Хосе', 'Санто-Доминго',
            'Сантьяго', 'Сент-Джонс', 'Сент-Джорджес', 'Сукре', 'Тегусигальпа', 'Апиа',
            'Веллингтон', 'Канберра', 'Маджуро', 'Нгерулмуд', 'Нукуалофа', 'Паликир', 'Порт-Вила',
            'Порт-Морсби', 'Сува', 'Фунафути', 'Хониара', 'Южная Тарава (Баирики)']

# режим: города России
cities = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Нижний Новгород',
          'Казань', 'Челябинск', 'Омск', 'Самара', 'Ростов-на-Дону', 'Уфа', 'Красноярск',
          'Воронеж', 'Пермь', 'Волгоград', 'Краснодар', 'Саратов', 'Тюмень', 'Тольятти',
          'Ижевск', 'Барнаул', 'Ульяновск', 'Иркутск', 'Хабаровск', 'Ярославль',
          'Владивосток', 'Махачкала', 'Томск', 'Оренбург', 'Кемерово', 'Новокузнецк',
          'Рязань', 'Астрахань', 'Набережные Челны', 'Пенза', 'Липецк', 'Киров',
          'Чебоксары', 'Тула', 'Калининград', 'Балашиха', 'Курск', 'Севастополь', 'Сочи',
          'Улан-Удэ', 'Ставрополь', 'Тверь', 'Магнитогорск', 'Брянск', 'Иваново',
          'Белгород', 'Сургут', 'Владимир', 'Нижний Тагил', 'Архангельск', 'Чита',
          'Симферополь', 'Калуга', 'Смоленск', 'Волжский', 'Саранск', 'Череповец', 'Курган',
          'Орёл', 'Вологда', 'Якутск', 'Владикавказ', 'Подольск', 'Грозный', 'Мурманск',
          'Тамбов', 'Петрозаводск', 'Стерлитамак', 'Кострома', 'Нижневартовск',
          'Новороссийск', 'Йошкар-Ола', 'Химки', 'Таганрог', 'Комсомольск-на-Амуре',
          'Сыктывкар', 'Нижнекамск', 'Нальчик', 'Шахты', 'Дзержинск', 'Орск', 'Братск',
          'Энгельс', 'Ангарск', 'Благовещенск', 'Королёв', 'Старый Оскол',
          'Великий Новгород', 'Мытищи', 'Псков', 'Люберцы', 'Бийск', 'Южно-Сахалинск',
          'Прокопьевск', 'Армавир', 'Балаково', 'Рыбинск', 'Абакан', 'Северодвинск',
          'Петропавловск-Камчатский', 'Норильск', 'Уссурийск', 'Волгодонск', 'Сызрань',
          'Новочеркасск', 'Каменск-Уральский', 'Златоуст', 'Красногорск', 'Электросталь',
          'Альметьевск', 'Салават', 'Миасс', 'Керчь', 'Находка', 'Копейск', 'Пятигорск',
          'Коломна', 'Рубцовск', 'Березники', 'Хасавюрт', 'Майкоп', 'Одинцово', 'Ковров',
          'Кисловодск', 'Домодедово', 'Нефтекамск', 'Нефтеюганск', 'Новочебоксарск',
          'Батайск', 'Щёлково', 'Серпухов', 'Новомосковск', 'Дербент', 'Черкесск',
          'Первоуральск', 'Орехово-Зуево', 'Кызыл', 'Обнинск', 'Назрань', 'Невинномысск',
          'Новый Уренгой', 'Каспийск', 'Раменское', 'Димитровград', 'Октябрьский',
          'Долгопрудный', 'Камышин', 'Муром', 'Ессентуки', 'Новошахтинск', 'Жуковский',
          'Евпатория', 'Северск', 'Реутов', 'Артём', 'Ноябрьск', 'Ачинск', 'Пушкино',
          'Арзамас', 'Бердск', 'Сергиев Посад', 'Елец', 'Элиста', 'Ногинск',
          'Новокуйбышевск', 'Железногорск']

# режим: достопримечательности
sights = {'Мачу-Пикчу': 'machu_piсchu.jpg', 'Мечеть шейха Зайда': 'zaid.jpg',
          'Тадж-Махал': 'taj_mahal.jpg', 'Мескита': 'meskita.jpg',
          'Собор Святого Петра': 'st_paul.jpg', 'Ангкор-Ват': 'angkor.jpg',
          'Собор Воскресения Христова на Крови': 'sobor_na_krovi.jpg',
          'Пагода Шведагон': 'shvedagon.jpg',
          'Мемориал Линкольна': 'linkoln.jpg',
          'Древний город Петра': 'old_peter.jpg',
          'Великая Китайская Стена': 'great_wall.jpg',
          'Эфес': 'efes.jpg', 'Альгамбра': 'algambra.jpg',
          'Австралийский военный мемориал': 'military_memorial.jpg', 'Сиенский собор': 'siena.jpg',
          'Миланский собор Дуомо': 'milan.jpg', 'Храм Святого Семейства': 'sagrada_familia.jpg',
          'Мост «Золотые ворота»': 'golden_gate.jpg', 'Статуя Христа-Искупителя': 'christ.jpg',
          'Теотиуакан': 'teotihuacan.jpg',
          'Сиднейский оперный театр': 'sidney_opera.jpg'}


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


russia_image = pygame.transform.scale(load_image('russia.jpg'), (200, 100))
great_britain_image = pygame.transform.scale(load_image('great_britain.png'), (200, 100))
translations = [['Играть', 'Play'], ['Правила', 'Rules'], ['Настройки', 'Settings'],
                ['Столицы мира', 'Capitals'], ['Города России', 'Russian cities'],
                ['Интересные места', 'Interesting places'], ['Назад', 'Back']]


def terminate():
    pygame.quit()
    sys.exit()


def start_screen(lang):
    fon = pygame.transform.scale(load_image('fon.jpg'), (600, 500))
    play = Play(lang)
    rules = Rules(lang)
    settings = Settings(lang)
    screen.blit(fon, (0, 0))
    play_group.draw(screen)
    rules_group.draw(screen)
    settings_group.draw(screen)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                a = play.get_event(event)
                b = rules.get_event(event)
                c = settings.get_event(event)
                if a or b or c:
                    play_group.remove(play)
                    rules_group.remove(rules)
                    settings_group.remove(settings)
                if a:
                    mode, lang = choose_mode(lang)
                    return mode, lang
                elif b:
                    mode, lang = rules_screen(lang)
                    return mode, lang
                elif c:
                    mode, lang = settings_screen(lang)
                    return mode, lang
        pygame.display.flip()


def choose_mode(lang):
    fon = pygame.transform.scale(load_image('fon.jpg'), (600, 500))
    mode_capitals = ModeCapitals(lang)
    mode_russian_cities = ModeRussianCities(lang)
    mode_city_sights = ModeCitySights(lang)
    screen.blit(fon, (0, 0))
    mode_capitals_group.draw(screen)
    mode_city_sights_group.draw(screen)
    mode_russian_cities_group.draw(screen)
    play_group.draw(screen)
    rules_group.draw(screen)
    settings_group.draw(screen)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mode = 0
                if mode_capitals.get_event(event):
                    mode = 'capitals'
                elif mode_russian_cities.get_event(event):
                    mode = 'cities'
                elif mode_city_sights.get_event(event):
                    mode = 'sights'
                if mode:
                    mode_capitals_group.remove(mode_capitals)
                    mode_city_sights_group.remove(mode_city_sights)
                    mode_russian_cities_group.remove(mode_russian_cities)
                    return mode, lang
        pygame.display.flip()


def rules_screen(lang):
    fon = pygame.transform.scale(load_image('fon.jpg'), (600, 500))
    screen.blit(fon, (0, 0))
    rules = Rules(lang)
    rules.rect = rules.image.get_rect().move(150, 320)
    rules_group.draw(screen)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rules.get_event(event):
                    rules_group.remove(rules)
                    mode, lang = start_screen(lang)
                    return mode, lang
        pygame.display.flip()


def settings_screen(lang):
    fon = pygame.transform.scale(load_image('fon.jpg'), (600, 500))
    screen.blit(fon, (0, 0))
    settings = Settings(lang)
    russia = Russia()
    great_britain = GreatBritain()
    done = pygame.sprite.Sprite(all_sprites, done_group)
    done.image = load_image('done.png')
    done.rect = done.image.get_rect()
    if lang == 'ru':
        done.rect.x = 200
        done.rect.y = 80
    else:
        done.rect.x = 500
        done.rect.y = 80
    settings.rect = settings.image.get_rect().move(150, 320)
    settings_group.draw(screen)
    russia_group.draw(screen)
    great_britain_group.draw(screen)
    done_group.draw(screen)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                a = settings.get_event(event)
                b = russia.get_event(event)
                c = great_britain.get_event(event)
                if b:
                    lang = 'ru'
                elif c:
                    lang = 'en'
                if b or c:
                    settings_group.remove(settings)
                    russia_group.remove(russia)
                    great_britain_group.remove(great_britain)
                    done_group.remove(done)
                    mode, lang = settings_screen(lang)
                    return mode, lang
                elif a:
                    settings_group.remove(settings)
                    russia_group.remove(russia)
                    great_britain_group.remove(great_britain)
                    done_group.remove(done)
                    mode, lang = start_screen(lang)
                    return mode, lang

        pygame.display.flip()


class Play(pygame.sprite.Sprite):
    def __init__(self, lang):
        super().__init__(play_group, all_sprites)
        self.image = pygame.transform.scale(load_image('play_' + lang + '.png'), (300, 100))
        self.rect = self.image.get_rect().move(150, 80)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


class Rules(pygame.sprite.Sprite):
    def __init__(self, lang):
        super().__init__(rules_group, all_sprites)
        self.image = pygame.transform.scale(load_image('rules_' + lang + '.png'), (300, 100))
        self.rect = self.image.get_rect().move(150, 200)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


class Settings(pygame.sprite.Sprite):
    def __init__(self, lang):
        super().__init__(settings_group, all_sprites)
        self.image = pygame.transform.scale(load_image('settings_' + lang + '.png'), (300, 100))
        self.rect = self.image.get_rect().move(150, 320)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


class ModeCapitals(pygame.sprite.Sprite):
    def __init__(self, lang):
        super().__init__(mode_capitals_group, all_sprites)
        self.image = pygame.transform.scale(load_image('capitals_' + lang + '.png'), (300, 100))
        self.rect = self.image.get_rect().move(150, 80)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


class ModeRussianCities(pygame.sprite.Sprite):
    def __init__(self, lang):
        super().__init__(mode_russian_cities_group, all_sprites)
        self.image = pygame.transform.scale(load_image('russian_cities_' + lang + '.png'), (300, 100))
        self.rect = self.image.get_rect().move(150, 200)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


class ModeCitySights(pygame.sprite.Sprite):
    def __init__(self, lang):
        super().__init__(mode_city_sights_group, all_sprites)
        self.image = pygame.transform.scale(load_image('city_sights.png'), (300, 100))
        self.rect = self.image.get_rect().move(150, 320)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


class Russia(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(russia_group, all_sprites)
        self.image = russia_image
        self.rect = self.image.get_rect().move(50, 100)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


class GreatBritain(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(great_britain_group, all_sprites)
        self.image = great_britain_image
        self.rect = self.image.get_rect().move(350, 100)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


all_sprites = pygame.sprite.Group()
play_group = pygame.sprite.Group()
rules_group = pygame.sprite.Group()
settings_group = pygame.sprite.Group()
mode_capitals_group = pygame.sprite.Group()
mode_russian_cities_group = pygame.sprite.Group()
mode_city_sights_group = pygame.sprite.Group()
russia_group = pygame.sprite.Group()
great_britain_group = pygame.sprite.Group()
done_group = pygame.sprite.Group()


def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000
    a_lon, a_lat = a
    b_lon, b_lat = b
    radians_latitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_latitude)
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor
    distance = math.sqrt(dx * dx + dy * dy)
    return distance


class Answer:
    def __init__(self, answer, mode):
        self.answer = answer
        self.mode = mode

    def get_coordinates(self):
        geocoder_request = (f"http://geocode-maps.yandex.ru/1.x/?geocode={self.answer}" +
                            "&format=json")
        response = None
        try:
            response = requests.get(geocoder_request)
            if response:
                json_response = response.json()
                toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0][
                    "GeoObject"]
                toponym_coordinates = toponym["Point"]["pos"]
                return ','.join(toponym_coordinates.split())
            else:
                print("Ошибка выполнения запроса:")
                print(geocoder_request)
                print("Http статус:", response.status_code, "(", response.reason, ")")
        except:
            print("Проверьте подключение к сети Интернет.")


class MapParams(object):
    def __init__(self, answer):
        self.lat = 55.729738
        self.lon = 37.664777
        self.zoom = 5
        self.type = "sat"
        self.geoscreen = self.screen_to_geo()
        self.point = ""
        self.postal = ''
        self.route = ''
        self.use_postal_code = False
        self.answer = answer
        self.answer_coordinates = self.answer.get_coordinates()
        self.inaccuracy = 0
        self.max_zoom = 17 if self.answer.answer in sights else 12

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.lon, self.lat = self.position_to_geo(event.pos)
                if self.lon > 180:
                    self.lon -= 360
                if self.lon < -180:
                    self.lon += 360
                self.type = 'sat,skl'
                self.point = "&pt=" + ','.join([str(self.lon), str(self.lat), "pm2rdl"])
                self.route = (f"&pl={','.join(self.point.replace('&pt=', '').split(',')[:-1])}," +
                              self.answer_coordinates)
                self.inaccuracy = lonlat_distance((self.lon, self.lat),
                                                  tuple(map(float,
                                                            self.answer_coordinates.split(','))))
                print(self.inaccuracy)

            elif event.button == 4:
                if self.zoom <= self.max_zoom:
                    self.zoom += 1
                    self.geoscreen = self.screen_to_geo()

            elif event.button == 5:
                if self.zoom > 5:
                    self.zoom -= 1
                    self.geoscreen = self.screen_to_geo()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                direction = [1 if event.key == pygame.K_UP else -1][0]
                move = self.lat + direction * self.geoscreen[1]
                self.lat = [move if abs(move) < 85 else self.lat][0]

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                direction = [1 if event.key == pygame.K_RIGHT else -1][0]
                move = self.lon + direction * self.geoscreen[0]
                self.lon = [move if abs(move) < 180 else move + -1 * direction * 360][0]

    def screen_to_geo(self, width=200, height=150):
        dx = width * 0.0000428 * math.pow(2, 15 - self.zoom)
        dy = height * 0.0000428 * math.cos(math.radians(self.lat)) * math.pow(2, 15 - self.zoom)
        return dx, dy

    def position_to_geo(self, position):
        try:
            lx, ly = self.screen_to_geo(position[0] - 300, 225 - position[1])
            lx, ly = self.lon + lx, self.lat + ly

            return lx, ly
        except Exception as e:
            print(e)
            return tuple(map(float, self.point.replace('&pt=', '').split(',')[:-1]))


def load_map(mp):
    map_request = ("http://static-maps.yandex.ru/1.x/?" +
                   "ll={},{}&z={z}&l={type}{pt}{pl}".format(mp.lon, mp.lat, z=mp.zoom, type=mp.type,
                                                            pt=mp.point, pl=mp.route))

    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)

    return map_file


def show_sight(sight):
    photo = pygame.transform.scale(load_image(sights[sight.answer]), (600, 500))
    screen.blit(photo, (0, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                fon = pygame.transform.scale(load_image('fon.jpg'), (600, 500))
                screen.blit(fon, (0, 0))
                return  # начинаем игру


def main():
    global choose_game_mode
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    gamemode = None
    if choose_game_mode:
        gamemode, lang = start_screen('en')

    if gamemode == 'sights':
        answer = Answer(random.choice(eval('list(sights.keys())')), gamemode)
        show_sight(answer)
    else:
        answer = Answer(random.choice(eval(gamemode)), gamemode)

    mp = MapParams(answer)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            mp.update(event)
        map_file = load_map(mp)

        screen.blit(pygame.image.load(map_file), (0, 0))
        if gamemode != 'sights':
            pygame.draw.rect(screen, (152, 200, 220), (0, 450, 600, 500))
            screen.blit(pygame.font.SysFont('Impact Thin', 40).render(answer.answer, 1,
                                                                      (30, 48, 134)), (10, 460))

        pygame.display.flip()

    pygame.quit()
    os.remove(map_file)


if __name__ == "__main__":
    main()
