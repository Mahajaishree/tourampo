from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    anvil.users.login_with_form()

    # Any code you write here will run when the form opens.

  def primary_color_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    name=self.text_box_1.text
    anvil.server.call('sname',name)
    open_form('Form6')
    pass



