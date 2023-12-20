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
                "ModelId": "abc",
                "ModelVersionId": "abc",
                "ModelJobId": "abc",
                "ModelJobName": "abc",
                "ModelVersion": "abc",
                "SpeedUp": "abc",
                "ModelSource": {
                    "Source": "abc",
                    "JobName": "abc",
                    "JobVersion": "abc",
                    "JobId": "abc",
                    "ModelName": "abc",
                    "AlgorithmFramework": "abc",
                    "TrainingPreference": "abc",
                    "ReasoningEnvironmentSource": "abc",
                    "ReasoningEnvironment": "abc",
                    "ReasoningEnvironmentId": "abc",
                    "ReasoningImageInfo": {
                        "ImageType": "abc",
                        "ImageUrl": "abc",
                        "RegistryRegion": "abc",
                        "RegistryId": "abc",
                        "AllowSaveAllContent": true,
                        "ImageName": "abc"
                    }
                },
                "CosPathInfo": {
                    "Bucket": "abc",
                    "Region": "abc",
                    "Paths": [
                        "abc"
                    ]
                },
                "CreateTime": "abc",
                "ModelFormat": "abc",
                "Status": "abc",
                "Progress": 1,
                "ErrorMsg": "abc",
                "GPUType": "abc",
                "ModelCosPath": {
                    "Bucket": "abc",
                    "Region": "abc",
                    "Paths": [
                        "abc"
                    ]
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

