import pyglet

import terminal

terminal_open = False

class TextWidget:
    def __init__(self, text, x, y, width, height, batch):
        self.document = pyglet.text.document.UnformattedDocument(text)
        self.document.set_style(0, len(self.document.text), dict(font_name='Menlo',
                                                                 font_size=11,
                                                                 color=(255, 255, 255, 255)))

        self.layout = pyglet.text.layout.IncrementalTextLayout(self.document, width, height, batch=batch)
        self.layout.position = x, y, 0
        self.caret = pyglet.text.caret.Caret(self.layout, color=(255,255,255))
        # Rectangular outline
        pad = 2
        self.rectangle = pyglet.shapes.Rectangle(x - pad, y - pad, width + pad, height + pad, (50, 50, 50), batch)


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(400, 140, caption='Termi-nal', *args, **kwargs)
        terminal.terminal_open = True

        self.batch = pyglet.graphics.Batch()
        self.widgets = [
            TextWidget(' <<', 0, 0, self.width, self.height, self.batch),
        ]
        self.text_cursor = self.get_system_mouse_cursor('text')

        self.focus = None
        self.set_focus(self.widgets[0])

    def on_draw(self):
        pyglet.gl.glClearColor(0, 0, 0, 0)
        self.clear()
        self.batch.draw()

    def on_text(self, text):
        if self.focus:
            self.focus.caret.on_text(text)

    def on_text_motion(self, motion):
        if self.focus:
            self.focus.caret.on_text_motion(motion)

    def on_text_motion_select(self, motion):
        if self.focus:
            self.focus.caret.on_text_motion_select(motion)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.TAB:
            if modifiers & pyglet.window.key.MOD_SHIFT:
                direction = -1
            else:
                direction = 1

            if self.focus in self.widgets:
                i = self.widgets.index(self.focus)
            else:
                i = 0
                direction = 0

            self.set_focus(self.widgets[(i + direction) % len(self.widgets)])

        elif symbol == pyglet.window.key.ENTER:
            self.on_close()

    def set_focus(self, focus):
        if focus is self.focus:
            return

        if self.focus:
            self.focus.caret.visible = False
            self.focus.caret.mark = self.focus.caret.position = 0

        self.focus = focus
        if self.focus:
            self.focus.caret.visible = True

    def on_close(self):
        terminal.terminal_open = False
        print("closed")

        self.has_exit = True
        from pyglet import app
        if app.event_loop.is_running:
            self.close()

def launch_terminal():
    window = Window(resizable=True)
