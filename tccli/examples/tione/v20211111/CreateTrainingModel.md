**Example 1: 导入模型请求**



Input: 

```
tccli tione CreateTrainingModel --cli-unfold-argument  \
    --TrainingJobName xx \
    --TrainingJobId xx \
    --TrainingModelVersion xx \
    --Tags.0.TagKey xx \
    --Tags.0.TagValue xx \
    --ModelMoveMode xx \
    --TrainingModelIndex xx \
    --ReasoningEnvironment xx \
    --TrainingModelName xx \
    --AlgorithmFramework xx \
    --ImportMethod xx \
    --ReasoningImageInfo.ImageUrl xx \
    --ReasoningImageInfo.RegistryRegion xx \
    --ReasoningImageInfo.RegistryId xx \
    --ReasoningImageInfo.ImageType xx \
    --ReasoningEnvironmentSource xx \
    --TrainingModelCosPath.Paths xx \
    --TrainingModelCosPath.Region xx \
    --TrainingModelCosPath.Bucket xx
```

Output: 
```
{
    "Response": {
        "Id": "xx",
        "RequestId": "xx",
        "TrainingModelVersionId": "xx"
    }
}
```

