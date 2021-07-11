import instaloader
import json
import re

L = instaloader.Instaloader()
L.load_session_from_file('x20920')
posts = instaloader.Profile.from_username(
    L.context, "lauren.jumps").get_posts()

image_urls = []
post_infos = []
patten = re.compile(r'[^/]*\.jpg')

i = 0
for post in posts:
    post_info = {}
    post_info['shortcode'] = post.shortcode
    post_info['date'] = str(post.date)
    image_url = post.url
    image_urls.append(image_url)
    image_name = patten.findall(image_url)[0]
    post_info['image_name'] = image_name
    post_infos.append(post_info)
    i += 1
    print(i)

with open('posts.json', 'w', encoding='utf-8') as f:
    json.dump(post_infos, f)

with open('images.json', 'w', encoding='utf-8') as f:
    json.dump(image_urls, f)

print('succeed')