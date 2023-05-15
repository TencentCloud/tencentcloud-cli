**Example 1: 跑批任务列表**

批量预测任务列表信息

Input: 

```
tccli tione DescribeBatchTasks --cli-unfold-argument  \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.Negative True \
    --Filters.0.Fuzzy True \
    --TagFilters.0.TagKey abc \
    --TagFilters.0.TagValues abc \
    --Offset 1 \
    --Limit 1 \
    --Order abc \
    --OrderField abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "BatchTaskSet": [
            {
                "BatchTaskId": "abc",
                "BatchTaskName": "abc",
                "ModelInfo": {
                    "ModelId": "abc",
                    "ModelName": "abc",
                    "ModelVersionId": "abc",
                    "ModelVersion": "abc",
                    "ModelSource": "abc",
                    "CosPathInfo": {
                        "Bucket": "abc",
                        "Region": "abc",
                        "Paths": [
                            "abc"
                        ]
                    },
                    "AlgorithmFramework": "abc",
                    "ModelType": "abc"
                },
                "ImageInfo": {
                    "ImageType": "abc",
                    "ImageUrl": "abc",
                    "RegistryRegion": "abc",
                    "RegistryId": "abc"
                },
                "ChargeType": "abc",
                "ChargeStatus": "abc",
                "ResourceGroupId": "abc",
                "ResourceConfigInfo": {
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
                },
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "Status": "abc",
                "RuntimeInSeconds": 1,
                "CreateTime": "abc",
                "StartTime": "abc",
                "EndTime": "abc",
                "UpdateTime": "abc",
                "Outputs": [
                    {
                        "MappingPath": "abc",
                        "DataSourceType": "abc",
                        "DataSetSource": {
                            "Id": "abc"
                        },
                        "COSSource": {
                            "Bucket": "abc",
                            "Region": "abc",
                            "Paths": [
                                "abc"
                            ]
                        },
                        "CFSSource": {
                            "Id": "abc",
                            "Path": "abc"
                        },
                        "HDFSSource": {
                            "Id": "abc",
                            "Path": "abc"
                        },
                        "GooseFSSource": {
                            "Id": "abc"
                        }
                    }
                ],
                "ResourceGroupName": "abc",
                "FailureReason": "abc",
                "BillingInfo": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

