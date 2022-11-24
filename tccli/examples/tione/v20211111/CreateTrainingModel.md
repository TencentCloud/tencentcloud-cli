**Example 1: 导入模型请求**



Input: 

```
tccli tione CreateTrainingModel --cli-unfold-argument  \
    --TrainingJobName test-job \
    --TrainingJobId train-608753141184489472 \
    --TrainingModelVersion v1 \
    --Tags.0.TagKey test-key \
    --Tags.0.TagValue test-value \
    --ModelMoveMode COPY \
    --TrainingModelIndex test123 \
    --ReasoningEnvironment tione.tencentcloudcr.com/qcloud-ti-platform/ti-cloud-infer-pytorch-gpu:py38-torch1.9.0-cu111-tiacc3.0.0-2.0.2 \
    --ReasoningEnvironmentId pytorch1.9.0-py38(gpu) \
    --TrainingModelName test-model \
    --AlgorithmFramework PYTORCH \
    --ImportMethod MODEL \
    --ReasoningEnvironmentSource SYSTEM \
    --TrainingModelCosPath.Paths test/output/train-608753141184489472/model/ \
    --TrainingModelCosPath.Region ap-guangzhou \
    --TrainingModelCosPath.Bucket test-bucket
```

Output: 
```
{
    "Response": {
        "Id": "m-664968589676184576",
        "RequestId": "ced11c16-fd5a-4f12-8a0b-17c7f0b14659",
        "TrainingModelVersionId": "mv-v1-664975193381340160"
    }
}
```

