**Example 1: 训练任务详情**



Input: 

```
tccli tione DescribeTrainingTask --cli-unfold-argument  \
    --Id abc
```

Output: 
```
{
    "Response": {
        "TrainingTaskDetail": {
            "Id": "abc",
            "Name": "abc",
            "Uin": "abc",
            "SubUin": "abc",
            "Region": "abc",
            "FrameworkName": "abc",
            "FrameworkVersion": "abc",
            "FrameworkEnvironment": "abc",
            "ChargeType": "abc",
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
            "Tags": [
                {
                    "TagKey": "abc",
                    "TagValue": "abc"
                }
            ],
            "TrainingMode": "abc",
            "CodePackagePath": {
                "Bucket": "abc",
                "Region": "abc",
                "Paths": [
                    "abc"
                ]
            },
            "StartCmdInfo": {
                "StartCmd": "abc",
                "PsStartCmd": "abc",
                "WorkerStartCmd": "abc"
            },
            "DataSource": "abc",
            "DataConfigs": [
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
                        "Path": "abc",
                        "MountType": "abc",
                        "Protocol": "abc"
                    },
                    "HDFSSource": {
                        "Id": "abc",
                        "Path": "abc"
                    },
                    "GooseFSSource": {
                        "Id": "abc"
                    },
                    "CFSTurboSource": {
                        "Id": "abc",
                        "Path": "abc"
                    }
                }
            ],
            "TuningParameters": "abc",
            "Output": {
                "Bucket": "abc",
                "Region": "abc",
                "Paths": [
                    "abc"
                ]
            },
            "LogEnable": true,
            "LogConfig": {
                "LogsetId": "abc",
                "TopicId": "abc"
            },
            "VpcId": "abc",
            "SubnetId": "abc",
            "ImageInfo": {
                "ImageType": "abc",
                "ImageUrl": "abc",
                "RegistryRegion": "abc",
                "RegistryId": "abc",
                "AllowSaveAllContent": true,
                "ImageName": "abc"
            },
            "RuntimeInSeconds": 1,
            "CreateTime": "abc",
            "StartTime": "abc",
            "ChargeStatus": "abc",
            "LatestInstanceId": "abc",
            "TensorBoardId": "abc",
            "Remark": "abc",
            "FailureReason": "abc",
            "UpdateTime": "abc",
            "EndTime": "abc",
            "BillingInfo": "abc",
            "ResourceGroupName": "abc",
            "Message": "abc",
            "Status": "abc",
            "CallbackUrl": "abc"
        },
        "RequestId": "abc"
    }
}
```

