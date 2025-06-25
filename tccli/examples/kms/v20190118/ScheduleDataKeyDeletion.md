**Example 1: 计划删除数据密钥示例**

计划删除数据密钥

Input: 

```
tccli kms ScheduleDataKeyDeletion --cli-unfold-argument  \
    --DataKeyId 2a87094f-4c0e-11f0-8c25-52540073b995 \
    --PendingWindowInDays 7
```

Output: 
```
{
    "Response": {
        "DataKeyId": "2a87094f-4c0e-11f0-8c25-52540073b995",
        "DeletionDate": 1751276581,
        "RequestId": "f610236f-580d-49d3-a766-71163d9108eb"
    }
}
```

