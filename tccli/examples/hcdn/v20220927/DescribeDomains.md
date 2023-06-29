**Example 1: 查询域名列表**



Input: 

```
tccli hcdn DescribeDomains --cli-unfold-argument  \
    --Filters.0.Name Status \
    --Filters.0.Values 3 \
    --Filters.1.Name Domain \
    --Filters.1.Values www.qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "edd43e1f-e192-4541-a07d-e4c0da17d9c6",
        "TotalCount": 4,
        "DomainSet": [
            {
                "Domain": "www.qq.com",
                "Status": 3,
                "CreateTime": "2022-10-09 10:53:45"
            }
        ]
    }
}
```

