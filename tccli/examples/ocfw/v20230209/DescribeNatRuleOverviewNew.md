**Example 1: NAT边界规则概览**

NAT边界规则概览

Input: 

```
tccli ocfw DescribeNatRuleOverviewNew --cli-unfold-argument  \
    --CurrentAppId 0 \
    --Area abc
```

Output: 
```
{
    "Response": {
        "InTotal": 0,
        "InEnableNum": 0,
        "OutTotal": 0,
        "OutEnableNum": 0,
        "InstanceId": "abc",
        "InstanceName": "abc",
        "RequestId": "abc"
    }
}
```

