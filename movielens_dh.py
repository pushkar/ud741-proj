#!/bin/python
import re

class User:
    def __init__(self, id, age, sex, occupation, zip):
        self.id = id
        self.age = age
        self.sex = sex
        self.occupation = occupation
        self.zip = zip

class Item:
    def __init__(self, id, title, release_date, video_release_date, imdb_url, \
    unknown, action, adventure, animation, childrens, comedy, crime, documentary, \
    drama, fantasy, film_noir, horror, musical, mystery ,romance, sci_fi, thriller, war, western):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.video_release_date = video_release_date
        self.imdb_url = imdb_url
        self.unknown = unknown
        self.action = action
        self.adventure = adventure
        self.animation = animation
        self.childrens = childrens
        self.comedy = comedy
        self.crime = crime
        self.documentary = documentary
        self.drama = drama
        self.fantasy = fantasy
        self.film_noir = film_noir
        self.horror = horror
        self.musical = musical
        self.mystery = mystery
        self.romance = romance
        self.sci_fi = sci_fi
        self.thriller = thriller
        self.war = war
        self.western = western

class Rating:
    def __init__(self, user_id, item_id, rating, time):
        self.user_id = user_id
        self.item_id = item_id
        self.rating = rating
        self.time = time

class Dataset:
    def load_users(self, file, u):
        f = open(file, "r")
        text = f.read()
        entries = re.split("\n+", text)
        for entry in entries:
            e = entry.split('|', 5)
            if len(e) == 5:
                u.append(User(e[0], e[1], e[2], e[3], e[4]))
        f.close()

    def load_items(self, file, i):
        f = open(file, "r")
        text = f.read()
        entries = re.split("\n+", text)
        for entry in entries:
            e = entry.split('|', 24)
            if len(e) == 24:
                i.append(Item(e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7], e[8], e[9], e[10], \
                e[11], e[12], e[13], e[14], e[15], e[16], e[17], e[18], e[19], e[20], e[21], \
                e[22], e[23]))
        f.close()

    def load_ratings(self, file, r):
        f = open(file, "r")
        text = f.read()
        entries = re.split("\n+", text)
        for entry in entries:
            e = entry.split('\t', 24)
            if len(e) == 4:
                r.append(Rating(e[0], e[1], e[2], e[3]))
        f.close()

user = []
item = []
rating = []
d = Dataset()
d.load_users("u.user", user)
d.load_items("u.item", item)
d.load_ratings("u.base", rating)
