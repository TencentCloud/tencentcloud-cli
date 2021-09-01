**Example 1: 查询报表数据**



Input: 

```
tccli cdn DescribeReportData --cli-unfold-argument  \
    --StartTime 2020-02-01 \
    --EndTime 2020-02-29 \
    --ReportType monthly \
    --Area mainland
```

Output: 
```
{
    "Response": {
        "RequestId": "8aa8eb8d-d704-45a9-ae81-9606243193cb",
        "DomainReport": [
            {
                "Resource": "www.test1.com",
                "ResourceId": "cdn-8km12345",
                "Value": 100,
                "Percentage": 50,
                "BillingValue": 100,
                "BillingPercentage": 50
            },
            {
                "Resource": "www.test2.com",
                "ResourceId": "cdn-rl523456",
                "Value": 100,
                "Percentage": 50,
                "BillingValue": 100,
                "BillingPercentage": 50
            }
        ],
        "ProjectReport": [
            {
                "Resource": "p1",
                "ResourceId": "123",
                "Value": 100,
                "Percentage": 10,
                "BillingValue": 100,
                "BillingPercentage": 10
            },
            {
                "Resource": "默认项目",
                "ResourceId": "0",
                "Value": 900,
                "Percentage": 90,
                "BillingValue": 900,
                "BillingPercentage": 90
            }
        ]
    }
}
```

