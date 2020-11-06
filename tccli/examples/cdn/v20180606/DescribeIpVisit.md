**Example 1: 查询活跃IP详情**



Input: 

```
tccli cdn DescribeIpVisit --cli-unfold-argument  \
    --StartTime '2018-09-04 00:00:00' \
    --EndTime '2018-09-04 12:00:00' \
    --Domains www.test.com
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "Data": [
            {
                "Resource": "multiDomains",
                "CdnData": [
                    {
                        "Metric": "ipVisit",
                        "DetailData": [
                            {
                                "Time": "2018-09-03 00:00:00",
                                "Value": 10
                            },
                            {
                                "Time": "2018-09-03 00:05:00",
                                "Value": 20
                            }
                        ],
                        "SummarizedData": {
                            "Name": "sum",
                            "Value": 30
                        }
                    }
                ]
            }
        ],
        "Interval": 5
    }
}
```

