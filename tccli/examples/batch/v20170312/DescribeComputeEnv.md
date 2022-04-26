**Example 1: 查看计算环境详细信息**



Input: 

```
tccli batch DescribeComputeEnv --cli-unfold-argument  \
    --EnvId env-lcpcej85
```

Output: 
```
{
    "Response": {
        "EnvId": "env-lcpcej85",
        "ComputeNodeMetrics": {
            "CreatedCount": 0,
            "DeletingCount": 0,
            "CreationFailedCount": 0,
            "SubmittedCount": 0,
            "CreatingCount": 0,
            "AbnormalCount": 1,
            "RunningCount": 1
        },
        "ResourceType": "CVM",
        "EnvType": "MANAGED",
        "CreateTime": "2018-03-08T11:48:43Z",
        "EnvName": "test compute env",
        "NextAction": "",
        "Placement": {
            "Zone": "ap-guangzhou-2"
        },
        "ComputeNodeSet": [
            {
                "ComputeNodeId": "node-noa8vefu",
                "ComputeNodeState": "ABNORMAL",
                "Mem": 2,
                "ResourceCreatedTime": "2018-03-08T11:49:17Z",
                "ResourceType": "CVM",
                "ResourceOrigin": "BATCH_CREATED",
                "ComputeNodeInstanceId": "ins-0kj3gz6s",
                "AgentVersion": "1.1.9",
                "TaskInstanceNumAvailable": 1,
                "Cpu": 1,
                "PublicIpAddresses": [
                    "132.20.19.18"
                ],
                "PrivateIpAddresses": [
                    "10.10.8.3"
                ]
            },
            {
                "ComputeNodeId": "node-9yzd5jei",
                "ComputeNodeState": "RUNNING",
                "Mem": 2,
                "ResourceCreatedTime": "2018-03-09T13:15:44Z",
                "ResourceType": "CVM",
                "ResourceOrigin": "BATCH_CREATED",
                "ComputeNodeInstanceId": "ins-jyafz2sk",
                "AgentVersion": "1.1.9",
                "TaskInstanceNumAvailable": 1,
                "Cpu": 1,
                "PublicIpAddresses": [
                    "132.20.19.18"
                ],
                "PrivateIpAddresses": [
                    "10.10.8.3"
                ]
            }
        ],
        "DesiredComputeNodeCount": 2,
        "AttachedComputeNodeCount": 0,
        "Tags": [
            {
                "Key": "batch-test-tag-env-key",
                "Value": "batch-test-tag-env-value1"
            }
        ],
        "RequestId": "274cbd4f-77d2-4bf6-9984-643318ed3ef8"
    }
}
```

