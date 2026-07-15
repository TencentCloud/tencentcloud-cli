**Example 1: 获取模型路由实例日志**



Input: 

```
tccli clb DescribeModelRouterLogs --cli-unfold-argument  \
    --ModelRouterId cmr-pm53f9c3 \
    --KeyId vkey-cgjyw5xj \
    --Model gpt-4o \
    --Status failure \
    --NextToken eyJwYWdlIjogMiwgInBhZ2Vfc2l6ZSI6IDIwfQ== \
    --MaxResults 20
```

Output: 
```
{
    "Response": {
        "Logs": [],
        "NextToken": "",
        "TotalCount": 0,
        "RequestId": "110ce5a9-53aa-473a-af9b-8040404ae265"
    }
}
```

