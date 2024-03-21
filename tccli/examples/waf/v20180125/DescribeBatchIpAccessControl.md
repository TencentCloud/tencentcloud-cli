**Example 1: Waf 多域名ip黑白名单查询**



Input: 

```
tccli waf DescribeBatchIpAccessControl --cli-unfold-argument  \
    --Sort ts_version:-1 \
    --Limit 20 \
    --Filters.0.Values Domain \
    --Filters.0.Name www.q.com \
    --Filters.0.ExactMatch True \
    --OffSet 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Res": [
                {
                    "ActionType": 42,
                    "Ip": "1.1.1.1",
                    "Note": "",
                    "Source": "custom",
                    "TsVersion": 1579074751421,
                    "ValidTs": 1579017599,
                    "Hosts": [
                        "www.q.com",
                        "www.b.com"
                    ]
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "c937ce96-cf53-4df8-b288-07c6e092072d"
    }
}
```

