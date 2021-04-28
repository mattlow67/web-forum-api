-- $ sqlite3 db1.db < posts.sql

PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS posts;
CREATE TABLE  posts (
	post_id INTEGER primary key,
	post_title VARCHAR,
	post_text VARCHAR,
	post_community VARCHAR,
	post_url VARCHAR,
	post_user_name VARCHAR,
	post_date VARCHAR,
	UNIQUE(post_id)
);

INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(1, 'Headman of Purity','What Am I, Chopped Liver?','Online Gaming','www.fills.com','someone','03/01/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(2, 'Sultan of Life','Cry Over Spilt Milk','Online Gaming','www.dilimitation.com','senior','03/01/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(3, 'Sultan of Blue','Wake Up Call','Online Gaming','www.elimination.com','randomgirl','03/02/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(4, 'Sultan of Blue','Wake Up Call','Online Gaming','www.elimination.com','randomgirl','03/02/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(5, 'Delegate of Planning','He stepped gingerly onto the bridge knowing that enchantment awaited on the other side.','Online Gaming','www.illumination.com','jay','03/02/2020');

INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(6, 'Burst Your Bubble','He always wore his sunglasses at night.','Math','www.google.com','someone','03/03/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(7, 'Under the Weather','Random words in front of other random words create a random sentence.','Math','www.google.com','senior','03/03/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(8, 'Up In Arms','Peanuts dont grow on trees, but cashews do' ,'Math','www.google.com','randomgirl','03/03/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(9, 'Down And Out','You cant compare apples and oranges, but what about bananas and plantains?','Math','www.google.com','somewhere','03/03/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(10, 'Close But No Cigar','Flying fish few by the space station','Math','www.google.com','jay','03/03/2020');

INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(11, 'Theres No I in Team','The doll spun around in circles in hopes of coming alive','Quills','www.yahoo.com','someone','03/04/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(12, 'Down For The Count','Not all people who wander are lost.','Quills','www.yahoo.com','sills','03/05/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(13, 'Quality Time','She traveled because it cost the same as therapy and was a lot more enjoyable.','Quills','www.yahoo.com','randomgirl','03/06/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(14, 'Flea Market','He swore he just saw his sushi move.','Quills','www.yahoo.com','sills','03/07/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(15, 'Between a Rock and a Hard Place','Please tell me you dont work in a morgue.','Quills','www.yahoo.com','v','03/08/2020');

INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(16, 'Down To Earth','It was the scarcity that fueled her creativity.','Science','www.facebook.com','someone','03/03/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(17, 'In a Pickle','Carol drank the blood as if she were a vampire.','Science','www.facebook.com','senior','03/03/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(18, 'Dropping Like Flies','Three years later, the coffin was still full of Jello.','Science','www.facebook.com','randomgirl','03/05/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(19, 'Right Out of the Gate','He found a leprechaun in his walnut shell.','Science','www.facebook.com','sills','03/0/2020');
INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(20, 'Elvis Has Left The Building','This is the last random sentence I will be writing and I am going to stop mid-sent','Science','www.facebook.com','jay','03/03/2020');


COMMIT;
