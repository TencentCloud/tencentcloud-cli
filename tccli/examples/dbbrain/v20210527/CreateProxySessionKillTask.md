**Example 1: 根据实例 id 创建终止所有代理节点会话连接的异步任务**



Input: 

```
tccli dbbrain CreateProxySessionKillTask --cli-unfold-argument  \
    --InstanceId cdb-8jawylhf \
    --Product redis
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": 123456,
        "RequestId": "xx"
    }
}
```

