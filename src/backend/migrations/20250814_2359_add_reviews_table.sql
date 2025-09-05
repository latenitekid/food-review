-- Create reviews table
CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    movie_name VARCHAR(255) NOT NULL,
    headline VARCHAR(255) NOT NULL,
    rating INTEGER NOT NULL CHECK (rating >= 0 AND rating <= 10),
    date DATE,
    review_text TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS reviews_user_id_idx ON reviews(user_id);

CREATE INDEX IF NOT EXISTS reviews_movie_name_idx ON reviews(movie_name);

CREATE INDEX IF NOT EXISTS reviews_rating_idx ON reviews(rating DESC);
