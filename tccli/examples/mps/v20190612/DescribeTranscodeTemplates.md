**Example 1: 获取转码模板**



Input: 

```
tccli mps DescribeTranscodeTemplates --cli-unfold-argument  \
    --Definitions 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TranscodeTemplateSet": [
            {
                "Definition": 1008,
                "Container": "mp4",
                "Name": "模板1",
                "Comment": null,
                "Type": 0,
                "RemoveVideo": 0,
                "RemoveAudio": 0,
                "VideoTemplate": {
                    "Codec": "libx264",
                    "Fps": 24,
                    "Bitrate": 256,
                    "ResolutionAdaptive": "open",
                    "Width": 0,
                    "Height": 0,
                    "MinGop": 1,
                    "MaxGop": 10,
                    "VideoProfile": "high",
                    "ColorSpace": "yuv420p"
                },
                "AudioTemplate": {
                    "Codec": "libfdk_aac",
                    "Bitrate": 48,
                    "SampleRate": 48000,
                    "AudioChannel": 2,
                    "AudioProfile": "aac_lc"
                },
                "ContainerType": "Video",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

