from ._anvil_designer import Form7Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form7(Form7Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    v,l=anvil.server.call('getprocess')
    timings="மாலை பூஜை – 4:30  - 5:15  \nதிருவனந்தாள் பூஜை – 5:00 - 6:00 \nவிழா பூஜை – 6:30  - 7:15 \nகாலசந்தி பூஜை  6:30  - 7:15 \nத்ருகாலசந்தி பூஜை – 10:30  -  11:15 \nஉச்சிகால பூஜை – 10:30  -  11:15 \nஅர்த்தஜாம பூஜை – 7:30  -  8:15 \nபள்ளியறை பூஜை – 9:30 -  10:00 "
    eng_time="Maalai Pooja – 4:30 AM to 5:15 AM \nThiruvanandal Pooja – 5:00 AM to 6:00 AM\nVizha Pooja – 6:30 AM to 7:15 AM\nKalasandhi Pooja  6:30 AM to 7:15 AM\nThrukalasandhi pooja – 10:30 AM to 11:15 AM\nUchikkala Pooja (Noon Pooja) – 10:30 AM – 11:15 AM\nArdhajama Pooja (Night Pooja) – 7:30 PM – 8:15 PM\nPalliarai pooja – 9:30 PM – 10:00 PM"
    if (v==3) and (l=="ENGLISH"):
      self.label_2.text=eng_time
    elif (v==3) and (l=="TAMIL"):
      self.label_2.text=timings
    

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')
    pass

