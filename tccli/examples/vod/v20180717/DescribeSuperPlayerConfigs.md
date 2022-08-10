**Example 1: 获取播放器配置列表**



Input: 

```
tccli vod DescribeSuperPlayerConfigs --cli-unfold-argument  \
    --Names test
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "PlayerConfigSet": [
            {
                "Name": "test",
                "Type": "Custom",
                "DrmSwitch": "OFF",
                "AdaptiveDynamicStreamingDefinition": 10,
                "ImageSpriteDefinition": 10,
                "ResolutionNameSet": [
                    {
                        "MinEdgeLength": 480,
                        "Name": "标清"
                    },
                    {
                        "MinEdgeLength": 1440,
                        "Name": "2K"
                    }
                ],
                "TranscodeDefinition": 0,
                "AudioVideoType": "AdaptiveDynamicStream",
                "Domain": "xxx.vod2.myqcloud.com",
                "Scheme": "HTTPS",
                "Comment": "",
                "DrmStreamingsInfo": {
                    "FairPlayDefinition": 0,
                    "SimpleAesDefinition": 0,
                    "WidevineDefinition": 0
                },
                "CreateTime": "2019-10-11T10:00:00Z",
                "UpdateTime": "2019-10-11T10:00:00Z"
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-4594145287e1"
    }
}
```

