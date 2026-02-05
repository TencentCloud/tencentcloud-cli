**Example 1: 查询预热限速限制**

查询加速域名 cn2.test-***a.online 的预热回源限速限制。

Input: 

```
tccli teo DescribePrefetchOriginLimit --cli-unfold-argument  \
    --ZoneId zone-3***j8tqd \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name domain-name \
    --Filters.0.Values cn2.test-***a.online
```

Output: 
```
{
    "Response": {
        "Limits": [
            {
                "Area": "Overseas",
                "Bandwidth": 100,
                "CreateTime": "2025-12-16T07:08:40Z",
                "DomainName": "cn2.test-***a.online",
                "UpdateTime": "2025-12-16T07:08:40Z",
                "ZoneId": "zone-3***j8tqd"
            }
        ],
        "TotalCount": 1,
        "RequestId": "7db71bfe-e735-4d1a-8f2d-90c085b7418d"
    }
}
```

