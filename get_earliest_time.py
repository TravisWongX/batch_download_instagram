import instaloader
# import datetime

L = instaloader.Instaloader()

# L.login(user='', passwd='')
# 先用命令instaloader --login='你的用户名'登录，则会保存session
L.load_session_from_file('')
profile_name = 'jumpropegal_'  # 博主用户名

posts = instaloader.Profile.from_username(
    L.context, profile_name).get_posts()

# earliest_day = datetime.datetime.today()

datetimes = []

for post in posts:
    datetimes.append(post.date)

datetimes.sort()

print(datetimes[0])
print(len(datetimes))
