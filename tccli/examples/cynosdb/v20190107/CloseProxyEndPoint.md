**Example 1: 关闭数据库代理连接地址**



Input: 

```
tccli cynosdb CloseProxyEndPoint --cli-unfold-argument  \
    --ClusterId abc \
    --ProxyGroupId abc
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

