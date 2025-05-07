**Example 1: 获取转码模板**

获取转码模板

Input: 

```
tccli mps DescribeTranscodeTemplates --cli-unfold-argument  \
    --Definitions 100010
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TranscodeTemplateSet": [
            {
                "Definition": "100010",
                "Container": "mp4",
                "Name": "MP4-FLU",
                "Comment": "",
                "Type": "Preset",
                "RemoveVideo": 0,
                "RemoveAudio": 0,
                "VideoTemplate": {
                    "Codec": "libx264",
                    "Fps": 25,
                    "Bitrate": 400,
                    "ResolutionAdaptive": "open",
                    "Width": 0,
                    "Height": 360,
                    "FillType": "stretch",
                    "Gop": 0,
                    "VideoProfile": "",
                    "VideoLevel": "",
                    "SegmentType": 0,
                    "FpsDenominator": 1,
                    "Stereo3dType": "",
                    "HlsTime": 0,
                    "Mode": "ABR",
                    "Sar": "",
                    "NoScenecut": 0,
                    "BitDepth": 8,
                    "RawPts": 0,
                    "ScenarioBased": 0,
                    "SceneType": "",
                    "CompressType": ""
                },
                "AudioTemplate": {
                    "Codec": "libfdk_aac",
                    "Bitrate": 64,
                    "SampleRate": 44100,
                    "AudioChannel": 2
                },
                "ContainerType": "Video",
                "CreateTime": "2020-03-04T07:39:36+08:00",
                "UpdateTime": "2024-09-27T17:33:53+08:00",
                "TEHDConfig": null,
                "EnhanceConfig": null,
                "AliasName": ""
            }
        ],
        "RequestId": "817e02a2-abcd-efgh-a2c8-d32169733eaa"
    }
}
```

