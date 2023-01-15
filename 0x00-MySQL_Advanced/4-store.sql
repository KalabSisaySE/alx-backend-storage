-- creates a trigger that decreases the quantity of an item
-- after adding a new order

CREATE TRIGGER `items_INS`
AFTER INSERT
ON `orders` FOR EACH ROW
-- update the items table after each order decrease the quantity 
-- by the number of orders
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
