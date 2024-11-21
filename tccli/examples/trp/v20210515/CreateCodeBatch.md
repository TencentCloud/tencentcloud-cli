**Example 1: 新增批次**

新增批次

Input: 

```
tccli trp CreateCodeBatch --cli-unfold-argument  \
    --MerchantId eqdmnz7020bmtvi9 \
    --ProductId tz6jpscwky41u23o9b \
    --BatchType 1 \
    --BatchId  \
    --Remark 备注 \
    --MpTpl 模板ID \
    --CloneId 复制的批次ID \
    --BatchCode 20121212000001 \
    --ValidDate 2022-11-12 \
    --ProductionDate 2022-05-12
```

Output: 
```
{
    "Response": {
        "BatchId": "20121212000001xxx",
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

