**Example 1: 获取坐席实时状态统计指标示例**

获取坐席实时状态统计指标示例。

Input: 

```
tccli ccc DescribeStaffStatusMetrics --cli-unfold-argument  \
    --SdkAppId 0 \
    --StaffList aaa@abc.com \
    --GroupIdList 0 \
    --StatusList free
```

Output: 
```
{
    "Response": {
        "Metrics": [
            {
                "Email": "aaa@abc.com",
                "Status": "free",
                "StatusExtra": {
                    "Type": "tel",
                    "Direct": "callin"
                },
                "OnlineDuration": 0,
                "FreeDuration": 0,
                "BusyDuration": 0,
                "NotReadyDuration": 0,
                "RestDuration": 0,
                "AfterCallWorkDuration": 0,
                "Reason": "abc",
                "ReserveRest": true,
                "ReserveNotReady": true,
                "UseMobileAccept": 0,
                "UseMobileCallOut": true,
                "LastOnlineTimestamp": 0,
                "LastStatusTimestamp": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

