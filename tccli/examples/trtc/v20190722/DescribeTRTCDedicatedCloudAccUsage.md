**Example 1: 查询指定时间范围内用量数据**

查询指定时间范围内用量数据

Input: 

```
tccli trtc DescribeTRTCDedicatedCloudAccUsage --cli-unfold-argument  \
    --StartTime 2026-04-01 00:00:00 \
    --EndTime 2026-04-03 00:00:00 \
    --SdkAppId 1400621940
```

Output: 
```
{
    "Response": {
        "TotalUsage": [
            0
        ],
        "UsageKey": [
            "Time"
        ],
        "UsageList": [
            {
                "TimeKey": "2026-04-01 00:00:00",
                "UsageValue": [
                    0
                ]
            }
        ],
        "RequestId": "3262f482-57c6-4a8d-b1da-888d54e67ab4"
    }
}
```

