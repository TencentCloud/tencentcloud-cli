**Example 1: Enabling On-Cloud MixTranscoding**

This example shows you how to enable On-Cloud MixTranscoding for a specified room (ID: 3560) and specify the screen sharing template for the layout of each channel of video image.

Set the On-Cloud MixTranscoding parameters as follows:
- CDN live stream ID: 1400188366_3560_mix.
- Recording file name: 1400188366_3560_mix_file.
- CDN live stream video parameters: set the video width to 1280, height to 720, bitrate to 1560 Kbps, frame rate to 15, and GOP to 2 seconds.
- CDN live stream audio parameters: set the audio sample rate to 48 kHz, bitrate to 64 Kbps, and sound channel to dual-channel.
- Each channel of video image is arranged according to the screen sharing template, and the video stream in the big image on the left of the screen is the video image shared by the `main_pc` user.

Input: 

```
tccli trtc StartMCUMixTranscode --cli-unfold-argument  \
    --SdkAppId 1400188366\
    --RoomId 3560\
    --OutputParams.StreamId 1400188366_3560_mix\
    --OutputParams.PureAudioStream 0\
    --OutputParams.RecordId 1400188366_3560_mix_file\
    --OutputParams.RecordAudioOnly 0\
    --EncodeParams.VideoWidth 1280\
    --EncodeParams.VideoHeight 720\
    --EncodeParams.VideoBitrate 1560\
    --EncodeParams.VideoFramerate 15\
    --EncodeParams.VideoGop 2\
    --EncodeParams.BackgroundColor 0\
    --EncodeParams.AudioSampleRate 48000\
    --EncodeParams.AudioBitrate 64\
    --EncodeParams.AudioChannels 2\
    --LayoutParams.Template 2\
    --LayoutParams.MainVideoUserId main_pc\
    --LayoutParams.MainVideoStreamType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

