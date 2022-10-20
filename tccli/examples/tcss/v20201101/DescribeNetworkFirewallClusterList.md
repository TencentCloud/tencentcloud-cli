**Example 1: 查询结果**



Input: 

```
tccli tcss DescribeNetworkFirewallClusterList --cli-unfold-argument  \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ClusterInfoList": [
            {
                "ClusterVersion": "xx",
                "EnableRuleCount": 8,
                "ClusterName": "xx",
                "NetworkPolicyPluginError": "xx",
                "Region": "xx",
                "ClusterId": "xx",
                "ClusterType": "xx",
                "NetworkPolicyPlugin": "xx",
                "NetworkPolicyPluginStatus": "xx",
                "ClusterStatus": "xx",
                "ClusterOs": "xx",
                "TotalRuleCount": 5
            }
        ],
        "RequestId": "xx"
    }
}
```

