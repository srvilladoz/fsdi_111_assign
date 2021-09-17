CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);

-- Creating default test users
INSERT INTO user (
    first_name,
    last_name,
    hobbies
)VALUES (
    "John",
    "Doe",
    "Knitting"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
)VALUES (
    "Jane",
    "Doe",
    "Hiking"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
)VALUES (
    "Sarah",
    "Villadoz",
    "Playing with dogs"
);

