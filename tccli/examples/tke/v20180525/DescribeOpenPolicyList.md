**Example 1: 查询策略列表**



Input: 

```
tccli tke DescribeOpenPolicyList --cli-unfold-argument  \
    --ClusterId cls-gzzr1v5t \
    --Category baseline
```

Output: 
```
{
    "Response": {
        "GatekeeperStatus": 1,
        "OpenPolicyInfoList": [
            {
                "ConstraintYamlExample": "",
                "EnabledStatus": "open",
                "EnforcementAction": "deny",
                "EventNums": 0,
                "Kind": "blockclusterdeletion",
                "Name": "block-cluster-deletion-rule",
                "OpenConstraintInfoList": [
                    {
                        "EventNums": 0,
                        "Name": "block-cluster-deletion-rule",
                        "YamlDetail": ""
                    }
                ],
                "PolicyCategory": "cluster",
                "PolicyDesc": "集群中存在任意节点（普通节点、原生节点、注册节点），需先下线节点后方可删除",
                "PolicyName": "存在节点的集群不允许删除"
            }
        ],
        "RequestId": "224782f1-c990-4383-8f21-bb369c9ca396"
    }
}
```

