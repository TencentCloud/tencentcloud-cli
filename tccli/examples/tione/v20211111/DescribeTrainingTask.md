**Example 1: 训练任务详情**



Input: 

```
tccli tione DescribeTrainingTask --cli-unfold-argument  \
    --Id xx
```

Output: 
```
{
    "Response": {
        "TrainingTaskDetail": {
            "Id": "xx",
            "StartTime": "xx",
            "FrameworkName": "xx",
            "TrainingMode": "xx",
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
            "CodePackagePath": {
                "Paths": [
                    "xx"
                ],
                "Region": "xx",
                "Bucket": "xx"
            },
            "TuningParameters": "xx",
            "ResourceGroupId": "xx",
            "TensorBoardId": "xx",
            "LatestInstanceId": "xx",
            "SubnetId": "xx",
            "FrameworkVersion": "xx",
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
            "Name": "xx",
            "BillingInfo": "xx",
            "Region": "xx",
            "ResourceGroupName": "xx",
            "LogEnable": true,
            "EndTime": "xx",
            "Output": {
                "Paths": [
                    "xx"
                ],
                "Region": "xx",
                "Bucket": "xx"
            },
            "ImageInfo": {
                "ImageUrl": "xx",
                "RegistryRegion": "xx",
                "RegistryId": "xx",
                "ImageType": "xx"
            },
            "Uin": "xx",
            "RuntimeInSeconds": 1,
            "DataSource": "xx",
            "ChargeType": "xx",
            "CreateTime": "xx",
            "StartCmdInfo": {
                "PsStartCmd": "xx",
                "StartCmd": "xx",
                "WorkerStartCmd": "xx"
            },
            "LogConfig": {
                "TopicId": "xx",
                "LogsetId": "xx"
            }
        },
        "RequestId": "xx"
    }
}
```

