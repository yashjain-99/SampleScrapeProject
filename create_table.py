import sqlite3
import json

conn = sqlite3.connect('medium_posts_meta_data.db')
try:
    conn.execute('''CREATE TABLE meta_data (
        topic_name TEXT,
        topic_best_all_time_url TEXT,
        post_title TEXT,
        post_link TEXT,
        author_name TEXT,
        post_date DATETIME,
        read_time INTEGER,
        author_follower_count INTEGER,
        post_clap_count INTEGER,
        post_comment_count INTEGER,
        post_tags TEXT
        );''')
except:
    pass
cursor = conn.cursor()
with open('data.json') as json_file:
    data = json.load(json_file)
for item in data:
    topic_name = item['topic_name']
    topic_best_all_time_url = item['topic_best_all_time_url']
    post_title = item['post_title']
    post_link = item['post_link']
    author_name = item['author_name']
    post_date = item['post_date']
    read_time = item['read_time']
    author_follower_count = item['author_follower_count']
    post_clap_count = item['post_clap_count']
    post_comment_count = item['post_comment_count']
    post_tags = str(item['post_tags'])
    
    # Build the INSERT statement
    sql = '''INSERT INTO meta_data (topic_name, topic_best_all_time_url, post_title, post_link, author_name, post_date, read_time, author_follower_count, post_clap_count, post_comment_count, post_tags) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    values = (topic_name, topic_best_all_time_url, post_title, post_link, author_name, post_date, read_time, author_follower_count, post_clap_count, post_comment_count, post_tags)
    cursor.execute(sql, values)

# Commit the changes and close the connection
conn.commit()
conn.close()
