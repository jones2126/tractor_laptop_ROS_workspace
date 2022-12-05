from xdo import Xdo
# ref: https://github.com/rshk/python-libxdo
# https://rshk.github.io/python-libxdo/library.html

xdo = Xdo()
win_id = xdo.select_window_with_click()
xdo.enter_text_window(win_id, 'Python rocks!')