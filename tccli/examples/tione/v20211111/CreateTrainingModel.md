**Example 1: 创建模型**



Input: 

```
tccli tione CreateTrainingModel --cli-unfold-argument  \
    --ImportMethod MODEL \
    --TrainingModelName test-0203-05 \
    --TrainingModelVersion v1 \
    --ModelFormat PYTORCH \
    --AlgorithmFramework PYTORCH \
    --TrainingModelSource CFS \
    --ReasoningEnvironmentSource SYSTEM \
    --ReasoningImageInfo.ImageType PRE_SET \
    --ReasoningImageInfo.ImageUrl tione.tencentcloudcr.com/qcloud-ti-platform/llm-infer:vllm-0.9.1-ti-20250703 \
    --ReasoningImageInfo.RegistryRegion  \
    --ReasoningImageInfo.RegistryId  \
    --ReasoningEnvironment tione.tencentcloudcr.com/qcloud-ti-platform/llm-infer:vllm-0.9.1-ti-20250703 \
    --ReasoningEnvironmentId vllm(0.9.1) \
    --AutoClean false \
    --ModelCleanPeriod 1 \
    --MaxReservedModels 24
```

Output: 
```
{
    "Response": {
        "Id": "m-1511805105118762624",
        "TrainingModelVersionId": "mv-v1-1511805105118762625",
        "RequestId": "2569dfaf-131f-45f9-a5b5-dbf4d0db8d35"
    }
}
```

