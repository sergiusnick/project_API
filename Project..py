# -*- coding: utf8 -*-

import pygame
import random
import requests
import sys
import os
import math

pygame.init()
screen = pygame.display.set_mode((600, 500))
points = 0
guessed = []

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
sights = {'Мачу-Пикчу': ['machu_piсchu.jpg', (-72.543307, -13.161790)],
          'Мечеть шейха Зайда': ['zaid.jpg', (54.474369, 24.412349)],
          'Тадж-Махал': ['taj_mahal.jpg', (78.042119, 27.175014)],
          'Мескита': ['meskita.jpg', (78.042119, 27.175014)],
          'Собор Святого Петра': ['st_paul.jpg', (12.454805, 41.902181)],
          'Ангкор-Ват': ['angkor.jpg', (103.866968, 13.412503)],
          'Собор Воскресения Христова': ['sobor_na_krovi.jpg', (30.328660, 59.940064)],
          'Пагода Шведагон': ['shvedagon.jpg', (96.149640, 16.798365)],
          'Мемориал Линкольна': ['linkoln.jpg', (-77.050137, 38.889292)],
          'Древний город Петра': ['old_peter.jpg', (35.451653, 30.322172)],
          'Великая Китайская Стена': ['great_wall.jpg', (117.232121, 40.676563)],
          'Эфес': ['efes.jpg', (27.341812, 37.940433)],
          'Альгамбра': ['algambra.jpg', (-3.588103, 37.176429)],
          'Австралийский военный мемориал': ['military_memorial.jpg', (149.149383, -35.280523)],
          'Сиенский собор': ['siena.jpg', (11.329579, 43.317718)],
          'Миланский собор Дуомо': ['milan.jpg', (9.192844, 45.464241)],
          'Храм Святого Семейства': ['sagrada_familia.jpg', (2.174734, 41.403578)],
          'Мост «Золотые ворота»': ['golden_gate.jpg', (-122.478013, 37.813989)],
          'Статуя Христа-Искупителя': ['christ.jpg', (-43.209702, -22.952159)],
          'Теотиуакан': ['teotihuacan.jpg', (-98.870682, 19.690172)],
          'Сиднейский оперный театр': ['sidney_opera.jpg', (151.215386, -33.857163)]}


# функция загрузки изображения
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


russia_image = load_image('russia.png')
great_britain_image = load_image('great_britain.png')

# перевод некоторых слов
translations = [['Играть', 'Play'], ['Правила', 'Rules'], ['Настройки', 'Settings'],
                ['Столицы мира', 'Capitals'], ['Города России', 'Russian cities'],
                ['Интересные места', 'Interesting places'], ['Назад', 'Back'],
                ['Игра Окончена', 'Game Over'], ['Счёт:', 'Score:'],
                ['Лучший счет:', 'High score:']]


# функция выхода из Pygame
def terminate():
    pygame.quit()
    try:
        os.remove('map.png')
    except:
        pass
    sys.exit()


# стартовый экран (меню)
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


# экран выбора режима игры
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start_screen(lang)
        pygame.display.flip()


# экран с аннотацией к игре
def rules_screen(lang):
    fon = load_image('rules_' + lang + '.jpg')
    screen.blit(fon, (0, 0))
    back = Back(lang)
    back.rect = back.image.get_rect().move(150, 320)
    back_group.draw(screen)
    pygame.draw.rect(screen, (30, 48, 134), (180, 295, 300, 20))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.get_event(event):
                    back_group.remove(back)
                    mode, lang = start_screen(lang)
                    return mode, lang
        pygame.display.flip()


