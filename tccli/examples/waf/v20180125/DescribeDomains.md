**Example 1: 查询用户所有实例的详细信息**



Input: 

```
tccli waf DescribeDomains --cli-unfold-argument  \
    --Offset 1 \
    --Limit 20 \
    --Filters.0.Name Edition \
    --Filters.0.Values sparta_waf \
    --Filters.0.ExactMatch True \
    --Filters.1.Name InstanceId \
    --Filters.1.Values waf_000000002 \
    --Filters.1.ExactMatch True
```

Output: 
```
{
    "Response": {
        "RequestId": "b4f13899-561b-46a0-a045-6ba6b72c38f2",
        "Total": 8,
        "Domains": [
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {}
        ]
    }
}
```

