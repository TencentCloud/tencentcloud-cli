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
                            "Key": "abc",
                            "Operator": "==",
                            "Value": "abc",
                            "Delimiter": "abc",
                            "GlobalConfigId": "abc",
                            "GlobalConfigName": "abc"
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

