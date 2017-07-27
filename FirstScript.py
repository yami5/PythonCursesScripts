import curses
import os
os.system("mode con cols=100 lines=50")
stdscr=curses.initscr()
stdscr.refresh()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
pad = curses.newpad(20, 20)
# These loops fill the pad with letters; addch() is
# explained in the next section
#for y in range(0, 99):
 #   for x in range(0, 99):
  #      pad.addch(y,x, ord('a') + (x*x+y*y) % 26)

# Displays a section of the pad in the middle of the screen.
# (0,0) : coordinate of upper-left corner of pad area to display.
# (5,5) : coordinate of upper-left corner of window area to be filled
#         with pad content.
# (20, 75) : coordinate of lower-right corner of window area to be
#          : filled with pad content.
pad.refresh( 0,0, 5,5, 20,20)
curses.nocbreak()
stdscr.keypad(False)
curses.endwin()