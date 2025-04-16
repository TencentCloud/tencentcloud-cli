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
                "Id": "abc",
                "Name": "abc",
                "FrameworkName": "abc",
                "FrameworkVersion": "abc",
                "FrameworkEnvironment": "abc",
                "ChargeType": "abc",
                "ChargeStatus": "abc",
                "ResourceGroupId": "abc",
                "ResourceConfigInfos": [
                    {
                        "Role": "abc",
                        "Cpu": 1,
                        "Memory": 1,
                        "GpuType": "abc",
                        "Gpu": 1,
                        "InstanceType": "abc",
                        "InstanceNum": 1,
                        "InstanceTypeAlias": "abc",
                        "RDMAConfig": {
                            "Enable": true
                        }
                    }
                ],
                "TrainingMode": "abc",
                "Status": "abc",
                "RuntimeInSeconds": 1,
                "CreateTime": "abc",
                "StartTime": "abc",
                "EndTime": "abc",
                "Output": {
                    "Bucket": "abc",
                    "Region": "abc",
                    "Paths": [
                        "abc"
                    ]
                },
                "FailureReason": "abc",
                "UpdateTime": "abc",
                "BillingInfo": "abc",
                "ResourceGroupName": "abc",
                "ImageInfo": {
                    "ImageType": "abc",
                    "ImageUrl": "abc",
                    "RegistryRegion": "abc",
                    "RegistryId": "abc"
                },
                "Message": "abc",
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "CallbackUrl": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

