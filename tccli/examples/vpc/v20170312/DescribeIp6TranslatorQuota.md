**Example 1: 查询IPV6转换实例配额**

查询IPV6转换实例配额

Input: 

```
tccli vpc DescribeIp6TranslatorQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "QuotaSet": [
            {
                "QuotaId": "TOTAL_TRANSLATOR_QUOTA",
                "QuotaCurrent": 1,
                "QuotaLimit": 10
            },
            {
                "QuotaId": "ip6-8w9ts0j2",
                "QuotaCurrent": 2,
                "QuotaLimit": 50
            }
        ],
        "RequestId": "72ee23d3-e4ea-48d1-ae5b-dca1ab7dd68c"
    }
}
```

