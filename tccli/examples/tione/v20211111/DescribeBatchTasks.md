**Example 1: 批量预测任务列表**

批量预测任务列表信息

Input: 

```
tccli tione DescribeBatchTasks --cli-unfold-argument  \
    --Filters.0.Name BatchTaskName \
    --Filters.0.Values abc \
    --Filters.0.Negative True \
    --Filters.0.Fuzzy True \
    --TagFilters.0.TagKey abc \
    --TagFilters.0.TagValues abc \
    --Offset 0 \
    --Limit 1 \
    --Order ASC \
    --OrderField CreateTime
```

Output: 
```
{
    "Response": {
        "BatchTaskSet": [
            {
                "BatchTaskId": "batch-78ugzrxxxxx",
                "BatchTaskName": "示例任务",
                "ModelInfo": {
                    "ModelId": "m-882512801111",
                    "ModelName": "classify-cpu",
                    "ModelVersionId": "mv-v1-8825128049111111",
                    "ModelVersion": "v1",
                    "ModelSource": "COS",
                    "ModelType": "NORMAL",
                    "CosPathInfo": {
                        "Bucket": "example-gz-12111111111",
                        "Region": "ap-guangzhou",
                        "Paths": [
                            "classify/"
                        ]
                    },
                    "AlgorithmFramework": "PYTORCH"
                },
                "ImageInfo": {
                    "ImageType": "PRESET",
                    "ImageUrl": "tione.tencentcloudcr.com/qcloud-ti-platform/ti-cloud-infer-pytorch:example",
                    "RegistryRegion": "",
                    "RegistryId": ""
                },
                "ChargeType": "POSTPAID_BY_HOUR",
                "ChargeStatus": "NOT_BILLING",
                "ResourceGroupId": "",
                "ResourceGroupName": "",
                "ResourceConfigInfo": {
                    "Role": "WORKER",
                    "Cpu": 2000,
                    "Memory": 4096,
                    "GpuType": "",
                    "Gpu": 0,
                    "InstanceType": "TI.S.MEDIUM.POST",
                    "InstanceTypeAlias": "2C4G",
                    "InstanceNum": 1,
                    "RDMAConfig": {
                        "Enable": true
                    }
                },
                "Tags": [],
                "Status": "SUCCEED",
                "RuntimeInSeconds": 112,
                "CreateTime": "2023-12-26 20:23:36",
                "UpdateTime": "2023-12-26 20:23:36",
                "StartTime": "2023-12-26 20:24:20",
                "EndTime": "2023-12-26 20:26:12",
                "Outputs": [],
                "FailureReason": "job succeed",
                "BillingInfo": ""
            }
        ],
        "TotalCount": 69,
        "RequestId": "0ec7a782-111-111-a063-11111111111"
    }
}
```

