**Example 1: 模型版本列表请求**



Input: 

```
tccli tione DescribeTrainingModelVersions --cli-unfold-argument  \
    --TrainingModelId m-608587242317024640
```

Output: 
```
{
    "Response": {
        "TrainingModelVersions": [
            {
                "ReasoningEnvironment": "tione.tencentcloudcr.com/qcloud-ti-platform/ti-cloud-infer-pytorch-gpu:py38-torch1.9.0-cu111-tiacc2.5.0-2.0.2",
                "TrainingModelCosPath": {
                    "Paths": [
                        "test/model/"
                    ],
                    "Region": "ap-guangzhou",
                    "Bucket": "test-bucket"
                },
                "TrainingJobId": "",
                "TrainingModelProgress": 100,
                "TrainingModelStatus": "STATUS_SUCCESS",
                "AutoClean": "false",
                "MaxReservedModels": 0,
                "TrainingModelName": "test-model",
                "AlgorithmFramework": "PYTORCH",
                "ModelCleanPeriod": 0,
                "ModelHotUpdatePath": {
                    "Paths": [
                        "test/model/"
                    ],
                    "Region": "ap-guangzhou",
                    "Bucket": "test-bucket"
                },
                "TrainingModelErrorMsg": "",
                "TrainingModelCreator": "100020000",
                "TrainingModelCreateTime": "2022-09-06T08:34:13Z",
                "TrainingModelVersion": "v1",
                "TrainingModelSource": "COS",
                "ReasoningEnvironmentSource": "SYSTEM",
                "GPUType": "",
                "TrainingModelFormat": "TORCH_SCRIPT",
                "TrainingJobName": "",
                "TrainingModelVersionId": "mv-v1-625097625049989888",
                "TrainingModelIndex": "",
                "TrainingModelId": "m-608587242317024640",
                "VersionType": "NORMAL",
                "ReasoningImageInfo": {
                    "ImageUrl": "",
                    "RegistryRegion": "",
                    "RegistryId": "",
                    "ImageType": ""
                },
                "CreateTime": "2022-09-29T03:17:24Z"
            }
        ],
        "RequestId": "ced11c16-fd5a-4f12-8a0b-17c7f0b14659"
    }
}
```

