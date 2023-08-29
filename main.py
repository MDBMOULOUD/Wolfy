from kivy.app import App
from kivy.properties import ListProperty
from kivy.core.window import Window

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import random
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.metrics import sp
from kivy.core.audio import SoundLoader
from kivy.clock import Clock

from kivy.uix.label import Label  # Import Label widget


Window.clearcolor = (0.8, 0.9, 0.98, 1)


class Screen1(Screen):
    pass


class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        self.roles = []
        self.roles1 = []
        self.cap = []
        self.sound = SoundLoader.load('MDdrill.wav')

        self.sound.play()

    def button_pressed(self, button):
        button_name = button.text
        app = App.get_running_app()

        if button.disabled:
            # Enable the button and remove its role from the list
            button.disabled = False
            app.roles.remove(button_name)
        else:
            if button_name not in app.roles and button_name != '   Simple \n\n villageois':
                app.roles.append(button_name)
                button.disabled = True
            elif button_name == '   Simple \n\n villageois':
                app.roles.append(button_name)

        app.cap.append('capitaine')


class Screen3(Screen):
    def __init__(self, **kwargs):
        super(Screen3, self).__init__(**kwargs)
        self.roles_to_draw = []
        self.drawn_roles = []
        self.roles_to_draw2 = []
        self.drawn_roles1 = []
        self.capitaines = []
        self.capitaines.append('capitaine')
        self.soundWolf = SoundLoader.load('Wolf.wav')
        #self.sound = SoundLoader.load('MDdrill.wav')
        self.soundWolf.play()
    def draw_role(self):
        if self.roles_to_draw:
            index = random.randint(0, len(self.roles_to_draw) - 1)

            role = self.roles_to_draw.pop(index)

            self.drawn_roles.append(role)

            self.update_label()

            a = random.choice(range(1, len(self.drawn_roles) + 1))
            if len(self.drawn_roles) == a:
                self.ids.role_label.text += 'Captain'

            for i in range(10):
                anim = (
                    Animation(opacity=0, duration=0.5,)
                    + Animation(opacity=1, duration=0.5)
                    + Animation(opacity=0, duration=0.5)
                    + Animation(opacity=1, duration=0.5)
                    + Animation(opacity=0, duration=0.5)
                    + Animation(opacity=1, duration=0.5)
                    + Animation(opacity=0, duration=0.5)
                    + Animation(opacity=1, duration=0.5)
                )
                anim.start(self.ids.role_label)

            if role != '   Simple \n\n villageois':
                self.capitaines.append('')
            else:
                self.capitaines.append('')

            self.update_label()

        else:
            self.ids.role_label.text = "No roles left to draw!"

    def delete_drawn_role(self):
        if self.drawn_roles:
            index = random.randint(0, len(self.drawn_roles) - 1)
            role_to_delete = self.drawn_roles.pop(index)
            self.capitaines.pop(index)
            self.update_label()

    def update_label(self):
        role_texts = []
        for role, capitaine in zip(self.drawn_roles, self.capitaines):
            if capitaine:
                role_texts.append(f"{role}\n{capitaine}")
            else:
                role_texts.append(role)
        self.ids.role_label.text = "\n".join(role_texts)

    def reset_roles(self):
        self.drawn_roles = []
        self.capitaines = []
        self.roles_to_draw = Md.roles.copy()
        self.update_label()
    
    

    
    

class ManagerScreen(ScreenManager):
    pass


mm = Builder.load_file('md.kv')


class Md(App):
    
    roles = []

    cap = []

    def build(self):
        self.title = "Mouloud Application"
        self.icon='sigma.png'
        return mm


if __name__ == "__main__":
    Md().run()