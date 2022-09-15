**Example 1: 跑批任务列表**



Input: 

```
tccli tione DescribeBatchTasks --cli-unfold-argument  \
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
        "BatchTaskSet": [
            {
                "Status": "xx",
                "UpdateTime": "xx",
                "EndTime": "xx",
                "ModelInfo": {
                    "CosPathInfo": {
                        "Paths": [
                            "xx"
                        ],
                        "Region": "xx",
                        "Bucket": "xx"
                    },
                    "AlgorithmFramework": "xx",
                    "ModelVersion": "xx",
                    "ModelSource": "xx",
                    "ModelType": "xx",
                    "ModelName": "xx",
                    "ModelVersionId": "xx",
                    "ModelId": "xx"
                },
                "BillingInfo": "xx",
                "ImageInfo": {
                    "ImageUrl": "xx",
                    "RegistryRegion": "xx",
                    "RegistryId": "xx",
                    "ImageType": "xx"
                },
                "BatchTaskName": "xx",
                "Outputs": [
                    {
                        "DataSetSource": {
                            "Id": "xx"
                        },
                        "CFSSource": {
                            "Path": "xx",
                            "Id": "xx"
                        },
                        "DataSourceType": "xx",
                        "HDFSSource": {
                            "Path": "xx",
                            "Id": "xx"
                        },
                        "COSSource": {
                            "Paths": [
                                "xx"
                            ],
                            "Region": "xx",
                            "Bucket": "xx"
                        },
                        "MappingPath": "xx"
                    }
                ],
                "Tags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "ResourceGroupName": "xx",
                "RuntimeInSeconds": 1,
                "ResourceGroupId": "xx",
                "BatchTaskId": "xx",
                "ChargeType": "xx",
                "StartTime": "xx",
                "CreateTime": "xx",
                "ChargeStatus": "xx",
                "FailureReason": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

