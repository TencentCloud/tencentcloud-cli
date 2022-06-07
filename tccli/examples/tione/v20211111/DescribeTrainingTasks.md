**Example 1: 训练任务列表**



Input: 

```
tccli tione DescribeTrainingTasks --cli-unfold-argument  \
    --Filters.0.Fuzzy True \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.Negative True \
    --TagFilters.0.TagValues xx \
    --TagFilters.0.TagKey xx \
    --Limit 1 \
    --OrderField xx \
    --Offset 1 \
    --Order xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TrainingTaskSet": [
            {
                "Status": "xx",
                "UpdateTime": "xx",
                "EndTime": "xx",
                "Name": "xx",
                "BillingInfo": "xx",
                "Tags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "ResourceGroupId": "xx",
                "ResourceConfigInfos": [
                    {
                        "InstanceType": "xx",
                        "InstanceNum": 1,
                        "Cpu": 1,
                        "Role": "xx",
                        "Memory": 1,
                        "Gpu": 1,
                        "GpuType": "xx",
                        "InstanceTypeAlias": "xx"
                    }
                ],
                "ResourceGroupName": "xx",
                "CreateTime": "xx",
                "RuntimeInSeconds": 1,
                "ImageInfo": {
                    "ImageUrl": "xx",
                    "RegistryRegion": "xx",
                    "RegistryId": "xx",
                    "ImageType": "xx"
                },
                "FrameworkName": "xx",
                "ChargeType": "xx",
                "StartTime": "xx",
                "Output": {
                    "Paths": [
                        "xx"
                    ],
                    "Region": "xx",
                    "Bucket": "xx"
                },
                "TrainingMode": "xx",
                "FrameworkVersion": "xx",
                "Id": "xx",
                "ChargeStatus": "xx",
                "FailureReason": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

