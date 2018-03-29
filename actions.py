from rasa_core.actions import Action

class ActionOrderPizza(Action):
    def name(self):
        return 'action_order_pizza'
    def run(self, dispatcher, tracker,  domain ):
        print('Ordering Pizza is completed! It should be with you soon :)')
        pass
