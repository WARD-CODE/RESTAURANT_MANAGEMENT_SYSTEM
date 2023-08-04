# Importing all necessary modules
# like App, BoxLayout, Window, Builder, Camera
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from database_track import get_paquet,get_product,set_database
from barcode_extractor import get_barcode
from kivy.uix.camera import Camera


Builder.load_file("model_view.kv")

class MyApplication(App):
    def build(self):
        Window.size = (480, 700)
        Window.clearcolor = (1, 1, 1, 1)
        return AppLayout()

class AppLayout(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super(AppLayout, self).__init__(**kwargs)
    #     self.camera = Camera(resolution=(640, 480), play=False)
    #     self.add_widget(self.camera)

    # def start_scanner_product(self):
    #     # Start the camera for scanning the product
    #     self.camera.play = not self.camera.play

    # def start_scanner_paquet(self):
    #     # Start the camera for scanning the paquet
    #     self.camera.play = not self.camera.play

    # def capture_image(self):
    #     if self.camera.play and self.camera.texture:
    #         # Capture the current frame from the camera
    #         self.camera.export_to_png("captured_image.png")
    #         # You can add more code here to process the image or display it in your app
    #         # For example, you can use OpenCV or other image processing libraries.
    #         # After capturing the image, stop the camera
    #         self.camera.play = False

if __name__ == "__main__":
    MyApplication().run()
