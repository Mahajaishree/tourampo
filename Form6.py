from ._anvil_designer import Form6Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime

class Form6(Form6Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.init_components(**properties)
    hour = int(datetime.datetime.now().hour)
    uname= anvil.server.call('gname')
    if hour>= 0 and hour<12:
        self.label_2.text ="Good Morning "+uname+"!"
    elif hour>= 12 and hour<18:
        self.label_2.text ="Good Afternoon " +uname+"!"
    else:
        self.label_2.text ="Good Evening "+uname+"!"
    self.label_3.text ="Welcome to Meenakshi Amman Temple !!.I am your Tourist guide Assistant"

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')
    pass

  def primary_color_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')
    pass




