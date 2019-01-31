from django.test import TestCase
from data.models import Greeting
from data import controller

class ControllerTest(TestCase):
    def test_able_to_save_greeting(self):
        # Save a greeting
        name = "yoyoma-test"
        greeting = "yo"*50
        g = controller.add_greeting(name, greeting)
        g.save()

        # Check to make sure it got saved
        self.assertEqual(Greeting.objects.get(name=name), g)

        # Delete
        g.delete()
    
    def test_able_to_get_greeting(self):
        name = "yoyoma-test" 
        g = Greeting(name=name)
        g.save()

        self.assertEqual(Greeting.objects.get(name=name), controller.get_greeting(name))

        # Delete
        g.delete()
