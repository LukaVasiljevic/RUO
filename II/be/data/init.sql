-- Create book table
CREATE TABLE book (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
);

-- Insert books
INSERT INTO book (title, author) VALUES
    ('Zlocin i kazna', 'F.M. Dostojevski'),
    ('Sofijin svet', 'Justejn Gorder'),
    ('Ohridski prolog', 'Vladika Nikolaj Velimirovic'),
    ('Gubiliste', 'Cingiz Ajtmatov');