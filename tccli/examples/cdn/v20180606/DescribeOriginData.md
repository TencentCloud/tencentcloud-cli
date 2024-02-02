**Example 1: 查询Cdn回源数据**



Input: 

```
tccli cdn DescribeOriginData --cli-unfold-argument  \
    --StartTime '2018-09-04 00:00:00' \
    --EndTime '2018-09-04 12:00:00' \
    --Metric flux \
    --Domains www.test.com
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "Data": [
            {
                "Resource": "www.test.com",
                "OriginData": [
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

