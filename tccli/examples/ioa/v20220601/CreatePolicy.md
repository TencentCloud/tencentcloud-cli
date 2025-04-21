**Example 1: 创建策略**

创建策略

Input: 

```
tccli ioa CreatePolicy --cli-unfold-argument  \
    --Name 测试 \
    --Description 测试 \
    --Status 1 \
    --PolicyType 1 \
    --PolicySubType 1 \
    --OsType 2 \
    --Priority 50
```

Output: 
```
{
    "Response": {
        "Data": {
            "PolicyId": 303884
        },
        "RequestId": "dc58f2fa-8534-4cb5-9b8d-233d52f1ab31"
    }
}
```

