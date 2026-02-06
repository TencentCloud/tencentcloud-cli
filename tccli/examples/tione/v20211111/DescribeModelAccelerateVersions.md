**Example 1: 优化模型列表**



Input: 

```
tccli tione DescribeModelAccelerateVersions --cli-unfold-argument  \
    --Limit 10 \
    --Filters.0.Fuzzy False \
    --Filters.0.Values mv-v1-522962784402949761 \
    --Filters.0.Name TrainingModelVersionId \
    --Filters.0.Negative False \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ModelAccelerateVersions": [
            {
                "ModelId": "m-918096658947376768",
                "ModelVersionId": "mv-v9-918664407880828544",
                "ModelJobId": "train-999234853525975168",
                "ModelJobName": "zoeymodel",
                "ModelVersion": "v9",
                "SpeedUp": "4.83x",
                "ModelSource": {
                    "Source": "Job",
                    "JobName": "zoeymodel",
                    "JobVersion": "V1",
                    "JobId": "train-999234853525975168",
                    "ModelName": "zoeytest",
                    "AlgorithmFramework": "PYTORCH",
                    "TrainingPreference": "",
                    "ReasoningEnvironmentSource": "SYSTEM",
                    "ReasoningEnvironment": "tione.tencentcloudcr.com/qcloud-ti-platform/ti-cloud-infer-pytorch-gpu:py38-torch2.0.0-cu118-sd-tiacc4.2.9-3.2.17",
                    "ReasoningEnvironmentId": "stabe-diffusion-mosec-a10(gpu)",
                    "ReasoningImageInfo": {
                        "ImageType": "TCR",
                        "ImageUrl": "tione-live.tencentcloudcr.com/tione-demo/infer:angel-vllm-0.4.2-ti-1.1.2",
                        "RegistryRegion": "ap-shanghai",
                        "RegistryId": "tcr-f40c5gin",
                        "AllowSaveAllContent": true,
                        "ImageName": "infer"
                    }
                },
                "CosPathInfo": {
                    "Bucket": "qiqi-sh-1318247806",
                    "Region": "ap-shanghai",
                    "Paths": [
                        "lstest/"
                    ]
                },
                "CreateTime": "2024-02-27 14:32:11",
                "ModelFormat": "TORCH_SCRIPT",
                "Status": "STATUS_SUCCESS",
                "Progress": 1,
                "ErrorMsg": "",
                "GPUType": "T4",
                "ModelCosPath": {
                    "Bucket": "qiqi-sh-1318247806",
                    "Region": "ab-shanghai",
                    "Paths": [
                        "Output/"
                    ]
                }
            }
        ],
        "RequestId": "c72334f2-fb6f-4171-b8c6-8038cf8f1f9f"
    }
}
```

