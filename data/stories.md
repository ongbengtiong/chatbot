## happy path  
* greet
    - utter_greet
* order_pizza
    - utter_get_pizza_size
* order_pizza
    - utter_get_pizza_toppings
* order_pizza
    - action_order_pizza
	
## Generated Story -3890000785145209971
* order_pizza
    - utter_get_pizza_size
* order_pizza{"size": "small"}
    - slot{"size": "small"}
    - utter_get_pizza_toppings
* order_pizza
    - utter_ordering_pizza
	- action_order_pizza
* order_pizza{"toppings": "olives"}
    - slot{"toppings": "olives"}
	
	
	
## Generated Story 6537423929175673581
* order_pizza
    - utter_get_pizza_size
* order_pizza{"size": "small"}
    - slot{"size": "small"}
    - utter_get_pizza_toppings
* order_pizza{"toppings": "olives"}
    - slot{"toppings": "olives"}
    - utter_ordering_pizza
    - action_order_pizza
	
## Generated Story -1058085373211705092
* order_pizza
    - utter_get_pizza_size
* order_pizza{"size": "small"}
    - slot{"size": "small"}
    - utter_get_pizza_toppings
* order_pizza{"toppings": "olives"}
    - slot{"toppings": "olives"}
    - utter_ordering_pizza
    - action_order_pizza
    - export
## Generated Story 1606647465460309176
* order_pizza{"toppings": "olives"}
    - slot{"toppings": "olives"}
    - utter_get_pizza_size
* order_pizza{"size": "large"}
    - slot{"size": "large"}
    - utter_ordering_pizza
    - action_order_pizza
## Generated Story -5927646458511961981
* order_pizza{"size": "large", "toppings": "olives"}
    - slot{"size": "large"}
    - slot{"toppings": "olives"}
    - utter_ordering_pizza
    - action_order_pizza
