**Example 1: 新增批次**

新增批次

Input: 

```
tccli trp CreateCodeBatch --cli-unfold-argument  \
    --MerchantId abc \
    --ProductId abc \
    --BatchType 1 \
    --BatchId abc \
    --Remark abc \
    --MpTpl abc \
    --CloneId abc \
    --BatchCode abc \
    --ValidDate abc \
    --ProductionDate abc
```

Output: 
```
{
    "Response": {
        "BatchId": "abc",
        "RequestId": "abc"
    }
}
```

