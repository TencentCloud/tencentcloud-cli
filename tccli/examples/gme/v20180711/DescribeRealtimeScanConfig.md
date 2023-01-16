**Example 1: 获取用户自定义送检信息**

获取用户自定义送检信息

Input: 

```
tccli gme DescribeRealtimeScanConfig --cli-unfold-argument  \
    --BizId 1400000000
```

Output: 
```
{
    "Response": {
        "BizId": 1400000000,
        "UserIdRegex": [
            "^[0-9]*$"
        ],
        "UserIdString": "0001,0002,0003",
        "ErrorCode": 0,
        "AuditType": 0,
        "RequestId": "5e60ecbe-24f7-4821-ac4f-c9410b491277",
        "RoomIdRegex": [
            "^[0-9]*$"
        ],
        "RoomIdString": "0001,0002,0003"
    }
}
```

