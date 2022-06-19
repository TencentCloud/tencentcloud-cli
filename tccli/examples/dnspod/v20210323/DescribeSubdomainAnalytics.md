**Example 1: 子域名解析量统计**



Input: 

```
tccli dnspod DescribeSubdomainAnalytics --cli-unfold-argument  \
    --Domain example.com \
    --StartDate 2022-06-14 \
    --EndDate 2022-06-14 \
    --Subdomain www
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "AliasData": [
            {
                "Data": [
                    {
                        "DateKey": "20220608",
                        "HourKey": null,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220609",
                        "HourKey": null,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220610",
                        "HourKey": null,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220611",
                        "HourKey": null,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220612",
                        "HourKey": null,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220613",
                        "HourKey": null,
                        "Num": 0
                    },
                    {
                        "DateKey": "20220614",
                        "HourKey": null,
                        "Num": 0
                    }
                ],
                "Info": {
                    "DnsFormat": "DATE",
                    "DnsTotal": 0,
                    "Domain": "examplealis.com",
                    "EndDate": "2022-06-14",
                    "StartDate": "2022-06-08",
                    "Subdomain": "www"
                }
            }
        ],
        "Data": [
            {
                "DateKey": "20220608",
                "HourKey": null,
                "Num": 0
            },
            {
                "DateKey": "20220609",
                "HourKey": null,
                "Num": 0
            },
            {
                "DateKey": "20220610",
                "HourKey": null,
                "Num": 0
            },
            {
                "DateKey": "20220611",
                "HourKey": null,
                "Num": 0
            },
            {
                "DateKey": "20220612",
                "HourKey": null,
                "Num": 0
            },
            {
                "DateKey": "20220613",
                "HourKey": null,
                "Num": 0
            },
            {
                "DateKey": "20220614",
                "HourKey": null,
                "Num": 0
            }
        ],
        "Info": {
            "DnsFormat": "DATE",
            "DnsTotal": 0,
            "Domain": "example.com",
            "EndDate": "2022-06-14",
            "StartDate": "2022-06-08",
            "Subdomain": "www"
        }
    }
}
```

