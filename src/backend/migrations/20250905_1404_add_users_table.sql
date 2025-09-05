-- Create reviews table
CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(30) PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_DATE
);

CREATE INDEX IF NOT EXISTS user_id_idx ON users(user_id);

CREATE INDEX IF NOT EXISTS username_idx ON users(username);
