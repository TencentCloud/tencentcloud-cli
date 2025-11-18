**Example 1: 查询NAT网关可售卖的可用区信息**



Input: 

```
tccli vpc DescribeNatGatewayZones --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ZoneSet": [
            {
                "Zone": "ap-guangzhou-1",
                "ZoneId": 100001
            },
            {
                "Zone": "ap-guangzhou-2",
                "ZoneId": 100002
            }
        ],
        "RequestId": "6f2a42cf-2905-4fa5-af49-0f01612550de"
    }
}
```

