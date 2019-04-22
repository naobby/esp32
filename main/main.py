import os
from ota_updater import OTAUpdater
from time import sleep
from machine import Pin

wifi_ssid = "neobby"
wifi_password = "spdhql20!$"

def download_and_install_update_if_available():
  global last_commit
  o = OTAUpdater('https://github.com/naobby/esp32')
  o.autoUpdate(wifi_ssid, wifi_password)
  last_commit = o.last_commit

def start():
  download_and_install_update_if_available()
  
def version():
  led1=Pin(22, mode=Pin.OUT)        #create Green-LED object from pin22,Set Pin22 to output
  print(last_commit)
  print("Toggle!")
  i = 0
  for i in range(2):
    led1.value(not led1.value())
    sleep(1)

if __name__ == '__main__':
  start()
  while(True):
    version()
