from ._anvil_designer import Form4Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form4(Form4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def primary_color_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    l=anvil.server.call('getlang')
    if self.radio_button_1.selected:
      if l==1:
        open_form('Form8_copy')
      if l==2:
        open_form('Form8')
    if self.radio_button_2.selected:
      if l==1:
        open_form('Form9_copy')
      if l==2:
        open_form('Form9') 

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')
    pass


  

