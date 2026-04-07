**Example 1: 调用示例**

查询SSAI用量

Input: 

```
tccli mps DescribeStreamPackageSSAIUsage --cli-unfold-argument  \
    --StartTime 2025-05-01T00+08:00 \
    --EndTime 2025-05-01T10+08:00
```

Output: 
```
{
    "Response": {
        "Info": {
            "AdRequestSuccess": 1,
            "AdRequestFail": 0,
            "Impression": 0,
            "AdMarkerTime": 0,
            "ReplacedTime": 0,
            "MidFillRate": 0,
            "PreReqNum": 1,
            "PreReplacedNum": 0,
            "PreReplaceRate": 0,
            "UsageDetails": [
                {
                    "UniqId": "018f141593c91ea540e603706c52",
                    "ChannelId": "66503E8E0000930000F9",
                    "ChannelName": "ssai_channel",
                    "AdType": "Preroll",
                    "AdRequestSuccess": 1,
                    "AdRequestFail": 0,
                    "Impression": 0,
                    "Start": 0,
                    "FirstQuarter": 0,
                    "Midpoint": 0,
                    "ThirdQuarter": 0,
                    "Complete": 0,
                    "AdMarkerTime": 0,
                    "ReplacedTime": 0,
                    "MidFillRate": 0,
                    "PreReqNum": 1,
                    "PreReplacedNum": 0,
                    "PreReplaceRate": 0
                }
            ]
        },
        "RequestId": "req-xxx123"
    }
}
```

