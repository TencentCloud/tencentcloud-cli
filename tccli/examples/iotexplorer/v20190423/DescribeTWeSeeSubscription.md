**Example 1: 查询 TWeSee 视频理解订阅**



Input: 

```
tccli iotexplorer DescribeTWeSeeSubscription --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ServiceType VID_COMP \
    --ChannelId 0
```

Output: 
```
{
    "Response": {
        "ComprehensionConfig": {
            "AlternativeOutputLang": "en",
            "DetectTypes": [
                "person_climbing_fence"
            ],
            "EnableSearch": true,
            "MultiCameraLayout": "Vertical,Num=2,Index=0;1",
            "OutputLang": "zh"
        },
        "Enabled": true,
        "EventIdFilterConfig": {
            "IncludeOnly": [
                "_sys_id1_data"
            ]
        },
        "ExpireTime": 1781897528,
        "QuotaBasic": 3000,
        "QuotaRefreshTime": 1779219128,
        "QuotaUsedBasic": 2,
        "ResourceId": "twesee-753yd29x30********jqww1",
        "ServiceTier": "BASIC",
        "Status": "NORMAL",
        "RequestId": "a94ccccd-a34e-4daa-97fe-fed5a0c2f1c0"
    }
}
```

