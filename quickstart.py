# https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md
# https://github.com/InstaPy/instapy-quickstart/tree/master/quickstart_templates

import random, os
from dotenv import load_dotenv
# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

load_dotenv()
# login credentials
insta_username = os.getenv("USERNAME")
insta_password = os.getenv("PASSWORD")

max_followers = 2000
min_followers = 150
min_following = 400

comments = []
tags = ["pickupjazz", "pickupbeats", "bossanova", "latintrap",
        "futurebeats", "futurejazz", "futurebaile", "ableton", "djmix",
        "djset", "soundcloud", "djproducer", 'bedroomproducer', 'producerlife'
        'beats', 'soulection',  'bailefunk'] 
random.shuffle(tags)

dont_like_tags = [
  'yoga', 'vegan', 'workout', 'sexy', 'nazi', 'whitesupremacy', 
  'kkk', 'exercise', 'edm', 'food', 'techno', 'deeptechno', 'trance', 
  'psytrance', 'trancemusic', 'rave', 'clubmusic', 'edmmusic', 'housemix', 'dubstep'
]

likes_per_tag = 20

locations = ['212999109/los-angeles-california/']
# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  disable_image_load=False,
                  headless_browser=True)

with smart_run(session):
  # GENERAL SETTINGS

  session.set_dont_like(dont_like_tags)
  session.set_relationship_bounds(enabled=True, 
                                  delimit_by_numbers=True,
                                  max_followers=max_followers,
                                  min_followers=min_followers,
                                  min_following=min_following)
  # session.set_mandatory_words(['food', '#nstafood'])
  # session.set_dont_like(['#food', '#instafood'])
  # session.set_dont_include(["friend1", "friend2", "friend3"])		
  
  session.set_delimit_liking(enabled=True, max_likes=150, min_likes=0)
  # https: // github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md  # smart-hashtags
  # session.set_smart_hashtags(
  #     tags, limit=3, sort='top', log_tags=True)

# Look around this user's profile and do shit
  session.set_user_interact(amount=2, randomize=True,
                            percentage=69, media='Photo')

  # session.set_do_follow(enabled=True, percentage=40)
  session.set_do_like(enabled=True, percentage=80)
  
  
  
  # ACITIVTY
  # START!
                            # images per tag
  # session.like_by_tags(use_smart_hashtags=True, amount=likes_per_tag)

  session.like_by_tags(tags, amount=likes_per_tag, interact=True)

  # session.like_by_feed(amount=100, randomize=True,
  #                      unfollow=False, interact=True)

  # session.like_by_locations(locations, amount=100)
