**Example 1: CheckIntegrationTaskNameExists**

判断集成任务名称是否存在

Input: 

```
tccli wedata CheckIntegrationTaskNameExists --cli-unfold-argument  \
    --ProjectId 11022568003970304 \
    --TaskName 整库迁移 \
    --TaskId 20220506145218687
```

Output: 
```
{
    "Response": {
        "Data": true,
        "ExistsType": 1,
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

