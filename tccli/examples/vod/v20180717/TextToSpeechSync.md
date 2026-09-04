**Example 1: 同步语音合成**

同步语音合成

Input: 

```
tccli vod TextToSpeechSync --cli-unfold-argument  \
    --SubAppId 221*** \
    --Text 我怕我沒有機會跟你說一聲再見. 因為也許就再也見不到你. 明天我要離開熟悉的地方和你. 要分離我眼淚就掉下去. 我會牢牢記住你的臉我會珍惜你給的思念. \
    --LanguageBoost zh \
    --VoiceId minimax_7*********c6c-495b \
    --Output.Type url \
    --ExtParam {
  "model": "minimax-speech-2.8-hd",
  "stream": false,
  "voice_setting": {
    "speed": 1.5,
    "vol": 1.0,
    "pitch": 0,
    "emotion": "calm",
    "text_normalization": true,
    "latex_read": false
  },
  "audio_setting": {
    "sample_rate": 32000,
    "bitrate": 128000,
    "format": "mp3",
    "channel": 1,
    "force_cbr": false
  },
  "voice_modify": {
    "pitch": 0,
    "intensity": 0,
    "timbre": 0,
    "sound_effects": ""
  },
  "timbre_weights": [
    { "voice_id": "ttv-voice-2026081010451926-MJGKXATq", "weight": 100 }
   ],
  "subtitle_enable": true,
  "subtitle_type": "srt"
}
```

Output: 
```
{
    "Response": {
        "AudioData": "UklGRnxuAABXQVZFZm10IBAAAAABAAEAgD4AAAB9AAACABAATElTVF4EAABJTkZPSUNNVDwEAABBSUdDP********************************************************************************GIzZGFiODAwZjNlYzc4N2Q3MjZhMmQyNDYyIiwiUmVzZXJ2ZWRDb2RlMSI6IntcIlNlY3VyaXR5RGF0Y",
        "AudioUrl": "https://tennyyang-test-1258344699.cos.ap-guangzh***********************************************-08-10/cda673d1-5bfb-4111-8572-1838b91ee267.mp3",
        "ExtInfo": "{\"audio_length\":10188,\"audio_sample_rate\":32000,\"audio_size\":164724,\"bitrate\":128000,\"audio_format\":\"mp3\",\"audio_channel\":1,\"word_count\":66,\"invisible_character_ratio\":0,\"usage_characters\":75}",
        "RequestId": "a40fdd09-c7dd-45d9-9621-800e6cefab1e"
    }
}
```

