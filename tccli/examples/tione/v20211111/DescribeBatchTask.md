**Example 1: 查询跑批任务**

查看单个离线批处理任务详情

Input: 

```
tccli tione DescribeBatchTask --cli-unfold-argument  \
    --BatchTaskId xx
```

Output: 
```
{
    "Response": {
        "BatchTaskDetail": {
            "BatchTaskName": "xx",
            "BatchTaskId": "xx",
            "EndTime": "xx",
            "SubUin": "xx",
            "ChargeStatus": "xx",
            "Status": "xx",
            "UpdateTime": "xx",
            "VpcId": "xx",
            "Tags": [
                {
                    "TagKey": "xx",
                    "TagValue": "xx"
                }
            ],
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
            "PodList": [
                "batch-xxx-xxx-worker-0"
            ],
            "CodePackagePath": {
                "Paths": [
                    "xx"
                ],
                "Region": "xx",
                "Bucket": "xx"
            },
            "ResourceGroupId": "xx",
            "LatestInstanceId": "xx",
            "SubnetId": "xx",
            "DataConfigs": [
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
            "FailureReason": "xx",
            "Remark": "xx",
            "StartTime": "xx",
            "BillingInfo": "xx",
            "Region": "xx",
            "ResourceGroupName": "xx",
            "LogEnable": true,
            "ModelInfo": {
                "ModelName": "xx",
                "ModelVersion": "xx",
                "ModelSource": "xx",
                "ModelType": "xx",
                "AlgorithmFramework": "xx",
                "ModelVersionId": "xx",
                "ModelId": "xx"
            },
            "ImageInfo": {
                "ImageUrl": "xx",
                "RegistryRegion": "xx",
                "RegistryId": "xx",
                "ImageType": "xx"
            },
            "Uin": "xx",
            "RuntimeInSeconds": 1,
            "ResourceConfigInfo": {
                "InstanceType": "xx",
                "InstanceNum": 1,
                "Cpu": 1,
                "Role": "xx",
                "Memory": 1,
                "Gpu": 1,
                "GpuType": "xx",
                "InstanceTypeAlias": "xx"
            },
            "ChargeType": "xx",
            "CreateTime": "xx",
            "StartCmd": "xx",
            "LogConfig": {
                "TopicId": "xx",
                "LogsetId": "xx"
            }
        },
        "RequestId": "xx"
    }
}
```

