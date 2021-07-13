import os
import json

with open('posts.json') as f:
    posts = json.load(f)

path = 'videos'  # 需要重命名文件夹路径
file_names = os.listdir(path)

print(file_names)

for name in file_names:
    old_name = path + '/' + name
    for post in posts:
        if post['video_name'] == name:
            new_name = path + '/' + post['date'].replace(':', '-') + '.mp4'
            break
    os.rename(old_name, new_name)

print('succeed')