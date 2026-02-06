**Example 1: 训练任务列表**

获取训练任务列表

Input: 

```
tccli tione DescribeTrainingTasks --cli-unfold-argument  \
    --Filters.0.Fuzzy True \
    --Filters.0.Values string \
    --Filters.0.Name string \
    --Filters.0.Negative True \
    --TagFilters.0.TagValues string \
    --TagFilters.0.TagKey string \
    --Limit 1 \
    --OrderField string \
    --Offset 1 \
    --Order string
```

Output: 
```
{
    "Response": {
        "TrainingTaskSet": [
            {
                "Id": "train-fd",
                "Name": "testname",
                "FrameworkName": "pytorch",
                "FrameworkVersion": "v1",
                "FrameworkEnvironment": "testenv",
                "ChargeType": "PREPAID",
                "ChargeStatus": "PAID",
                "ResourceGroupId": "rsg-dfs",
                "ResourceConfigInfos": [
                    {
                        "Role": "worker",
                        "Cpu": 1,
                        "Memory": 1,
                        "GpuType": "A100",
                        "Gpu": 1,
                        "InstanceType": "instype-a",
                        "InstanceNum": 1,
                        "InstanceTypeAlias": "instype-ab",
                        "RDMAConfig": {
                            "Enable": true
                        }
                    }
                ],
                "TrainingMode": "DDP",
                "Status": "RUNNING",
                "RuntimeInSeconds": 1,
                "CreateTime": "2025-11-21 00:00:00",
                "StartTime": "2025-11-21 00:00:00",
                "EndTime": "2025-11-21 01:00:00",
                "Output": {
                    "Bucket": "testbucket",
                    "Region": "ap-nanjing",
                    "Paths": [
                        "/"
                    ]
                },
                "FailureReason": "",
                "UpdateTime": "2025-11-21 00:00:00",
                "BillingInfo": "",
                "ResourceGroupName": "rsg-fsdf",
                "ImageInfo": {
                    "ImageType": "TCR",
                    "ImageUrl": "image/url",
                    "RegistryRegion": "ap-nanjing",
                    "RegistryId": "tcr-234"
                },
                "Message": "test message",
                "Tags": [
                    {
                        "TagKey": "key",
                        "TagValue": "value"
                    }
                ],
                "CallbackUrl": "callback/url"
            }
        ],
        "TotalCount": 1,
        "RequestId": "fdsljfl-dfsafds-xxf"
    }
}
```

