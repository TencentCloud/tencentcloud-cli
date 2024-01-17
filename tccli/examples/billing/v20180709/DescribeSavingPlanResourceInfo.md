**Example 1: 输出示例**

查询名下可共享的sp资源详细

Input: 

```
tccli billing DescribeSavingPlanResourceInfo --cli-unfold-argument  \
    --Limit 0 \
    --Offset 1 \
    --CreateStartDate 2023-06-01 \
    --CreateEndDate 2023-09-30
```

Output: 
```
{
    "Response": {
        "RequestId": "37963bb4-f4ac-4c20-8c83-97d751f1aa91",
        "Total": 3
    }
}
```

