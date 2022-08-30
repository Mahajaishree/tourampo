from ._anvil_designer import Form2Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def primary_color_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.radio_button_1.selected:
      value=1
    elif self.radio_button_2.selected:
      value=2
    elif self.radio_button_3.selected:
      value=3
    elif self.radio_button_4.selected:
      value=4
    l=self.drop_down_1.selected_value  
    anvil.server.call('process',value,l)
    if value==3:
       open_form('Form7')
    if value==1:
      open_form('Form3')
    if value==2:
      open_form('Form4')
    if value==4:
      open_form('Form5')
    pass

  def radio_button_2_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')
    pass