# экран с настройками
def settings_screen(lang):
    fon = pygame.transform.scale(load_image('fon.jpg'), (600, 500))
    screen.blit(fon, (0, 0))
    back = Back(lang)
    russia = Russia(lang)
    great_britain = GreatBritain(lang)
    done = pygame.sprite.Sprite(all_sprites, done_group)
    done.image = load_image('done.png')
    done.rect = done.image.get_rect()
    if lang == 'ru':
        done.rect.x = 200
        done.rect.y = 80
    else:
        done.rect.x = 500
        done.rect.y = 80
    back.rect = back.image.get_rect().move(150, 320)
    back_group.draw(screen)
    russia_group.draw(screen)
    great_britain_group.draw(screen)
    done_group.draw(screen)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                a = back.get_event(event)
                b = russia.get_event(event)
                c = great_britain.get_event(event)
                if b:
                    lang = 'ru'
                elif c:
                    lang = 'en'
                if b or c:
                    great_britain_group.draw(screen)
                    russia_group.draw(screen)
                    done_group.draw(screen)
                    pygame.display.flip()
                    back_group.remove(back)
                    russia_group.remove(russia)
                    great_britain_group.remove(great_britain)
                    done_group.remove(done)
                    mode, lang = settings_screen(lang)
                    return mode, lang
                elif a:
                    back_group.remove(back)
                    russia_group.remove(russia)
                    great_britain_group.remove(great_britain)
                    done_group.remove(done)
                    mode, lang = start_screen(lang)
                    return mode, lang


# классы для кнопок:

# для кнопки "Играть"
class Play(pygame.sprite.Sprite):
    def __init__(self, lang):
        super().__init__(play_group, all_sprites)
        self.image = pygame.transform.scale(load_image('play_' + lang + '.png'), (300, 100))
        self.rect = self.image.get_rect().move(150, 80)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


# для кнопки "Правила"
class Rules(pygame.sprite.Sprite):
    def __init__(self, lang):
        super().__init__(rules_group, all_sprites)
        self.image = pygame.transform.scale(load_image('rules_' + lang + '.png'), (300, 100))
        self.rect = self.image.get_rect().move(150, 200)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


# для кнопки "Настройки"
class Settings(pygame.sprite.Sprite):
    def __init__(self, lang):
        super().__init__(settings_group, all_sprites)
        self.image = pygame.transform.scale(load_image('settings_' + lang + '.png'), (300, 100))
        self.rect = self.image.get_rect().move(150, 320)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


# для кнопки "Назад"
class Back(pygame.sprite.Sprite):
    def __init__(self, lang):
        super().__init__(back_group, all_sprites)
        self.image = pygame.transform.scale(load_image('back_' + lang + '.png'), (300, 100))
        self.rect = self.image.get_rect().move(150, 320)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


# для кнопки "Столицы"
class ModeCapitals(pygame.sprite.Sprite):
    def __init__(self, lang):
        super().__init__(mode_capitals_group, all_sprites)
        self.image = pygame.transform.scale(load_image('capitals_' + lang + '.png'), (300, 100))
        self.rect = self.image.get_rect().move(150, 80)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


# для кнопки "Города России"
class ModeRussianCities(pygame.sprite.Sprite):
    def __init__(self, lang):
        super().__init__(mode_russian_cities_group, all_sprites)
        self.image = pygame.transform.scale(load_image('russian_cities_' + lang + '.png'),
                                            (300, 100))
        self.rect = self.image.get_rect().move(150, 200)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


# для кнопки "Места"
class ModeCitySights(pygame.sprite.Sprite):
    def __init__(self, lang):
        super().__init__(mode_city_sights_group, all_sprites)
        self.image = pygame.transform.scale(load_image('sights_' + lang + '.png'), (300, 100))
        self.rect = self.image.get_rect().move(150, 320)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


# для кнопки выбора русского языка
class Russia(pygame.sprite.Sprite):
    def __init__(self, lang):
        super().__init__(russia_group, all_sprites)
        self.image = russia_image
        self.rect = self.image.get_rect()
        self.rect.x = 50
        if lang == 'ru':
            self.rect.y = 110
        else:
            self.rect.y = 100

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


# для кнопки выбора английского языка
class GreatBritain(pygame.sprite.Sprite):
    def __init__(self, lang):
        super().__init__(great_britain_group, all_sprites)
        self.image = great_britain_image
        self.rect = self.image.get_rect()
        self.rect.x = 350
        if lang == 'en':
            self.rect.y = 110
        else:
            self.rect.y = 100

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False


# группы спрайтов
all_sprites = pygame.sprite.Group()
play_group = pygame.sprite.Group()
rules_group = pygame.sprite.Group()
settings_group = pygame.sprite.Group()
back_group = pygame.sprite.Group()
mode_capitals_group = pygame.sprite.Group()
mode_russian_cities_group = pygame.sprite.Group()
mode_city_sights_group = pygame.sprite.Group()
russia_group = pygame.sprite.Group()
great_britain_group = pygame.sprite.Group()
done_group = pygame.sprite.Group()


