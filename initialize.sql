CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(50),
    password VARCHAR(50),
    is_active BOOLEAN
    
);

CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    title VARCHAR(50),
    content VARCHAR(50),
    view_count INT,
    status VARCHAR(50) DEFAULT 'draft',
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (user_id, username, email, password, is_active) VALUES (1, 'kelseym', 'nky7nt@virginia.edu', 'unicorn', TRUE);
INSERT INTO users (user_id, username, email, password, is_active) VALUES (2, 'beabadoobee', 'beaba@gmail.com', 'il0vemusic', FALSE);
INSERT INTO users (user_id, username, email, password, is_active) VALUES (3, 'hazel', 'hazel@yahoo.com', 'poodle', TRUE);
INSERT INTO users (user_id, username, email, password, is_active) VALUES (4, 'oakley', 'oakley@gmail.com', 'tennisb4ll', FALSE);
INSERT INTO users (user_id, username, email, password, is_active) VALUES (5, 'sonnyangel', 'sonnya@aol.com', 'bl1ndb0x', FALSE);

INSERT INTO posts (post_id, title, content, view_count, user_id) VALUES (1, 'hello', 'this is kelsey, please give me an a on my lab thanks', 1000000, 1); 
INSERT INTO posts (post_id, title, content, view_count, user_id) VALUES (2, 'pylon', 'listen to the new beabadoobee album its so good', 200, 2);
INSERT INTO posts (post_id, title, content, view_count, user_id) VALUES (3, 'hazel my dog', 'hazel i will see you on saturday for fall break yay!', 2323, 3);
INSERT INTO posts (post_id, title, content, view_count, user_id) VALUES (4, 'from oakley', 'i will also see you oakley yayyay', 3232, 4);
INSERT INTO posts (post_id, title, content, view_count, user_id) VALUES (5, 'new series', 'the new sonny angel series is so ugly', 4545, 5);
