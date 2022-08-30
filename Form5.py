from ._anvil_designer import Form5Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form5(Form5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def primary_color_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    l=anvil.server.call('getlang')
    if self.radio_button_1.selected:
      if l==1:
        open_form('Form14')
      if l==2:
        open_form('Form15')
    if self.radio_button_2.selected:
      if l==1:
        open_form('Form16')
      if l==2:
        open_form('Form17') 
    if self.radio_button_3.selected:
      if l==1:
        open_form('Form18')
      if l==2:
        open_form('Form19')
    if self.radio_button_4.selected:
      if l==1:
        open_form('Form20')
      if l==2:
        open_form('Form21') 
    if self.radio_button_5.selected:
      if l==1:
        open_form('Form22')
      if l==2:
        open_form('Form23')
    if self.radio_button_6.selected:
      if l==1:
        open_form('Form24')
      if l==2:
        open_form('Form25') 
    if self.radio_button_7.selected:
      if l==1:
        open_form('Form26')
      if l==2:
        open_form('Form27') 
    

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')
    pass






