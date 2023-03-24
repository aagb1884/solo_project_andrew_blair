DROP TABLE IF EXISTS orders_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS items;

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone_no VARCHAR(255),
    address VARCHAR(255)
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price INT
);

CREATE TABLE orders_items (
    id SERIAL PRIMARY KEY,
    order_id INT NOT NULL REFERENCES orders(id),
    item_id INT NOT NULL REFERENCES items(id)  
);

INSERT INTO orders (name, phone_no, address)
VALUES ('Lewis', '07891 234 567', '57 King St, EH90 1LS');

INSERT INTO orders (name, phone_no, address)
VALUES ('Paul', '01234 567 8910', '42 Roast Crescent, EH1 7ER');

INSERT INTO items (name, price)
VALUES ('Chips', '150');

INSERT INTO items (name, price)
VALUES ('Chips and Cheese', '200');

INSERT INTO items (name, price)
VALUES ('Chips and Curry Sauce', '200');

INSERT INTO orders_items (order_id, item_id)
VALUES (1, 2);

INSERT INTO orders_items (order_id, item_id)
VALUES (2, 1);

INSERT INTO orders_items (order_id, item_id)
VALUES (2, 3);