CREATE TABLE movie_dataset
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL , /* Movie name */
    rating      DECIMAL(10, 2) NOT NULL , /* Movie rating */
    votes       INTEGER NOT NULL , /* Number of total votes */
    meta        INTEGER NOT NULL , /* Meta score */
    genre       TEXT NOT NULL , /* Genre of movie */
    pg_rate     TEXT NOT NULL , /* PG-Rating */
    year        INTEGER NOT NULL , /* Year of production */
    duration    TEXT NOT NULL , /* Duration of movie */
    cast        TEXT NOT NULL , /* Actors */
    director    TEXT NOT NULL /* Director of that movie*/
);
