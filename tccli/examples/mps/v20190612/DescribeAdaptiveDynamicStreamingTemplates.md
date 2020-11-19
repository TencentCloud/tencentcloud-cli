**Example 1: 查询转自适应码流模板列表**



Input: 

```
tccli mps DescribeAdaptiveDynamicStreamingTemplates --cli-unfold-argument  \
    --Definitions 10001
```

Output: 
```
{
    "Response": {
        "AdaptiveDynamicStreamingTemplateSet": [
            {
                "Comment": "转自适应码流模板1",
                "Definition": 1001,
                "UpdateTime": "2018-10-01T10:00:00Z",
                "DisableHigherVideoBitrate": 1,
                "Name": "转自适应码流模板1",
                "Format": "HLS",
                "DisableHigherVideoResolution": 1,
                "StreamInfos": [
                    {
                        "RemoveVideo": 0,
                        "Audio": {
                            "Codec": "libfdk_aac",
                            "SampleRate": 44100,
                            "AudioChannel": 2,
                            "Bitrate": 200
                        },
                        "Video": {
                            "Fps": 25,
                            "Width": 1080,
                            "Height": 960,
                            "Vcrf": 23,
                            "Codec": "libx264",
                            "ResolutionAdaptive": "open",
                            "FillType": "black",
                            "Bitrate": 1000,
                            "Gop": 50
                        },
                        "RemoveAudio": 0
                    }
                ],
                "Type": "Preset",
                "CreateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

