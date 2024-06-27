**Example 1: 获取转码模板**

获取转码模板

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
                "Definition": "abc",
                "Container": "abc",
                "Name": "abc",
                "Comment": "abc",
                "Type": "abc",
                "RemoveVideo": 0,
                "RemoveAudio": 0,
                "VideoTemplate": {
                    "Codec": "abc",
                    "Fps": 0,
                    "Bitrate": 0,
                    "ResolutionAdaptive": "abc",
                    "Width": 1,
                    "Height": 1,
                    "Gop": 1,
                    "FillType": "abc",
                    "Vcrf": 1,
                    "SegmentType": 0
                },
                "AudioTemplate": {
                    "Codec": "abc",
                    "Bitrate": 0,
                    "SampleRate": 1,
                    "AudioChannel": 0
                },
                "TEHDConfig": {
                    "Type": "abc",
                    "MaxVideoBitrate": 0
                },
                "ContainerType": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "EnhanceConfig": {
                    "VideoEnhance": {
                        "FrameRate": {
                            "Switch": "abc",
                            "Fps": 1
                        },
                        "SuperResolution": {
                            "Switch": "abc",
                            "Type": "abc",
                            "Size": 0
                        },
                        "Hdr": {
                            "Switch": "abc",
                            "Type": "abc"
                        },
                        "Denoise": {
                            "Switch": "abc",
                            "Type": "abc"
                        },
                        "ImageQualityEnhance": {
                            "Switch": "abc",
                            "Type": "abc"
                        },
                        "ColorEnhance": {
                            "Switch": "abc",
                            "Type": "abc"
                        },
                        "SharpEnhance": {
                            "Switch": "abc",
                            "Intensity": 0
                        },
                        "FaceEnhance": {
                            "Switch": "abc",
                            "Intensity": 0
                        },
                        "LowLightEnhance": {
                            "Switch": "abc",
                            "Type": "abc"
                        },
                        "ScratchRepair": {
                            "Switch": "abc",
                            "Intensity": 0
                        },
                        "ArtifactRepair": {
                            "Switch": "abc",
                            "Type": "abc"
                        }
                    },
                    "AudioEnhance": {
                        "Denoise": {
                            "Switch": "abc"
                        },
                        "Separate": {
                            "Switch": "abc",
                            "Type": "abc",
                            "Track": "abc"
                        },
                        "VolumeBalance": {
                            "Switch": "abc",
                            "Type": "abc"
                        },
                        "Beautify": {
                            "Switch": "abc",
                            "Types": [
                                "abc"
                            ]
                        }
                    }
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

