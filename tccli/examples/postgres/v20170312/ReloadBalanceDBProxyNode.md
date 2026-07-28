**Example 1: 重新负载平衡数据库代理节点**

重新负载平衡数据库代理节点

Input: 

```
tccli postgres ReloadBalanceDBProxyNode --cli-unfold-argument  \
    --DBInstanceId postgres-ko7e7fs5 \
    --ProxyGroupId proxy-p0aio887 \
    --AddressId proxyaddr-nh6d1xue
```

Output: 
```
{
    "Response": {
        "RequestId": "572245a8-44f0-45d7-ac72-3f5dd7e656c6"
    }
}
```

