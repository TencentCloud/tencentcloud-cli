**Example 1: 示例1**



Input: 

```
tccli cwp DescribeClientException --cli-unfold-argument  \
    --EndTime 2020-11-21 15:16:00 \
    --Limit 10 \
    --ExceptionType 1 \
    --StartTime 2020-11-21 15:16:00 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "HostIP": "172.23.16.2",
                "InstanceID": "ins-kz85kljw",
                "Uuid": "2e6353e4-0498-450a-9be5-77e2537247f6",
                "OfflineTime": "2022-04-24T17:52:37+08:00",
                "UninstallTime": "2020-11-21 15:16:00",
                "UninstallCmd": "sh ******"
            }
        ],
        "RequestId": "1248a7df-c3fe-4930-b3ff-2af956cf8d66",
        "TotalCount": 944
    }
}
```

