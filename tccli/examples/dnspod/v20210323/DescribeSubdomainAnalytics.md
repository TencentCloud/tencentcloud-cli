**Example 1: 子域名解析量统计**

 子域名解析量统计

Input: 

```
tccli dnspod DescribeSubdomainAnalytics --cli-unfold-argument  \
    --Domain dnspod.cn \
    --StartDate 2024-12-30 \
    --EndDate 2024-12-30 \
    --Subdomain www
```

Output: 
```
{
    "Response": {
        "AliasData": [],
        "Data": [
            {
                "DateKey": "20241230",
                "HourKey": null,
                "Num": 0
            }
        ],
        "Info": {
            "DnsFormat": "DATE",
            "DnsTotal": 0,
            "Domain": "dnspod.cn",
            "EndDate": "2024-12-30",
            "StartDate": "2024-12-30",
            "Subdomain": "www"
        },
        "RequestId": "9ce684ec-a986-4f48-8495-e68b1f337e61"
    }
}
```

