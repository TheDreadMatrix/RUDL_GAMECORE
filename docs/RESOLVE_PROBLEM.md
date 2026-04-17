JOSHUA SETTINGS IN self.game.settings

change|load CONSTANT save them to your file 



Custom json settings must be:
your_custom_settings.json must be in PROJECT-NAME/.saves/

{
    "window": {
        "window-size": {
            "width": 800,
            "height": 600,
            "min-width": 799,
            "min-height": 599
        },
        "window-attr": {
            "vsync": 0,
            "fullscreen": false,
            "borderless": false,
            "resizable": true
        }
    },

    "audio": {
        "sound-volume": 1.0,
        "music-volume": 1.0
    },

    "frametime": 240

    "custom-audio": {...}
}



in PROJECT-NAME/router.py we write in init

self.settings_data = Joshua(...)
self.settings_dataread = self.settings_data.readData()
 
self.load_settings(self.settings_dataread)

and in savingProgress we write

self.save_settings()