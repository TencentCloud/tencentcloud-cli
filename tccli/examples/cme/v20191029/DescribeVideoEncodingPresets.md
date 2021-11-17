**Example 1: 指定 ID 查询配置**



Input: 

```
tccli cme DescribeVideoEncodingPresets --cli-unfold-argument  \
    --Platform test \
    --Ids 100047
```

Output: 
```
{
    "Response": {
        "RequestId": "46ada659-495d-43b3-88c8-64dad423007d",
        "TotalCount": 1,
        "VideoEncodingPresetSet": [
            {
                "AudioSetting": {
                    "Bitrate": 64000,
                    "Channels": 2,
                    "Codec": "AAC",
                    "SampleRate": 16000
                },
                "Container": "mp4",
                "Id": 100047,
                "Name": "",
                "RemoveAudio": 0,
                "RemoveVideo": 0,
                "VideoSetting": {
                    "Bitrate": 0,
                    "Codec": "H264",
                    "ShortEdge": 1080
                }
            }
        ]
    }
}
```

**Example 2: 按照分页查询配置**



Input: 

```
tccli cme DescribeVideoEncodingPresets --cli-unfold-argument  \
    --Platform test \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "RequestId": "f16e0eea-20d0-4716-8195-599df164d8b4",
        "TotalCount": 32,
        "VideoEncodingPresetSet": [
            {
                "AudioSetting": {
                    "Bitrate": 64000,
                    "Channels": 2,
                    "Codec": "AAC",
                    "SampleRate": 16000
                },
                "Container": "mp4",
                "Id": 100047,
                "Name": "",
                "RemoveAudio": 0,
                "RemoveVideo": 0,
                "VideoSetting": {
                    "Bitrate": 0,
                    "Codec": "H264",
                    "ShortEdge": 1080
                }
            },
            {
                "AudioSetting": {
                    "Bitrate": 64000,
                    "Channels": 1,
                    "Codec": "AAC",
                    "SampleRate": 32000
                },
                "Container": "mp4",
                "Id": 100048,
                "Name": "test1",
                "RemoveAudio": 0,
                "RemoveVideo": 0,
                "VideoSetting": {
                    "Bitrate": 131072,
                    "Codec": "H264",
                    "ShortEdge": 1024
                }
            }
        ]
    }
}
```

