**Example 1: 查询指定时间范围内音频审核数据**

查询指定时间范围内数据

Input: 

```
tccli trtc DescribeTRTCSegmentModerationUsage --cli-unfold-argument  \
    --StartTime 2026-04-01 00:00:00 \
    --EndTime 2026-04-10 00:00:00 \
    --Type audio \
    --Business 0
```

Output: 
```
{
    "Response": {
        "TotalUsage": [
            0
        ],
        "UsageKey": [
            "Audio"
        ],
        "UsageList": [
            {
                "TimeKey": "2026-04-01 00:00:00",
                "UsageValue": [
                    0
                ]
            }
        ],
        "RequestId": "e5783938-a9c4-451f-9b17-7db9c8635a96"
    }
}
```

**Example 2: 查询指定时间范围内图片切片用量数据**

查询指定时间范围内图片切片用量数据

Input: 

```
tccli trtc DescribeTRTCSegmentModerationUsage --cli-unfold-argument  \
    --StartTime 2026-04-01 00:00:00 \
    --EndTime 2026-04-10 00:00:00 \
    --Type picture \
    --Business 1
```

Output: 
```
{
    "Response": {
        "TotalUsage": [
            0
        ],
        "UsageKey": [
            "Picture"
        ],
        "UsageList": [
            {
                "TimeKey": "2026-04-01 00:00:00",
                "UsageValue": [
                    0
                ]
            }
        ],
        "RequestId": "3164f896-1141-4d6d-88da-8e757ce65360"
    }
}
```

