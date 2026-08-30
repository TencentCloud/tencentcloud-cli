**Example 1: 删除指定Proxy的连接地址**



Input: 

```
tccli postgres CloseDBProxyAddress --cli-unfold-argument  \
    --DBInstanceId postgres-2wvpv38j \
    --AddressId proxyaddr-0p3p1r76 \
    --ProxyGroupId proxy-89ap4mrx
```

Output: 
```
{
    "Response": {
        "TaskId": 100282,
        "RequestId": "c390a1f8-1907-47fd-b40f-d9eb5de8d0d1"
    }
}
```

