kv = """
#:import ZBarCam kivy_garden.zbarcam.ZBarCam
BoxLayout:
    orientation: 'vertical'
    ZBarCam:
        id:qrcodecam
    Label:
        size_hint: None, None
        size: self.texture_size[0], 50
        text: ' '.join([str(symbol) for symbol in qrcodecam.symbols])
"""

from kivy.app import App
from kivy.lang import Builder


class QrCodeApp(App):
    
    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    QrCodeApp().run()