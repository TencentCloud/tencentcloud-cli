**Example 1: 查询Cdn访问数据**



Input: 

```
tccli cdn DescribeCdnData --cli-unfold-argument  \
    --StartTime '2018-09-04 00:00:00' \
    --EndTime '2018-09-04 12:00:00' \
    --Metric flux \
    --Domains www.test.com \
    --Project 0
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "Data": [
            {
                "Resource": "www.test.com",
                "CdnData": [
                    {
                        "Metric": "flux",
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
        "Interval": "5min"
    }
}
```

