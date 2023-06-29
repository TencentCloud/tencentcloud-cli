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
                "ClusterName": "xx",
                "Region": "xx",
                "ClusterId": "xx",
                "Uin": "xx",
                "NetworkPolicyName": "xx",
                "AppId": 0,
                "Action": "xx",
                "Operation": "xx",
                "OperationTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

