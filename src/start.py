import unittest

from src.repo.repository import Repository
from src.serv.service import Service
from src.ui.console import Console

if __name__ == "__main__":
    r = Repository()
    s = Service(r)
    c = Console(s)
    c.run_console()



