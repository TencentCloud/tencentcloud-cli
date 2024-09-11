**Example 1: 创建托管节点池健康检测规则**



Input: 

```
tccli tke DescribeHealthCheckPolicies --cli-unfold-argument  \
    --Filters.0.Values A \
    --Filters.0.Name HealthCheckPolicyName \
    --ClusterId xx
```

Output: 
```
{
    "Response": {
        "HealthCheckPolicies": [
            {
                "Name": "NP1",
                "Rules": [
                    {
                        "Name": "A",
                        "Enabled": true,
                        "AutoRepairEnabled": false
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

