**Example 1: 删除所有路由**

删除域名及所有路由

Input: 

```
tccli tcb DeleteHTTPServiceRoute --cli-unfold-argument  \
    --EnvId *****************-7ezncwdd421446 \
    --Domain xxx.***************.cn
```

Output: 
```
{
    "Response": {
        "RequestId": "ac011e66-c9f3-4de9-8d76-df3316b3c5f8"
    }
}
```

