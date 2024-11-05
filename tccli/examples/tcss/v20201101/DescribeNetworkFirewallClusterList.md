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
                "ClusterVersion": "1.0.0",
                "EnableRuleCount": 8,
                "ClusterName": "tke_test",
                "NetworkPolicyPluginError": "   网络插件运行状态非RUNNING",
                "Region": "ap-guangzhou",
                "ClusterId": "cls-jvrv0kf2",
                "ClusterType": "MANAGED_CLUSTER",
                "NetworkPolicyPlugin": "    Kube-router",
                "NetworkPolicyPluginStatus": "Running",
                "ClusterStatus": "Running",
                "ClusterOs": "  ubuntu18.04.1x86_64",
                "ClusterNetworkSettings": "Cilium-Overlay",
                "TotalRuleCount": 5
            }
        ],
        "RequestId": "392f05bd-bf86-4911-8cf9-b8c2ac0f62ab"
    }
}
```

