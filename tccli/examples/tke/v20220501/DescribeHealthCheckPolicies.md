**Example 1: 创建托管节点池健康检测规则**



Input: 

```
tccli tke DescribeHealthCheckPolicies --cli-unfold-argument  \
    --Filters.0.Values A \
    --Filters.0.Name HealthCheckPolicyName \
    --ClusterId cls-4h43fuxj
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
        "RequestId": "9bd42c72-dd16-46bc-9d1e-b4020c59fab8"
    }
}
```

