#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


tk = TkDrawer()
try:
    for name in ["ccc", "cube", "box", "king", "cow", "p_test"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        pol = Polyedr(f"data/{name}.geom")
        pol.draw(tk)
        delta_time = time() - start_time
        print("Cумма площадей проекций граней,")
        print(f"центр которых — «хорошая» точка равен {pol.get_area()}.")
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
