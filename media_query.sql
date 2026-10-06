SELECT
    users.username,
    posts.title,
    posts.content,
    posts.view_count
FROM users
JOIN posts
    ON users.user_id = posts.user_id
WHERE view_count > 1000;
