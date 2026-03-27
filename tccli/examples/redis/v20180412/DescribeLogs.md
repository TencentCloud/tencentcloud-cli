**Example 1: 请求示例**



Input: 

```
tccli redis DescribeLogs --cli-unfold-argument  \
    --InstanceId crs-k2vh**** \
    --StartTime 2025-12-11 14:00:09 \
    --EndTime 2025-12-11 14:50:09 \
    --LogType auditLog
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CacheCode": "b606eeb",
                "ClientAddr": "************:****",
                "CommandDetail": "set ****-audit-test-*** 1",
                "CommandLatency": 1,
                "CommandType": "WRITE",
                "Timestamp": "2025-12-11 14:49:40.815",
                "DBId": 0,
                "ErrMsg": "",
                "UserName": "default"
            }
        ],
        "TotalCount": 10,
        "RequestId": "4f90d880-5c00-4e3c-a153-12b7f2e18226"
    }
}
```

