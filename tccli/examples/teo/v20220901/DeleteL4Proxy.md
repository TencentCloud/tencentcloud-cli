**Example 1: 删除四层代理实例**

删除 ZoneId 为 zone-24wjy25v1cwi 下，ProxyId 为 sid-2qwk27xf7j9g 的四层代理实例。

Input: 

```
tccli teo DeleteL4Proxy --cli-unfold-argument  \
    --ZoneId zone-24wjy25v1cwi \
    --ProxyId sid-2qwk27xf7j9g
```

Output: 
```
{
    "Response": {
        "RequestId": "6f8h5258-cdda-4f82-b7sc-0aef4a219244"
    }
}
```

