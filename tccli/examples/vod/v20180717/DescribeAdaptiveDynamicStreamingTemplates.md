**Example 1: 查询转自适应码流模板列表**



Input: 

```
tccli vod DescribeAdaptiveDynamicStreamingTemplates --cli-unfold-argument  \
    --Definitions 10001
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AdaptiveDynamicStreamingTemplateSet": [
            {
                "Definition": 1001,
                "Type": "Custom",
                "Name": "转自适应码流模板1",
                "Format": "HLS",
                "Comment": "",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z",
                "DrmType": "",
                "DisableHigherVideoResolution": 0,
                "DisableHigherVideoBitrate": 0,
                "StreamInfos": [
                    {
                        "RemoveVideo": 0,
                        "Audio": {
                            "Codec": "libfdk_aac",
                            "SampleRate": 44100,
                            "AudioChannel": 2,
                            "Bitrate": 128
                        },
                        "Video": {
                            "Fps": 25,
                            "Width": 720,
                            "Height": 1080,
                            "Codec": "libx264",
                            "ResolutionAdaptive": "open",
                            "FillType": "black",
                            "Bitrate": 12500,
                            "Vcrf": 23,
                            "Gop": 0
                        },
                        "RemoveAudio": 0,
                        "TEHDConfig": {
                            "MaxVideoBitrate": 10000,
                            "Type": "TEHD-100"
                        }
                    }
                ]
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