# функция, считающая расстояние между точками
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


# класс ответа
class Answer:
    def __init__(self, answer, mode, lang):
        key = 'trnsl.1.1.20190411T101949Z.78d4160c7fa6a0ce.5a54445e1d3185f1030254671e225a002eff7b83'
        self.lang = lang
        # перевод ответа на нужный язык с помощью API Яндекс.Переводчика
        self.answer = [answer] if lang == 'ru' else [requests.get(
            'https://translate.yandex.net/api/v1.5/tr.json/translate' +
            '?key={}&text={}&lang=en'.format(key, answer)).json()['text'][0], answer]
        self.mode = mode

    # получение координат города (или объекта) с помощью геокодера
    def get_coordinates(self):
        if self.mode != 'sights':
            geocoder_request = (f"http://geocode-maps.yandex.ru/1.x/?geocode={self.answer[-1]}" +
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
        else:
            return ','.join(list(map(str, sights[self.answer[-1]][1])))


# класс для работы с картой
class MapParams(object):
    def __init__(self, answer):
        self.lat = 55.729738
        self.lon = 37.664777
        self.zoom = 4
        self.type = "sat"
        self.geoscreen = self.screen_to_geo()
        self.point = ""
        self.route = ''
        self.answer = answer
        self.answer_coordinates = self.answer.get_coordinates()
        self.inaccuracy = 0
        self.max_zoom = 12
        self.finished = False

    # обновление карты
    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # нажав на левую кнопку мыши, мы составляем запрос для карты и
            # получаем информацию о том, на сколько мы ошиблись
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
                self.point += '~' + self.answer_coordinates + ',pm2gnl'
                self.inaccuracy = lonlat_distance((self.lon, self.lat),
                                                  tuple(map(float,
                                                            self.answer_coordinates.split(','))))
                self.finished = True

            # прокрутив колесико мышки, мы можем изменить масштаб
            elif event.button == 4:
                if self.zoom <= self.max_zoom:
                    self.zoom += 1
                    self.geoscreen = self.screen_to_geo()

            elif event.button == 5:
                if self.zoom > 4:
                    self.zoom -= 1
                    self.geoscreen = self.screen_to_geo()

        # с помощью стрелок можно двигать карту
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


# функция загрузки карты
def load_map(mp, lang):
    map_request = ("http://static-maps.yandex.ru/1.x/?" +
                   "ll={},{}&z={z}&l={type}&lang={lang}{pt}{pl}".format(mp.lon, mp.lat, z=mp.zoom,
                                                                        type=mp.type, lang=lang,
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


# функция, которая показывает достопримечательность
def show_sight(sight):
    photo = pygame.transform.scale(load_image(sights[sight.answer[-1]][0]), (600, 500))
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


# экран с результатом
def results(lang):
    global timer
    global points
    global choose_game_mode
    # рекорд хранится в файле "record.txt". Если его нет - он создается
    # points - очки за эту игру
    try:
        with open(os.path.join('data', 'record.txt'), 'r') as r:
            record = r.read()
    except:
        record = '0'

    if int(record) < points:
        record = str(points)
    with open(os.path.join('data', 'record.txt'), 'w') as r:
        r.write(record)
    fon = load_image('gameover.jpg')
    screen.blit(fon, (10, -30))

    back = Back(lang)
    back_group.draw(screen)
    if lang == 'ru':
        number = 0
    else:
        number = 1
    pygame.draw.rect(screen, (152, 200, 220), (0, 450, 600, 50))
    pygame.draw.rect(screen, (152, 200, 220), (0, 0, 10, 500))
    screen.blit(pygame.font.SysFont('Times New Roman', 35).render(
        translations[8][number] + ' ' * len(str(points)) + str(points), 1, (30, 48, 134)),
        (160, 190))
    screen.blit(
        pygame.font.SysFont('Times New Roman', 35).render(
            translations[9][number] + ' ' * len(record) + record,
            1, (30, 48, 134)), (160, 240))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.remove('map.png')
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back.get_event(event):
                    back_group.remove(back)
                    points = 0
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    timer = 60
                    return
        pygame.display.flip()


# главная функция, отвечает за процесс игры в целом
def main():
    global choose_game_mode
    global timer
    timer = 60

    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    gamemode = None
    lang = 'en'
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if choose_game_mode:
            gamemode, lang = start_screen(lang)

        result = game(gamemode, lang, screen)
        while result == 'next':
            # пока мы в цикле, игра продолжается, после этого выводятся результаты
            result = game(gamemode, lang, screen)
        results(lang)
        choose_game_mode = True

    pygame.quit()
    os.remove('map.png')


# функция, отвечающая за игру с картой
def game(gamemode, lang, screen):
    global timer
    global guessed
    global points
    ended = False

    pygame.time.set_timer(1, 10)

    # выбираем объект (или город) для угадывания
    if gamemode == 'sights':
        answer = Answer(random.choice(eval('list(sights.keys())')), gamemode, lang)
        while answer.answer[-1] in guessed:
            if len(guessed) == len(eval('list(sights.keys())')):
                results(lang)
                return
            answer = Answer(random.choice(eval('list(sights.keys())')), gamemode, lang)
        guessed.append(answer.answer[-1])
        show_sight(answer)
    else:
        answer = Answer(random.choice(eval(gamemode)), gamemode, lang)
        while answer.answer[-1] in guessed:
            if len(guessed) == len(eval(gamemode)):
                results(lang)
                return
            answer = Answer(random.choice(eval(gamemode)), gamemode, lang)
        guessed.append(answer.answer[-1])
    mp = MapParams(answer)
    running = True
    pygame.draw.rect(screen, (152, 200, 220), (0, 450, 600, 500))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            # если мы уже угадали и после этого нажали на карту, переходим к следующему объекту
            if mp.finished and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return 'next'
            elif event.type == pygame.QUIT:
                running = False
                os.remove('map.png')
                terminate()
            # если мы угадали, то таймер останавливается, чтобы мы могли всё детально рассмотреть
            elif event.type == 1 and not mp.finished:
                timer -= 0.01
            # обновляем карту
            mp.update(event)

        map_file = load_map(mp, lang)

        screen.blit(pygame.image.load(map_file), (0, 0))

        # выводим то, что нужно найти
        if gamemode != 'sights':
            screen.blit(pygame.font.SysFont('Times New Roman', 35).render(answer.answer[0], 1,
                                                                          (200, 200, 200)),
                        (10, 20))
        # если мы нажали на карту, то игра рассказывает нам, на сколько мы ошиблись
        if mp.finished:
            if not ended:
                ended = True
                screen.blit(pygame.font.SysFont('Times New Roman', 30).render(
                    ('You missed it by {} km' if lang == 'en' else 'Вы ошиблись на {} км').format(
                        str(int(mp.inaccuracy) // 1000)), 1, (30, 48, 134)), (10, 455))
                points += int(
                    (100000 - int(mp.inaccuracy) // 1000) * 0.0001)
                # хитрая формула для подсчета очков
                # если мы угадывали достопримечательности,
                # то показываем название только после того, как отгадали

            if gamemode == 'sights':
                if len(answer.answer[0]) > 25:
                    answer.answer[0] = answer.answer[0].split()
                    screen.blit(pygame.font.SysFont('Times New Roman', 35).render(
                        ' '.join(answer.answer[0][:2]), 1, (200, 200, 200)), (10, 20))
                    screen.blit(pygame.font.SysFont('Times New Roman', 35).render(
                        ' '.join(answer.answer[0][2:]), 1, (200, 200, 200)), (10, 60))
                    answer.answer[0] = ' '.join(answer.answer[0])
                else:
                    screen.blit(pygame.font.SysFont('Times New Roman', 35).render(
                        answer.answer[0], 1, (200, 200, 200)), (10, 20))
        # таймер
        screen.blit(pygame.font.SysFont('Times New Roman', 35).render(str(int(timer) // 60) + ':' +
                                                                      str(int(timer) % 60).zfill(2),
                                                                      1, (200, 200, 200)), (520,
                                                                                            20))
        # если время вышло, прекращаем работу функции
        if (int(timer) // 60) <= 0 and (int(timer) % 60) <= 0 or timer < 0:
            running = False

        pygame.display.flip()
    return


if __name__ == "__main__":
    main()
