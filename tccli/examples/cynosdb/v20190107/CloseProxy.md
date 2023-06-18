**Example 1: 关闭数据库代理**

关闭数据库代理

Input: 

```
tccli cynosdb CloseProxy --cli-unfold-argument  \
    --ClusterId abc \
    --ProxyGroupId abc \
    --OnlyCloseRW True
```

Output: 
```
{
    "Response": {
        "FlowId": 0,
        "TaskId": 0,
        "RequestId": "abc"
    }
}
```

