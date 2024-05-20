import sqlite3
con = sqlite3.connect('db.sqlite')

SELECT title,
       release_year 
-- из всех записей в таблице video_products
FROM video_products; 
