**Example 1: 获取恶意请求策略列表**



Input: 

```
tccli cwp DescribeRiskDnsPolicyList --cli-unfold-argument  \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "PolicyId": 1001,
                "PolicyName": "系统规则(重保)",
                "PolicyType": 0,
                "PolicyDesc": "系统规则(重保)",
                "PolicyAction": 0,
                "HostScope": 1,
                "HostIds": [],
                "Domains": [
                    ""
                ],
                "IsEnabled": 1,
                "IsDealOldEvent": 0,
                "EventId": 0,
                "UpdateTime": "2022-09-19 17:12:01"
            }
        ],
        "RequestId": "a8a04837-4318-4a21-8a05-7096ed84062c",
        "TotalCount": 21
    }
}
```

