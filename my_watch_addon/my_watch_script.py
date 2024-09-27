from touch_sdk import Watch
import requests

# Home Assistant Konfiguration
HA_URL = "http://deine-homeassistant-url:8123/api/services/light/toggle"
HA_TOKEN = "dein_long_lived_access_token"
LIGHT_ENTITY_ID = "light.dein_licht"

class MyWatch(Watch):
    def on_tap(self):
        print('Tap detected!')
        self.toggle_light()

    def toggle_light(self):
        headers = {
            "Authorization": f"Bearer {HA_TOKEN}",
            "Content-Type": "application/json",
        }
        data = {
            "entity_id": LIGHT_ENTITY_ID
        }
        response = requests.post(HA_URL, headers=headers, json=data)
        if response.status_code == 200:
            print("Light toggled successfully!")
        else:
            print(f"Failed to toggle light: {response.status_code}")

# Initialisiere die Uhr
watch = MyWatch()
watch.start()
