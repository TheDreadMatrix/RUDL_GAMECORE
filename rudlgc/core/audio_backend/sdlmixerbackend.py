from rudlgc.core.audio_backend.base_audio_backend import BaseAudioBackend


class SdlmixerBackend(BaseAudioBackend):
    def __init__(self, game):
        super().__init__(game)
        