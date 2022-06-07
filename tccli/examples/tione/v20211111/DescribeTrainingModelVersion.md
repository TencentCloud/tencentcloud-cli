**Example 1: 查询模型版本请求**



Input: 

```
tccli tione DescribeTrainingModelVersion --cli-unfold-argument  \
    --TrainingModelVersionId xx
```

Output: 
```
{
    "Response": {
        "TrainingModelVersion": {
            "TrainingModelCreateTime": "xx",
            "TrainingModelFormat": "xx",
            "TrainingJobId": "xx",
            "TrainingModelVersionId": "xx",
            "TrainingJobName": "xx",
            "TrainingModelIndex": "xx",
            "CreateTime": "xx",
            "ReasoningEnvironment": "xx",
            "TrainingModelStatus": "xx",
            "AlgorithmFramework": "xx",
            "TrainingModelName": "xx",
            "TrainingModelErrorMsg": "xx",
            "TrainingModelVersion": "xx",
            "TrainingModelProgress": 1,
            "TrainingModelSource": "xx",
            "ReasoningImageInfo": {
                "ImageUrl": "xx",
                "RegistryRegion": "xx",
                "RegistryId": "xx",
                "ImageType": "xx"
            },
            "ReasoningEnvironmentSource": "xx",
            "TrainingModelCosPath": {
                "Paths": [
                    "xx"
                ],
                "Region": "xx",
                "Bucket": "xx"
            },
            "TrainingModelId": "xx",
            "TrainingModelCreator": "xx"
        },
        "RequestId": "xx"
    }
}
```

