**Example 1: 子域名解析量统计**

 子域名解析量统计

Input: 

```
tccli dnspod DescribeSubdomainAnalytics --cli-unfold-argument  \
    --Domain example.com \
    --StartDate 2022-06-14 \
    --EndDate 2022-06-14 \
    --Subdomain test
```

Output: 
```
{
    "Response": {
        "AliasData": [],
        "Data": [
            {
                "DateKey": "20221201",
                "HourKey": null,
                "Num": 0
            }
        ],
        "Info": {
            "DnsFormat": "DATE",
            "DnsTotal": 0,
            "Domain": "zhaodapian.com",
            "EndDate": "2022-12-01",
            "StartDate": "2022-12-01",
            "Subdomain": "test"
        },
        "RequestId": "b4aca3e1-c134-4a31-bc07-408d78551449"
    }
}
```

