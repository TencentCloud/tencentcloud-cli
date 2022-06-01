**Example 1: 修改应用代理的状态**



Input: 

```
tccli teo ModifyApplicationProxyStatus --cli-unfold-argument  \
    --ZoneId zone-id123 \
    --ProxyId proxy-id123 \
    --Status online
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ProxyId": "proxy-xxx"
    }
}
```

