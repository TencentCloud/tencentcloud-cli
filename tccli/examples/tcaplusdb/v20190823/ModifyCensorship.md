**Example 1: 更新审核状态**



Input: 

```
tccli tcaplusdb ModifyCensorship --cli-unfold-argument  \
    --Uins xx \
    --ClusterId xx \
    --Censorship 0
```

Output: 
```
{
    "Response": {
        "Uins": [
            "xx"
        ],
        "ClusterId": "xx",
        "RequestId": "xx",
        "Censorship": 0
    }
}
```

