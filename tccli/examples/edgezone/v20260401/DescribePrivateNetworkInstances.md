**Example 1: 根据可用区查询私网实例**



Input: 

```
tccli edgezone DescribePrivateNetworkInstances --cli-unfold-argument  \
    --ZoneId ap-beijing \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "test-req-013",
        "TotalCount": 1,
        "PrivateNetworkInstanceSet": [
            {
                "NetworkInstanceId": "ein-a1b2c3d4",
                "ZoneId": "ap-beijing-a",
                "NetworkInstanceName": "test-pri-instance",
                "Network": "10.0.0.0",
                "Mask": 24,
                "ServerCount": 3,
                "AvailableIpCount": 251,
                "CreatedAt": "2026-04-07T00:00:00",
                "UpdatedAt": "2026-04-07T00:00:00"
            }
        ]
    }
}
```

