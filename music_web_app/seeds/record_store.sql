-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year INT,
    artist_id INT
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums (title, release_year, artist_id) VALUES ('Hyperspace Sunset', 2035, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Lighter Motion', 2028, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('your Limit', 2035, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Every One Need Horizon', 2055, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Earning Peace', 2040, 1);
