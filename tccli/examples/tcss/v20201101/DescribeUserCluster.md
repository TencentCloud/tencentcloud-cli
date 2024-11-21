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
        "ClusterInfoList": [
            {
                "AccessedStatus": "AccessedPartialDefence",
                "AccessedSubStatus": "AccessedSubNone",
                "ChargeCoresCnt": 4000,
                "CheckFailReason": "SUCCESS",
                "CheckStatus": "HasRisk",
                "ClusterAuditFailedInfo": "",
                "ClusterAuditStatus": "Opened",
                "ClusterAutoCheck": false,
                "ClusterCheckMode": "",
                "ClusterId": "cls-abhq0j4o",
                "ClusterName": "bx_test_tmp",
                "ClusterNodeNum": 4,
                "ClusterOs": "",
                "ClusterStatus": "CSR_RUNNING",
                "ClusterSubStatus": "",
                "ClusterType": "INDEPENDENT_CLUSTER",
                "ClusterVersion": "1.28.3",
                "CoresCnt": 12000,
                "DefenderErrorReason": "",
                "DefenderStatus": "UnDefended",
                "HighRiskCount": 6,
                "HintRiskCount": 3,
                "MasterAddresses": [
                    "10.0.0.11;10.0.0.14;10.0.0.4;"
                ],
                "MiddleRiskCount": 7,
                "NodeCount": 4,
                "OffLineNodeCount": 0,
                "Region": "ap-guangzhou",
                "SeriousRiskCount": 1,
                "TaskCreateTime": "2024-10-30 14:41:25",
                "UnInstallAgentNodeCount": 1,
                "UnreadyNodeNum": 3
            }
        ],
        "RequestId": "8a64a4f9-864c-49c6-adcb-21b483de477a",
        "TotalCount": 7
    }
}
```

