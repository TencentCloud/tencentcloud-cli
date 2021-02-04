**Example 1: 创建结构化任务接口示例**



Input: 

```
tccli cii CreateStructureTask --cli-unfold-argument  \
    --PolicyId 20201212001 \
    --CustomerId c001 \
    --CustomerName xx保险 \
    --TaskType HealthReport \
    --Year 2020 \
    --FileList original_upload_dir/report.pdf
```

Output: 
```
{
    "Response": {
        "RequestId": "22dfcc05-1ba1-49b4-a751-f5611cdb3420",
        "TaskId": "37835597617481728"
    }
}
```

