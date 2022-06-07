**Example 1: 新增批次**

新增批次

Input: 

```
tccli trp CreateCodeBatch --cli-unfold-argument  \
    --BatchId xx \
    --BatchType 1 \
    --MerchantId xx \
    --ProductId xx
```

Output: 
```
{
    "Response": {
        "BatchId": "xx",
        "RequestId": "xx"
    }
}
```

