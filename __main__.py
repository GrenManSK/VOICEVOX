from .complete_as_module import main
from curses import wrapper
from .__get_index__ import get_index


wrapper(main, get_index())
