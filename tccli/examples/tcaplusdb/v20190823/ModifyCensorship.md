**Example 1: 更新审核状态**



Input: 

```
tccli tcaplusdb ModifyCensorship --cli-unfold-argument  \
    --Uins 12323 \
    --ClusterId 123213 \
    --Censorship 0
```

Output: 
```
{
    "Response": {
        "Uins": [
            "123123"
        ],
        "ClusterId": "12313",
        "RequestId": "123123-12313",
        "Censorship": 0
    }
}
```

