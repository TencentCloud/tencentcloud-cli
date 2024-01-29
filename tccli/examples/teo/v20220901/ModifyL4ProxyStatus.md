**Example 1: 启用四层代理实例**

将 ZoneId 为 zone-24wjy25v1cwi 下 ProxyId 为 sid-2qwk27xf7j9g 的四层代理实例启用。

Input: 

```
tccli teo ModifyL4ProxyStatus --cli-unfold-argument  \
    --ZoneId zone-24wjy25v1cwi \
    --ProxyId sid-2qwk27xf7j9g \
    --Status online
```

Output: 
```
{
    "Response": {
        "RequestId": "6f8h5258-cdda-4f82-b7sc-0aef4a219244"
    }
}
```

