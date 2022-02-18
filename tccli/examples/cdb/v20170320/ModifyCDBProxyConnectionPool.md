**Example 1: 配置数据库代理连接池**



Input: 

```
tccli cdb ModifyCDBProxyConnectionPool --cli-unfold-argument  \
    --OpenConnectionPool True \
    --ConnectionPoolType SessionConnectionPool \
    --PoolConnectionTimeOut 10 \
    --ProxyGroupId proxy-test
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "8155d27a-079a2580-19593e48-f1af5042",
        "RequestId": "3689c0eb-a92d-77ce-0ee2-17d99f604e64"
    }
}
```

