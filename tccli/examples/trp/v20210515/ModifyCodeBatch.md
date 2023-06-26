**Example 1: 修改批次状态**

激活批次

Input: 

```
tccli trp ModifyCodeBatch --cli-unfold-argument  \
    --BatchId abc \
    --Status 1
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

