-- trigger that decreases the quantity of an item after adding a new order.
-- The trigger is activated after an insert operation on the order table.

CREATE TRIGGER decrease_quantity AFTER INSERT ON order
FOR EACH ROW UPDATE items 
SET quantity = NEW.number WHERE name = NEW.item_name;