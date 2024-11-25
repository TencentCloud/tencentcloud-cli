**Example 1: 查询云原生网关灰度规则列表**

查询云原生网关灰度规则列表

Input: 

```
tccli tse DescribeCloudNativeAPIGatewayCanaryRules --cli-unfold-argument  \
    --GatewayId gateway-18f786a \
    --ServiceId 6abf620f-c6b9-4440-b90c-56c165225cfc \
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
                            "Type": "query",
                            "Key": "app",
                            "Operator": "==",
                            "Value": "learn",
                            "Delimiter": ",",
                            "GlobalConfigId": "4fe634e9-ea28-4f1e-8461-da89f3b84d28",
                            "GlobalConfigName": "global-rule1"
                        }
                    ],
                    "BalancedServiceList": [
                        {
                            "ServiceID": "6abf620f-c6b9-4440-b90c-56c165225cfc",
                            "ServiceName": "svc1",
                            "UpstreamName": "abc",
                            "Percent": 0
                        }
                    ],
                    "ServiceId": "6abf620f-c6b9-4440-b90c-56c165225cfc",
                    "ServiceName": "svc1"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "741e4e82-371d-48de-a843-867c69ff114d"
    }
}
```

