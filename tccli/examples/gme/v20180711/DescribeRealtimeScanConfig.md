**Example 1: 获取用户自定义送检信息**



Input: 

```
tccli gme DescribeRealtimeScanConfig --cli-unfold-argument  \
    --BizId 1
```

Output: 
```
{
    "Response": {
        "BizId": 1,
        "UserIdRegex": [
            "xx"
        ],
        "UserIdString": "xx",
        "ErrorCode": 0,
        "AuditType": 0,
        "RequestId": "xx",
        "RoomIdRegex": [
            "xx"
        ],
        "RoomIdString": "xx"
    }
}
```

