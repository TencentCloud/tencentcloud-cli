**Example 1: 查询节点类型的影响范围示例**



Input: 

```
tccli tcss DescribeAffectedNodeList --cli-unfold-argument  \
    --Limit 2 \
    --CheckItemId 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "d2cf3a82-f75e-49f3-b2ea-d1f9172062db",
        "TotalCount": 6,
        "AffectedNodeList": [
            {
                "ClusterId": "cls-0zmsjvko",
                "ClusterName": "wk独立集群",
                "InstanceId": "ins-afynf7mw",
                "PrivateIpAddresses": "10.0.2.7",
                "InstanceRole": "WORKER",
                "ClusterVersion": "1.18.4",
                "ContainerRuntime": "docker",
                "Region": "ap-guangzhou",
                "VerifyInfo": "Runc 版本为 1.0.0-rc10"
            },
            {
                "ClusterId": "cls-0zmsjvko",
                "ClusterName": "wk独立集群",
                "InstanceId": "ins-9l567jse",
                "PrivateIpAddresses": "10.0.2.42",
                "InstanceRole": "WORKER",
                "ClusterVersion": "1.18.4",
                "ContainerRuntime": "docker",
                "Region": "ap-guangzhou",
                "VerifyInfo": "Runc 版本为 1.0.0-rc10"
            }
        ]
    }
}
```

