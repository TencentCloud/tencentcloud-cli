**Example 1: 修改地址配置**

修改地址配置

Input: 

```
tccli postgres ModifyDBProxyAddress --cli-unfold-argument  \
    --DBInstanceId postgres-l4mvde5d \
    --ProxyGroupId proxy-o0rx08tn \
    --AddressId proxyaddr-3fhqchao \
    --ConnectionPool True
```

Output: 
```
{
    "Response": {
        "RequestId": "c34ee392-54cf-4aa5-bcce-ed4991f9f4c2"
    }
}
```

