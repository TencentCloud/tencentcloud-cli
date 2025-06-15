**Example 1: 查询原生节点池健康检测策略模板**



Input: 

```
tccli tke DescribeHealthCheckTemplate --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "HealthCheckTemplate": {
            "Rules": [
                {
                    "Name": "A",
                    "Description": "",
                    "RepairAction": "restart",
                    "RepairEffect": "",
                    "ShouldEnable": true,
                    "ShouldRepair": false,
                    "Severity": "general"
                }
            ]
        },
        "RequestId": "123"
    }
}
```

