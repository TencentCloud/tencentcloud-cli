**Example 1: 配置数据库代理参数**



Input: 

```
tccli cdb ModifyCdbProxyParam --cli-unfold-argument  \
    --InstanceId cdb-xxxx \
    --ProxyGroupId proxy-xxx \
    --ConnectionPoolLimit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx"
    }
}
```

