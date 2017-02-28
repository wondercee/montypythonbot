#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = 'helloworld.txt'

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'lu4iEecPQFZn4s9LGRPpYGUWb'
CONSUMER_SECRET = 'oFg9st50Yjd7ULxrYyuhegupLYbY0N90Dfajd6WOZfWW0Njdj0'
ACCESS_KEY = '834031117237907456-mCThq0J1KduyGb6yAQNytOCkBJDajJo'
ACCESS_SECRET = 'ZxwDhlAwqKNdEQvaLqYMfdnHaEBvjBhRjAnFayOKu0rmi'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes
