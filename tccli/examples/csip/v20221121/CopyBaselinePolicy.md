**Example 1: 复制自定义策略**

复制自定义策略

Input: 

```
tccli csip CopyBaselinePolicy --cli-unfold-argument  \
    --PolicyID 2 \
    --TargetAppIDList 200000000 \
    --MemberId mem-tencent-6*************29
```

Output: 
```
{
    "Response": {
        "RequestId": "beba8ffe-1028-4f9f-a345-b4653de3af30"
    }
}
```

