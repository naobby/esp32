import os
from main.ota_updater import OTAUpdater

wifi_ssid = "neobby"
wifi_password = "spdhql20!$"

def download_and_install_update_if_available():
  o = OTAUpdater('https://github.com/naobby/esp32')
  o.autoUpdate(wifi_ssid, wifi_password)

def start():
  download_and_install_update_if_available()

if __name__ == '__main__':
  start()






