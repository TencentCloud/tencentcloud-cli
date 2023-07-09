**Example 1: 查询云原生网关灰度规则列表**

查询云原生网关灰度规则列表

Input: 

```
tccli tse DescribeCloudNativeAPIGatewayCanaryRules --cli-unfold-argument  \
    --GatewayId abc \
    --ServiceId abc \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "CanaryRuleList": [
                {
                    "Priority": 0,
                    "Enabled": true,
                    "ConditionList": [
                        {
                            "Type": "abc",
                            "Key": "abc",
                            "Operator": "abc",
                            "Value": "abc",
                            "Delimiter": "abc",
                            "GlobalConfigId": "abc",
                            "GlobalConfigName": "abc"
                        }
                    ],
                    "BalancedServiceList": [
                        {
                            "ServiceID": "abc",
                            "ServiceName": "abc",
                            "UpstreamName": "abc",
                            "Percent": 0
                        }
                    ],
                    "ServiceId": "abc",
                    "ServiceName": "abc"
                }
            ],
            "TotalCount": 0
        },
        "RequestId": "abc"
    }
}
```

