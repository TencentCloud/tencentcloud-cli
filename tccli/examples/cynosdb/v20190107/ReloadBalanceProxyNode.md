**Example 1: 负载均衡数据库代理**

负载均衡数据库代理

Input: 

```
tccli cynosdb ReloadBalanceProxyNode --cli-unfold-argument  \
    --ClusterId cynosdbmysql-1234qwer \
    --ProxyGroupId cynosdbmysql-proxy-a13fcqwe
```

Output: 
```
{
    "Response": {
        "RequestId": "128046",
        "FlowId": 123,
        "TaskId": 123
    }
}
```

