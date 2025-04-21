**Example 1: 修改策略内容**

修改策略内容

Input: 

```
tccli ioa ModifyPolicy --cli-unfold-argument  \
    --PolicyId 303884 \
    --Name 测试2 \
    --Description 修改名字 \
    --Status 1 \
    --Priority 50 \
    --OsType 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "PolicyId": 303884
        },
        "RequestId": "cb3552ae-b868-4069-a238-48426455e251"
    }
}
```

