import json
import sqlite3

conn = sqlite3.connect('AnalogeH.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS Video;
DROP TABLE IF EXISTS Channel;
DROP TABLE IF EXISTS Series;

CREATE TABLE Video (
    id       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name     TEXT UNIQUE
    vid_id   TEXT UNIQUE
    views    TEXT UNIQUE
    comments TEXT UNIQUE
    sub_date TEXT UNIQUE
);

CREATE TABLE Channel (
    id       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title    TEXT UNIQUE
    chan_id  TEXT UNIQUE
);
                  
CREATE TABLE Series (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name   TEXT UNIQUE
);

''')


fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    title = entry[0]
    date = entry[1]
    vidId = entry[2]
    chanTitle = entry[3]
    chanId = entry[4]
    views = entry[5]
    comments = entry[6]

    cur.execute('''INSERT OR IGNORE INTO Video (title, date, vidId, views, comments)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Video WHERE name = ? ', (title, date, vidId, views, comments, ))
    video_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Channel (chanTitle, chanId)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (chanTitle, chanId, ))
    channel_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Series
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( video_id ) )

    conn.commit()