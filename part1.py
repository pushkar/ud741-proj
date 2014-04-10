#!/bin/python
from numpy import *
from sklearn.metrics import mean_squared_error

class User:
    def __init__(self, name):
        self.name = name
        self.avg_r = 0.0

class Item:
    def __init__(self, name):
        self.name = name


class Rating:
    def __init__(self, user_id, item_id, rating):
        self.user_id = user_id
        self.item_id = item_id
        self.rating = rating

user = []
user.append(User("Ann"))
user.append(User("Bob"))
user.append(User("Carl"))
user.append(User("Doug"))

item = []
item.append(Item("HP1"))
item.append(Item("HP2"))
item.append(Item("HP3"))
item.append(Item("SW1"))
item.append(Item("SW2"))
item.append(Item("SW3"))

rating = []
rating.append(Rating(1, 1, 4))
rating.append(Rating(1, 4, 1))
rating.append(Rating(2, 1, 5))
rating.append(Rating(2, 2, 5))
rating.append(Rating(2, 3, 4))
rating.append(Rating(3, 4, 4))
rating.append(Rating(3, 5, 5))
rating.append(Rating(4, 2, 3))
rating.append(Rating(4, 6, 3))

n_users = len(user)
n_items = len(item)
n_ratings = len(rating)

utility = zeros((n_users, n_items))

for r in rating:
    utility[r.user_id-1][r.item_id-1] = r.rating

set_printoptions(precision=3)
print utility

for i in range(0, n_users):
    user[i].avg_r = mean(utility[i])

def pcs(x, y):
    rx = user[x].avg_r
    ry = user[y].avg_r
    a = 0
    b = 1
    c = 1
    for j in range(0, n_items):
        if utility[x][j] > 0 and utility[y][j] > 0:
            a += (utility[x][j] - rx) * (utility[y][j] - ry)
            b += (utility[x][j] - rx) ** 2
            c += (utility[y][j] - ry) ** 2
    return a / sqrt(b*c)

def guess(user_id, i_id, top_n):
    user_id -= 1
    i_id -= 1
    s = []
    for i in range(0, n_users):
        s.append((pcs(user_id, i), i))

    s = sorted(s, reverse=True)
    r = 0
    n = 0
    for i in range(0, top_n):
        if utility[s[i][1]][i_id] > 0:
            r += (utility[s[i][1]][i_id] - user[s[i][1]].avg_r)
            n += 1
    if n == 0:
        n = 1
    return ((r / n) + user[user_id].avg_r)


n = 3 # Assume top_n users

utility_copy = copy(utility)
for i in range(0, n_users):
    for j in range(0, n_items):
        if utility_copy[i][j] == 0:
            utility_copy[i][j] = guess(i, j, n)

print utility_copy

print "Ann's rating for SW2 should be " + str(guess(1, 5, n))
print "Carl's rating for HP1 should be " + str(guess(3, 1, n))
print "Carl's rating for HP2 should be " + str(guess(3, 2, n))
print "Doug's rating for SW1 should be " + str(guess(4, 4, n))
print "Doug's rating for SW2 should be " + str(guess(4, 5, n))

guess = array([guess(1, 5, n), guess(3, 1, n), guess(3, 2, n), guess(4, 4, n), guess(4, 5, n)])
test = array([2, 2, 2, 4, 3])
print "Mean Squared Error is " + str(mean_squared_error(guess, test))
