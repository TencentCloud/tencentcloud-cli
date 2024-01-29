**Example 1: 查询批量预测任务**

查询单个批量预测任务详情

Input: 

```
tccli tione DescribeBatchTask --cli-unfold-argument  \
    --BatchTaskId batch-78ugzrxxxxx
```

Output: 
```
{
    "Response": {
        "BatchTaskDetail": {
            "BatchTaskId": "batch-78ugzrxxxxx",
            "BatchTaskName": "示例任务",
            "Uin": "100011111111",
            "SubUin": "100011111111",
            "Region": "ap-shanghai",
            "ChargeType": "PREPAID",
            "ResourceGroupId": "ersg-l5pg11111",
            "ResourceGroupName": "示例资源组",
            "ResourceConfigInfo": {
                "Role": "WORKER",
                "Cpu": 4000,
                "Memory": 8192,
                "GpuType": "T4",
                "Gpu": 0,
                "InstanceType": "",
                "InstanceTypeAlias": "",
                "InstanceNum": 1,
                "RDMAConfig": {
                    "Enable": true
                }
            },
            "Tags": [],
            "ModelInfo": {
                "ModelId": "m-76225796131111111111",
                "ModelName": "classify-cpu",
                "ModelVersionId": "mv-v1-76225796131111111111",
                "ModelVersion": "v1",
                "ModelSource": "COS",
                "ModelType": "NORMAL",
                "CosPathInfo": {
                    "Bucket": "example-sh-125651111",
                    "Region": "ap-shanghai",
                    "Paths": [
                        "classify/classify/"
                    ]
                },
                "AlgorithmFramework": "PYTORCH"
            },
            "ImageInfo": {
                "ImageType": "PRESET",
                "ImageUrl": "tione.tencentcloudcr.com/qcloud-ti-platform/ti-cloud-infer-pytorch-cpu:example-v1",
                "RegistryRegion": "",
                "RegistryId": ""
            },
            "CodePackagePath": {
                "Bucket": "",
                "Region": "",
                "Paths": []
            },
            "StartCmd": "",
            "DataConfigs": [
                {
                    "MappingPath": "",
                    "DataSourceType": "COS",
                    "DataSetSource": null,
                    "COSSource": {
                        "Bucket": "example-test-sh-125658111111",
                        "Region": "ap-shanghai",
                        "Paths": [
                            "data/test/"
                        ]
                    },
                    "CFSSource": null,
                    "HDFSSource": null,
                    "CFSTurboSource": null,
                    "GooseFSSource": null
                }
            ],
            "Outputs": [
                {
                    "MappingPath": "",
                    "DataSourceType": "COS",
                    "DataSetSource": null,
                    "COSSource": {
                        "Bucket": "example-test-sh-125658111111",
                        "Region": "ap-shanghai",
                        "Paths": [
                            "output/"
                        ]
                    },
                    "CFSSource": null,
                    "HDFSSource": null,
                    "GooseFSSource": null,
                    "CFSTurboSource": null
                }
            ],
            "LogEnable": false,
            "LogConfig": {
                "LogsetId": "",
                "TopicId": ""
            },
            "VpcId": "",
            "SubnetId": "",
            "Status": "SUCCEED",
            "RuntimeInSeconds": 89,
            "CreateTime": "2023-12-26 20:15:41",
            "UpdateTime": "2023-12-26 20:17:38",
            "StartTime": "2023-12-26 20:16:07",
            "EndTime": "2023-12-26 20:17:36",
            "ChargeStatus": "NOT_BILLING",
            "LatestInstanceId": "batch-78ugzrxxxxx-78ufl1m111w",
            "Remark": "",
            "FailureReason": "job succeed",
            "BillingInfo": "",
            "PodList": [],
            "ModelInferenceCodeInfo": {
                "Bucket": "example-test-sh-125658111111",
                "Region": "ap-shanghai",
                "Paths": [
                    "classify/classify/batch/model_service.py"
                ]
            }
        },
        "RequestId": "2ec5cd1e-311b-1111-9119-3da111160111"
    }
}
```

