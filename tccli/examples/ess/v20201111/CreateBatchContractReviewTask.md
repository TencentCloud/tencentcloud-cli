**Example 1: 批量创建合同审查任务**



Input: 

```
tccli ess CreateBatchContractReviewTask --cli-unfold-argument  \
    --Operator.UserId yDwJGUU6xxxhztsrrmBe \
    --ResourceIds yDtG1UU2xexxxC1pfrsbRhIOj \
    --PolicyType 0 \
    --Role.Name 授权方 \
    --Role.Description 广州贸易测试有限公司 \
    --ChecklistId yDtCMUUckpxxx0j0a6Ii
```

Output: 
```
{
    "Response": {
        "RequestId": "s1753417470034482869",
        "TaskIds": [
            "yDtIFUU2tnsxxx9d8"
        ]
    }
}
```

