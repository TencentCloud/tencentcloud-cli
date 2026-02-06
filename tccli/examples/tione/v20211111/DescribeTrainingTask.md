**Example 1: 训练任务详情**



Input: 

```
tccli tione DescribeTrainingTask --cli-unfold-argument  \
    --Id train-1329791605108055040
```

Output: 
```
{
    "Response": {
        "TrainingTaskDetail": {
            "Id": "train-1329791605108055040",
            "Name": "initCommand_test",
            "Uin": "100031385875",
            "SubUin": "100042146752",
            "Region": "ap-guangzhou",
            "FrameworkName": "PYTORCH",
            "FrameworkVersion": "",
            "FrameworkEnvironment": "torch1.9-py3.8-cuda11.1-gpu",
            "TrainingMode": "DDP",
            "ChargeType": "POSTPAID_BY_HOUR",
            "ResourceGroupId": "",
            "ResourceGroupName": "",
            "ResourceConfigInfos": [
                {
                    "Role": "WORKER",
                    "Cpu": 2000,
                    "Memory": 2048,
                    "GpuType": "",
                    "Gpu": 0,
                    "InstanceType": "TI.S6.MEDIUM2.POST",
                    "InstanceTypeAlias": "2C2G",
                    "InstanceNum": 1,
                    "RDMAConfig": {
                        "Enable": false
                    }
                }
            ],
            "Tags": [
                {
                    "TagKey": "qcs:tag:createdBy",
                    "TagValue": "CAMUser:100042146752:evanxli"
                }
            ],
            "ImageInfo": {
                "ImageType": "PRE_SET",
                "ImageUrl": "tione.tencentcloudcr.com/qcloud-ti-platform/ti-cloud-torch-1.9.0-devel:1.0.9",
                "RegistryRegion": "",
                "RegistryId": "",
                "ImageName": "torch1.9-py3.8-cuda11.1-gpu"
            },
            "CodePackagePath": {
                "Bucket": "",
                "Region": "",
                "Paths": []
            },
            "StartCmdInfo": {
                "StartCmd": "",
                "PsStartCmd": "",
                "WorkerStartCmd": "sleep 3600"
            },
            "DataSource": "",
            "DataConfigs": [],
            "TuningParameters": "{abc,}",
            "Output": {
                "Bucket": "",
                "Region": "",
                "Paths": []
            },
            "LogEnable": false,
            "LogConfig": {
                "LogsetId": "",
                "TopicId": ""
            },
            "VpcId": "",
            "SubnetId": "",
            "Status": "SUCCEED",
            "RuntimeInSeconds": 3602,
            "CreateTime": "2025-05-28T18:18:33+08",
            "UpdateTime": "2025-05-29T14:41:57+08",
            "StartTime": "2025-05-29T14:43:53+08",
            "EndTime": "2025-05-29T15:43:55+08",
            "ChargeStatus": "NOT_BILLING",
            "LatestInstanceId": "train-1329791605108055040-a3vq1whfx24g",
            "TensorBoardId": "",
            "Remark": "",
            "FailureReason": "",
            "BillingInfo": "",
            "Message": "",
            "CallbackUrl": "",
            "SubUinName": "evanxli",
            "CodeRepos": [
                {
                    "Id": "cr-1076157270725717248",
                    "TargetPath": "/git/data"
                }
            ]
        },
        "RequestId": "aaa06bff-0a06-4539-9a86-36b2f605d525"
    }
}
```

