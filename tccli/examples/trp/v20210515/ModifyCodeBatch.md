**Example 1: 修改批次状态**

激活批次

Input: 

```
tccli trp ModifyCodeBatch --cli-unfold-argument  \
    --BatchId 20121212000001 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "BatchId": "20121212000001",
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

