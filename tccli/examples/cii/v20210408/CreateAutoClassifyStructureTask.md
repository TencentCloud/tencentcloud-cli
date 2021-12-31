**Example 1: 创建未分类结构化任务接口示例**



Input: 

```
tccli cii CreateAutoClassifyStructureTask --cli-unfold-argument  \
    --ServiceType Underwrite \
    --PolicyId 0406-01 \
    --TriggerType Auto \
    --InsuranceTypes CriticalDiseaseInsurance LifeInsurance AccidentInsurance \
    --TaskInfos.0.CustomerId 0406-01-1 \
    --TaskInfos.0.CustomerName 0406-01-1 \
    --TaskInfos.0.FileList original_upload_dir/test.pdf
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

