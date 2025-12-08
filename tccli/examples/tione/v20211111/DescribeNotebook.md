**Example 1: Notebook详情**



Input: 

```
tccli tione DescribeNotebook --cli-unfold-argument  \
    --Id nb-1188508294472113920
```

Output: 
```
{
    "Response": {
        "RequestId": "ecc8d2f6-9772-40df-856f-f6e48c6a7008",
        "NotebookDetail": {
            "ChargeType": "POSTPAID_BY_HOUR",
            "AutomaticStopTime": 0,
            "EndTime": "2024-11-14T17:22:16+08",
            "ChargeStatus": "BILLING",
            "Status": "Stopped",
            "UpdateTime": "2024-11-14T17:17:51+08",
            "DataSource": "CFS",
            "Message": "",
            "VolumeSourceCFS": {
                "Id": "cfs-9su5kqtv",
                "Path": "/tione",
                "Protocol": "NFS",
                "MountType": "STORAGE"
            },
            "VolumeSourceType": "CFS",
            "ImageInfo": {
                "ImageType": "SYSTEM",
                "ImageUrl": "tione.tencentcloudcr.com/qcloud-ti-platform/llm-train:24.03-gpu-py310-cu124-tilearn-llm-v1.8.0",
                "ImageName": "tilearn-llm0.9-torch2.3-py3.10-cuda12.4-gpu",
                "RegistryId": "",
                "RegistryRegion": ""
            },
            "ImageType": "SYSTEM",
            "DataConfigs": [
                {
                    "MappingPath": "/home/tione/notebook",
                    "DataSourceType": "CFS",
                    "DataSourceUsage": "",
                    "HDFSSource": {
                        "Id": "hd-sds",
                        "Path": "/date"
                    },
                    "CFSTurboSource": {
                        "Id": "cfs-14csdso5",
                        "Path": "/tione"
                    },
                    "CFSSource": {
                        "Id": "cfs-14cpoxo5",
                        "Protocol": "NFS",
                        "MountType": "STORAGE",
                        "Path": "/tione"
                    },
                    "COSSource": {
                        "Bucket": "harry-1318247806",
                        "Region": "ap-shanghai",
                        "Paths": [
                            "/test"
                        ]
                    },
                    "GooseFSSource": {
                        "Id": "",
                        "Type": "",
                        "Path": "",
                        "NameSpace": ""
                    },
                    "LocalDiskSource": {
                        "InstanceId": ""
                    },
                    "CBSSource": {
                        "VolumeSizeInGB": 0
                    },
                    "DataSetSource": {
                        "Id": ""
                    }
                }
            ],
            "VpcId": "vpc-hb7u9q6e",
            "Tags": [
                {
                    "TagKey": "test-key",
                    "TagValue": "test-value"
                }
            ],
            "Id": "nb-1188508294472113920",
            "ResourceGroupId": "trsg-dwpqnjmk",
            "SubnetId": "subnet-58zkmdob",
            "LifecycleScriptId": "ls-1007228485705742720",
            "RootAccess": true,
            "Name": "notebook-test",
            "DefaultCodeRepoId": "cr-1000669213287070080",
            "ResourceConf": {
                "Gpu": 1,
                "Cpu": 2018,
                "GpuType": "V100",
                "InstanceType": "TI.S.MEDIUM.POST",
                "Memory": 4000
            },
            "AutoStopping": true,
            "ResourceGroupName": "resource-test",
            "LogEnable": true,
            "BillingInfos": [
                "info"
            ],
            "InstanceTypeAlias": "2C4G",
            "AdditionalCodeRepoIds": [
                "cr-1000669213287070080"
            ],
            "DirectInternetAccess": true,
            "CreateTime": "2024-11-11T10:50:44+08",
            "JobCreateTime": "2024-11-14T16:58:00+08",
            "RuntimeInSeconds": 100,
            "VolumeSizeInGB": 100,
            "StartTime": "2024-11-14T19:50:10+08",
            "PodName": "nb-1188501796310898048-912gqy8i0xvk",
            "FailureReason": "no-msg",
            "SubUin": "100032979603",
            "LogConfig": {
                "TopicId": "ea8048db-8f97-4abb-9668-f3532b9b61f8",
                "LogsetId": "4dd0a097-f629-4afc-9b99-888ef99a178f"
            }
        }
    }
}
```

