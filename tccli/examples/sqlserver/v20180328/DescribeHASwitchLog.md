**Example 1: 查询实例主备切换日志**



Input: 

```
tccli sqlserver DescribeHASwitchLog --cli-unfold-argument  \
    --InstanceId mssql-98aiauan \
    --SwitchType 1 \
    --StartTime 2023-01-01 00:00:00 \
    --EndTime 2023-01-01 00:01:00 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "863b2797-858b-49f3-88e9-50159e564cbc",
        "TotalCount": 1,
        "SwitchLog": [
            {
                "EventId": "f39bc24b76d1c5d3ce60f0dcb9e0bd79",
                "SwitchType": 1,
                "StartTime": "2023-01-01 00:00:00",
                "EndTime": "2023-01-01 00:01:00",
                "Reason": "AUTO"
            }
        ]
    }
}
```

