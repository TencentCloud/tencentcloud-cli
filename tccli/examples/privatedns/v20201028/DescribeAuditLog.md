**Example 1: 获取操作日志列表**



Input: 

```
tccli privatedns DescribeAuditLog --cli-unfold-argument  \
    --Filters.0.Name ZoneId \
    --Filters.0.Values xxxxxxx \
    --Filters.1.Name Domain \
    --Filters.1.Values a.com \
    --Filters.2.Name OperatorUin \
    --Filters.2.Values xxxxx \
    --TimeRangeBegin 2020-11-22 00:00:00 \
    --TimeRangeEnd 2020-11-23 23:59:59 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "5471b753-7d7a-8742-6cb079c6472692f2",
        "Data": [
            {
                "Resource": "all",
                "Metric": "request_count",
                "TotalCount": 48,
                "DataSet": [
                    {
                        "Date": "2020-11-22 00:00:00",
                        "OperatorUin": "100000009719",
                        "Content": "www(11111111111111) A , zone(777777)"
                    },
                    {
                        "Date": "2020-11-22 01:00:00",
                        "OperatorUin": "100000009719",
                        "Content": "www(11111111111111) A , zone(777777)"
                    },
                    {
                        "Date": "2020-11-22 02:00:00",
                        "OperatorUin": "100000009719",
                        "Content": "www.baidu.com 600 TXT aaaaaaaaaaaaaaaaaaaaaaaa zone(666666)"
                    },
                    {
                        "Date": "2020-11-22 03:00:00",
                        "OperatorUin": "100000009719",
                        "Content": "www.baidu.com 600 TXT aaaaaaaaaaaaaaaaaaaaaaaa zone(666666)"
                    },
                    {
                        "Date": "2020-11-22 04:00:00",
                        "OperatorUin": "100000009719",
                        "Content": "[子域名递归解析：关闭 -> 开启  ][], zone(444444)"
                    }
                ]
            }
        ]
    }
}
```

