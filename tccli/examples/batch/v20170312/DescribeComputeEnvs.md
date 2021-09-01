**Example 1: 查看计算环境列表**



Input: 

```
tccli batch DescribeComputeEnvs --cli-unfold-argument  \
    --EnvIds env-lcx7qbbr
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ComputeEnvSet": [
            {
                "EnvId": "env-lcx7qbbr",
                "ComputeNodeMetrics": {
                    "CreatedCount": 0,
                    "DeletingCount": 0,
                    "CreationFailedCount": 0,
                    "SubmittedCount": 0,
                    "CreatingCount": 0,
                    "AbnormalCount": 1,
                    "RunningCount": 0
                },
                "Tags": [
                    {
                        "Key": "batch-test-tag-env-key",
                        "Value": "batch-test-tag-env-value"
                    }
                ],
                "ResourceType": "CVM",
                "EnvType": "MANAGED",
                "AttachedComputeNodeCount": 0,
                "DesiredComputeNodeCount": 1,
                "EnvName": "test-compute-env",
                "Placement": {
                    "Zone": "ap-guangzhou-4"
                },
                "NextAction": "",
                "CreateTime": "2020-09-22T06:51:42Z"
            }
        ],
        "RequestId": "bedb1750-a09f-4c4d-9f25-6afccda50dea"
    }
}
```

