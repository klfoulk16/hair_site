DROP TABLE IF EXISTS experts;

CREATE TABLE experts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    curl TEXT NOT NULL,
    length TEXT NOT NULL,
    density TEXT NOT NULL,
    porosity TEXT NOT NULL,
    oily TEXT NOT NULL,
    colored TEXT NOT NULL,
    permed TEXT NOT NULL,
    keratin TEXT NOT NULL,
    washMethod TEXT NOT NULL
);
