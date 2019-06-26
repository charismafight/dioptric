from db import db, get
from case import Ui_formAdd
import sqlite3


class Actual_Case(Ui_formAdd):
    def __init__(self):
        super(Actual_Case, self).__init__()

    def bind_add(self):
        self.buttonBox.accepted.connect(get)
