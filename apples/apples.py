import tkinter as tk
import time

import settings as st
from controller import ApplesController


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self._init_main()

    def draw_apples(self):
        self._controller.draw_field()
        self._controller.draw_apples()
        if self._controller.check_if_collided():
            print("There are some collided circles")

    def _init_main(self):
        self.canvas = tk.Canvas(height=st.HEIGHT + 2*st.FRAME_SPAN,
                                width=st.WIDTH + 2*st.FRAME_SPAN,
                                bg='gray')
        self.canvas.pack()

        self._settings = st.ApplesGeneratorSettingBuilder().build()
        self._controller = ApplesController(self.canvas, self._settings)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(f'{st.WIDTH + 2*st.FRAME_SPAN}x{st.HEIGHT + 2*st.FRAME_SPAN}+200+300')
    root.resizable(False, False)

    app = Main(root)
    app.pack()

    app.draw_apples()

    root.mainloop()
