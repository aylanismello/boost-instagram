# https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md
# https://github.com/InstaPy/instapy-quickstart/tree/master/quickstart_templates

# Blocking likes issue: https://github.com/timgrossmann/InstaPy/issues/4609

import csv
import random, os, sys
from dotenv import load_dotenv
# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

load_dotenv()

followlist = []

with open('los_angles_users_with_followings.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')

  for row in csv_reader:
    new_follower = row[5]
    followlist.append(new_follower)

followlist = followlist[::-1]

try:
  user = sys.argv[1]
except:
  print('Pass which user you want to run this on')
  sys.exit()


headless_browser = True

print(f'headless browser? -> {headless_browser}')

# follow_list

insta_username = os.getenv(
    "HY_USERNAME") if user == 'hy' else os.getenv("BC_USERNAME")
insta_password = os.getenv(
    "HY_PASSWORD") if user == 'hy' else os.getenv("BC_PASSWORD")
cookie_path = os.getenv(
    "HY_COOKIE_PATH") if user == 'hy' else os.getenv("BC_COOKIE_PATH")

if os.path.exists(cookie_path):
    # removing the file using the os.remove() method
    os.remove(cookie_path)
    print(f'Removed cookie at {cookie_path}')
else:
    # file not found message
    print(f'File {cookie_path} not found in the directory')

disable_image_load = True

max_followers = 3000
min_followers = 50
min_following = 80

comments = []

burn_tags = [
        "bossanova", "latintrap", "jazz",
        "futurebeats", "futurejazz", "futurebaile", "ableton", 
        'mpb', 'chillbaile', 'funk150',
        'beats', 'soulection',  'bailefunk', 'jdilla', 'producer', 'chillhop',
        'afrobeat', 'kuduro', 'moombahton', 'globalclub'
]

secondary_tags = [ "pickupjazz", "pickupbeats", "bossanova", "latintrap", "jazz",
        "futurebeats", "futurejazz", "futurebaile", "ableton", "djmix",
        'mpb', 'chillbaile', 'funk150',
        "djset", "soundcloud", "djproducer", 'bedroomproducer', 'producerlife'
        'beats', 'soulection',  'bailefunk', 'ukg', 'jdilla', 'producer', 'chillhop',
        'afrobeat', 'kuduro' ] 


hy_tags = [
  'abletonpush', 'abletonbeats', 'abletonpush2', 'bossanova', 'mpb', 'pickupjazz', 'pickupbeats', 'futurebeats', 'futuremusic', 'soulection', 'bailefunk',
    'chillbaile', 'chillhop', 'electronica', 'lamusic', 'soundcloud', 'latinhouse', 'musicproducer', 'abletonlive', 'studiolife', 'beatmakers', 'electrocumbia'
]


tags = hy_tags if user == 'hy' else burn_tags
random.shuffle(tags)

dont_like_tags = [
  'yoga', 'vegan', 'workout', 'sexy', 'nazi', 'whitesupremacy', 
  'kkk', 'exercise', 'food', 'techno', 'trance', 'confederate',
  'psytrance', 'trancemusic', 'housemix',
  'learnguitar', 'lessons'
]

likes_per_tag = 5


locations = ['212999109/los-angeles-california/']
# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  disable_image_load=disable_image_load,
                  headless_browser=headless_browser)

with smart_run(session):
  # GENERAL SETTINGS
  session.set_dont_like(dont_like_tags)
  session.set_relationship_bounds(enabled=True, 
                                  delimit_by_numbers=True,
                                  max_followers=max_followers,
                                  min_followers=min_followers,
                                  min_following=min_following)
  
  session.set_delimit_liking(enabled=True, max_likes=500)

# Look around this user's profile and do shit
  session.set_user_interact(amount=3, randomize=True,
                            percentage=69, media='Photo')

  session.set_do_like(enabled=True, percentage=69)
  # ACITIVTY
  # START!







  session.like_by_tags(tags, amount=likes_per_tag, interact=True)
  # session.follow_by_list(followlist=followlist,
  #                times=1, sleep_delay=600, interact=True)

  # session.like_by_feed(amount=100, randomize=True,
  #                      unfollow=False, interact=True)
  # session.like_by_locations(locations, amount=100)
