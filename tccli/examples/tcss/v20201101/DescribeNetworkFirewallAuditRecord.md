**Example 1: 查询集群策略审计列表示例**



Input: 

```
tccli tcss DescribeNetworkFirewallAuditRecord --cli-unfold-argument  \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AuditList": [
            {
                "ClusterName": "tke_test",
                "Region": "ap-guangzhou",
                "ClusterId": "  cls-jvrv0kf2",
                "Uin": "10023234334",
                "NetworkPolicyName": "test",
                "AppId": 346456456,
                "PolicyId": "54645",
                "Action": "add",
                "Operation": "Running",
                "OperationTime": "2024-10-30 12:21:51"
            }
        ],
        "RequestId": "392f05bd-bf86-4911-8cf9-b8c2ac0f62ab"
    }
}
```

