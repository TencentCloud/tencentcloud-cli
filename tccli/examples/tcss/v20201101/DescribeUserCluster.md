**Example 1: 查询用户集群列表**

查询用户集群列表

Input: 

```
tccli tcss DescribeUserCluster --cli-unfold-argument  \
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
                "ClusterId": "abc",
                "ClusterName": "abc",
                "ClusterVersion": "abc",
                "ClusterOs": "abc",
                "ClusterType": "abc",
                "ClusterNodeNum": 1,
                "Region": "abc",
                "DefenderStatus": "abc",
                "ClusterStatus": "abc",
                "ClusterCheckMode": "abc",
                "ClusterAutoCheck": true,
                "DefenderErrorReason": "abc",
                "UnreadyNodeNum": 1,
                "SeriousRiskCount": 0,
                "HighRiskCount": 0,
                "MiddleRiskCount": 0,
                "HintRiskCount": 0,
                "CheckFailReason": "abc",
                "CheckStatus": "abc",
                "TaskCreateTime": "abc",
                "AccessedStatus": "abc",
                "AccessedSubStatus": "abc",
                "NodeCount": 1,
                "OffLineNodeCount": 1,
                "UnInstallAgentNodeCount": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

