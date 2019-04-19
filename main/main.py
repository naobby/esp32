import os
from ota_updater import OTAUpdater
from time import sleep
from machine import Pin

led1=Pin(2, mode=Pin.OUT)        #create LED object from pin2,Set Pin2 to output

wifi_ssid = "neobby"
wifi_password = "spdhql20!$"

def download_and_install_update_if_available():
  o = OTAUpdater('https://github.com/naobby/esp32')
  o.autoUpdate(wifi_ssid, wifi_password)

def start():
  download_and_install_update_if_available()

if __name__ == '__main__':
  start()
  while True:
  #  led1.value(not led1.value())
    sleep(1)











