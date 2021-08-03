**Example 1: 创建结构化任务接口示例**



Input: 

```
tccli cii CreateStructureTaskTest --cli-unfold-argument  \
    --ServiceType Underwrite \
    --PolicyId 0406-01 \
    --TriggerType Auto \
    --InsuranceTypes CriticalDiseaseInsurance LifeInsurance AccidentInsurance \
    --TaskInfos.0.TaskType HealthReport \
    --TaskInfos.0.CustomerId 0406-01-1 \
    --TaskInfos.0.CustomerName 0406-01-1 \
    --TaskInfos.0.FileList original_upload_dir/test.pdf \
    --TaskInfos.0.Year 2021
```

Output: 
```
{
    "Response": {
        "RequestId": "22dfcc05-1ba1-49b4-a751-f5611cdb3420",
        "MainTaskId": "37835597617481728"
    }
}
```

