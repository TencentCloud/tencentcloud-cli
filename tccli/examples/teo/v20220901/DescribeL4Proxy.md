**Example 1: 查询站点下四层代理实例列表**

查询站点 ID 为 zone-24wjy25v1cwi 的站点下四层代理实例列表。

Input: 

```
tccli teo DescribeL4Proxy --cli-unfold-argument  \
    --Offset 1 \
    --Limit 10 \
    --ZoneId zone-24wjy25v1cwi
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "L4Proxies": [
            {
                "ZoneId": "zone-24wjy25v1cwi",
                "ProxyId": "sid-2qwk27xf7j9g",
                "ProxyName": "test",
                "Area": "mainland",
                "Cname": "test.24wjy25v1cwi.eo.dnse5.com",
                "Ips": [],
                "Status": "online",
                "Ipv6": "off",
                "StaticIp": "off",
                "AccelerateMainland": "off",
                "UpdateTime": "2023-09-22T15:31:04+00:00"
            }
        ],
        "RequestId": "6f8h5258-cdda-4f82-b7sc-0aef4a219244"
    }
}
```

