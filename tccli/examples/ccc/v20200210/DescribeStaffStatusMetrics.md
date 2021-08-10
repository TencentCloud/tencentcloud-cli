**Example 1: 获取坐席实时状态统计指标示例**



Input: 

```
tccli ccc DescribeStaffStatusMetrics --cli-unfold-argument  \
    --SdkAppId 0 \
    --StaffList xx
```

Output: 
```
{
    "Response": {
        "Metrics": [
            {
                "Status": "free",
                "BusyDuration": 63,
                "NotReadyDuration": 39175,
                "ReserveRest": false,
                "ReserveNotReady": false,
                "Reason": "xx",
                "OnlineDuration": 54548,
                "AfterCallWorkDuration": 15,
                "FreeDuration": 15253,
                "StatusExtra": {
                    "Type": "xx",
                    "Direct": "xx"
                },
                "RestDuration": 41,
                "Email": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

