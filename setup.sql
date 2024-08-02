--Table definition

CREATE TABLE task(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128),
    summary VARCHAR(256),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);



INSERT INTO task(
    name,
    summary,
    description
)VALUES(
    "Wash car",
    "The car needs to be washed",
    "Make sure the car gets waxed after it is washed"
),(
    "Walk the dog",
    "Rocky needs their exercise",
    "Make sure to do ay least 2 laps around the park"
),(
    "Buy groceries",
    "Go to the supermarket and buy groceries",
    "We need: Eggs, Milk, Cereal and Coffee"
);